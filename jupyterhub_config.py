"""
sample jupyterhub config file for testing tmpauthenticator
"""

c = get_config()  # noqa

from tmpauthenticator import TmpAuthenticator

c.JupyterHub.authenticator_class = TmpAuthenticator

from jupyterhub.spawner import SimpleLocalProcessSpawner

c.JupyterHub.spawner_class = SimpleLocalProcessSpawner
