import uuid

from jupyterhub.auth import Authenticator
from jupyterhub.handlers import BaseHandler
from jupyterhub.utils import url_path_join
from traitlets import Unicode, default


class TmpAuthenticateHandler(BaseHandler):
    """
    Handler for /tmplogin which is registered by TmpAuthenticator.

    Creates a new user with a random UUID as username and ensures cookies are
    updated to let JupyterHub recognize future requests as coming from the newly
    created user.
    """

    async def get(self):
        """
        Authenticate as a new user.

        Each time /tmplogin is hit, we want to create a brand new user. This lets
        users hit the hub URL, and immediately get a new server - regardless of wether
        they had already logged in or not. So /tmplogin really acts as a logout +
        login mechanism. This only happens when /tmplogin is hit - so you can use
        other parts of the hub as you normally would.
        """
        username = str(uuid.uuid4())

        # Run post_auth_hook
        #
        # Authenticator.run_post_auth_hook ref: https://github.com/jupyterhub/jupyterhub/blob/4.0.0/jupyterhub/auth.py#L400-L418
        #
        authenticated = {"name": username}
        authenticated = await self.authenticator.run_post_auth_hook(self, authenticated)

        # Create a new user
        #
        # BaseHandler.auth_to_user ref: https://github.com/jupyterhub/jupyterhub/blob/4.0.0/jupyterhub/handlers/base.py#L774-L821
        #
        user = await self.auth_to_user(authenticated)

        # Set or overwrite the login cookie to recognize the new user.
        #
        # set_login_cookie(user) sets a login cookie for the provided user via
        # set_hub_cookie(user), but only if it doesn't recognize a user from an
        # pre-existing login cookie. Due to that, we unconditionally call
        # self.set_hub_cookie(user) here.
        #
        # BaseHandler.set_login_cookie ref: https://github.com/jupyterhub/jupyterhub/blob/4.0.0/jupyterhub/handlers/base.py#L627-L628
        # BaseHandler.set_hub_cookie ref:   https://github.com/jupyterhub/jupyterhub/blob/4.0.0/jupyterhub/handlers/base.py#L623-L625
        #
        self.set_login_cookie(user)
        self.set_hub_cookie(user)

        # Login complete, redirect the user.
        #
        # BaseHandler.get_next_url ref: https://github.com/jupyterhub/jupyterhub/blob/4.0.0/jupyterhub/handlers/base.py#L646-L653
        #
        next_url = self.get_next_url(user)
        self.redirect(next_url)


class TmpAuthenticator(Authenticator):
    """
    When JupyterHub is configured to use this authenticator, visiting the home
    page immediately logs the user in with a randomly generated UUID if they are
    already not logged in, and spawns a server for them.
    """

    @default("auto_login")
    def _auto_login_default(self):
        """
        The Authenticator base class' config auto_login defaults to False, but
        we change that default to True in TmpAuthenticator. This makes users
        automatically get logged in when they hit the hub's home page, without
        requiring them to click a 'login' button.

        JupyterHub admins can still opt back to present the /hub/login page with
        the login button like this:

            c.TmpAuthenticator.auto_login = False
        """
        return True

    login_service = Unicode(
        "Automatic Temporary Credentials",
        help="""
        Text to be shown with the 'Sign in with ...' button, when auto_login is
        False.

        The Authenticator base class' login_service isn't tagged as a
        configurable traitlet, so we redefine it to allow it to be configurable
        like this:

            c.TmpAuthenticator.login_service = "your inherent worth as a human being"
        """,
    ).tag(config=True)

    def get_handlers(self, app):
        """
        Registers a dedicated endpoint and web request handler for logging in
        with tmpauthenticator. This is needed as /hub/login is reserved for
        redirecting to whats returned by login_url.

        ref: https://github.com/jupyterhub/jupyterhub/pull/1066
        """
        return [("/tmplogin", TmpAuthenticateHandler)]

    def login_url(self, base_url):
        """
        login_url is overridden as intended for Authenticator subclasses by
        jupyterhub to redirected users to it when they visit /hub/login.

        ref: https://github.com/jupyterhub/jupyterhub/blob/4.0.0/jupyterhub/auth.py#L708-L723
        """
        return url_path_join(base_url, 'tmplogin')
