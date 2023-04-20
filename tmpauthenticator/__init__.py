import uuid

from jupyterhub.auth import Authenticator
from jupyterhub.handlers import BaseHandler
from jupyterhub.utils import url_path_join
from tornado import gen


class TmpAuthenticateHandler(BaseHandler):
    """
    Handler for /tmplogin

    Creates a new user with a random UUID, and auto starts their server
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
        username = str(uuid.uuid4())
        user = self.user_from_username(username)
        user = await gen.maybe_future(self.process_user(user, self))
        self.set_login_cookie(user)

        # This sets a hub login cookie for the new user, overwriting old user's cookies if needed
        self.set_hub_cookie(user)

        next_url = self.get_next_url(user)

        self.redirect(next_url)


class TmpAuthenticator(Authenticator):
    """
    JupyterHub Authenticator for use with tmpnb.org

    When JupyterHub is configured to use this authenticator, visiting the home
    page immediately logs the user in with a randomly generated UUID if they
    are already not logged in, and spawns a server for them.
    """

    auto_login = True
    login_service = 'tmp'

    def process_user(self, user, handler):
        """
        Do additional arbitrary things to the created user before spawn.

        user is a user object, and handler is a TmpAuthenticateHandler object

        Should return the new user object.

        This method can be a @tornado.gen.coroutine.

        Note: This is primarily for overriding in subclasses
        """
        return user

    def get_handlers(self, app):
        # FIXME: How to do this better?
        extra_settings = {'process_user': self.process_user}
        return [('/tmplogin', TmpAuthenticateHandler, extra_settings)]

    def login_url(self, base_url):
        return url_path_join(base_url, 'tmplogin')
