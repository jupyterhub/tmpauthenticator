import uuid


from jupyterhub.auth import Authenticator
from jupyterhub.handlers import BaseHandler
from jupyterhub.utils import url_path_join


class TmpAuthenticateHandler(BaseHandler):
    """
    Handler for /tmplogin

    Creates a new user with a random UUID, and auto starts their server
    """
    def get(self):
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
    def get_handlers(self, app):
        return [
            ('/tmplogin', TmpAuthenticateHandler)
        ]

    def login_url(self, base_url):
        return url_path_join(base_url, 'tmplogin')
