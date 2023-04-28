"""
sample jupyterhub config file for testing tmpauthenticator
"""

c = get_config()  # noqa

c.JupyterHub.authenticator_class = "tmp"  # TmpAuthenticator
c.JupyterHub.spawner_class = "simple"  # SimpleLocalProcessSpawner

# c.TmpAuthenticator.auto_login = False
# c.TmpAuthenticator.login_service = "your inherent worth as a human being"
