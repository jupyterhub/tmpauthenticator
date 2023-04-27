import inspect
import uuid

from jupyterhub.auth import Authenticator
from jupyterhub.handlers import BaseHandler
from jupyterhub.utils import url_path_join
from traitlets import default


class TmpAuthenticateHandler(BaseHandler):
    """
    Handler for /tmplogin

    Creates a new user with a random UUID as username and ensures cookies are
    updated to let JupyterHub recognize future requests as coming from the newly
    created user.
    """

    def initialize(self, process_user):
        super().initialize()
        self.process_user = process_user

    async def get(self):
        """
        Authenticate as a new user.

        Each time /tmplogin is hit, we want to create a brand new user. This lets
        users hit the hub URL, and immediately get a new server - regardless of wether
        they had already logged in or not. So /tmplogin really acts as a logout +
        login mechanism. This only happens when /tmplogin is hit - so you can use
        other parts of the hub as you normally would.
        """
        # Create a new user.
        #
        # user_from_username ref: https://github.com/jupyterhub/jupyterhub/blob/4.0.0/jupyterhub/handlers/base.py#L504-L505
        #
        username = str(uuid.uuid4())
        user = self.user_from_username(username)

        # Let a subclasses of TmpAuthenticator process the new user by
        # overriding TmpAuthenticator.process_user.
        #
        user = self.process_user(user, self)
        if inspect.isawaitable(user):
            user = await user

        # Set or overwrite the login cookie to recognize the new user.
        #
        # set_login_cookie(user) sets a login cookie for the provided user via
        # set_hub_cookie(user), but only if it doesn't recognize a user from an
        # pre-existing login cookie. Due to that, we unconditionally call
        # self.set_hub_cookie(user) here.
        #
        # set_login_cookie ref: https://github.com/jupyterhub/jupyterhub/blob/4.0.0/jupyterhub/handlers/base.py#L627-L628
        # set_hub_cookie ref:   https://github.com/jupyterhub/jupyterhub/blob/4.0.0/jupyterhub/handlers/base.py#L623-L625
        #
        self.set_login_cookie(user)
        self.set_hub_cookie(user)

        # Login complete, redirect the user.
        #
        # get_next_url ref: https://github.com/jupyterhub/jupyterhub/blob/4.0.0/jupyterhub/handlers/base.py#L646-L653
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

    # Text to be shown with the 'Sign in with...' button, when auto_login is False
    login_service = 'Automatic Temporary Credentials'

    def process_user(self, user, handler):
        """
        Do additional arbitrary things to the created user before spawn.

        user is a user object, and handler is a TmpAuthenticateHandler object

        Should return the new user object.

        This method can be a coroutine.

        Note: This is primarily for overriding in subclasses
        """
        return user

    def get_handlers(self, app):
        # FIXME: How to do this better?
        extra_settings = {'process_user': self.process_user}
        return [('/tmplogin', TmpAuthenticateHandler, extra_settings)]

    def login_url(self, base_url):
        return url_path_join(base_url, 'tmplogin')
