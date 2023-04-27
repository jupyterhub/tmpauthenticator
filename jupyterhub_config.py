"""
sample jupyterhub config file for testing tmpauthenticator
"""

c = get_config()  # noqa

c.JupyterHub.authenticator_class = "tmp"

from jupyterhub.spawner import SimpleLocalProcessSpawner

c.JupyterHub.spawner_class = SimpleLocalProcessSpawner
