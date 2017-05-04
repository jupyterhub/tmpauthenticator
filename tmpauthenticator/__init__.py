import uuid

from traitlets import Bool

from jupyterhub.auth import Authenticator
from jupyterhub.handlers import BaseHandler
from jupyterhub.utils import url_path_join


class TmpAuthenticateHandler(BaseHandler):
    """
    Handler for /tmplogin

    Creates a new user with a random UUID, and auto starts their server
    """
    def initialize(self, force_new_server):
        super().initialize()
        self.force_new_server = force_new_server

    def get(self):
        if self.force_new_server:
            self.clear_login_cookie()
        username = str(uuid.uuid4())
        user = self.user_from_username(username)
        self.set_login_cookie(user)
        self.redirect(url_path_join(
            self.hub.server.base_url,
            'spawn'
        ))


class TmpAuthenticator(Authenticator):
    """
    JupyterHub Authenticator for use with tmpnb.org

    When JupyterHub is configured to use this authenticator, visiting the home
    page immediately logs the user in with a randomly generated UUID if they
    are already not logged in, and spawns a server for them.
    """
    force_new_server = Bool(
        False,
        help="""
        Automatically log out the user first before logging them in.

        When set to True, users going to /hub/login will *always* get a
        new single-user server. When set to False, they'll just be
        redirected to their current session if one exists.
        """,
        config=True
    )

    def get_handlers(self, app):
        # FIXME: How to do this better?
        extra_settings = {
            'force_new_server': self.force_new_server
        }
        return [
            ('/tmplogin', TmpAuthenticateHandler, extra_settings)
        ]

    def login_url(self, base_url):
        return url_path_join(base_url, 'tmplogin')
