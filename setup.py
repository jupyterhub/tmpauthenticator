from setuptools import find_packages, setup

setup(
    name='jupyterhub-tmpauthenticator',
    version='1.0.0.dev',
    description='JupyterHub authenticator that hands out temporary accounts for everyone',
    url='https://github.com/jupyterhub/tmpauthenticator',
    author='Yuvi Panda',
    author_email='yuvipanda@gmail.com',
    license='3 Clause BSD',
    install_requires=[
        'jupyterhub',
    ],
    entry_points={
        # Thanks to this, user are able to do:
        #
        #     c.JupyterHub.authenticator_class = "tmp"
        #
        # ref: https://jupyterhub.readthedocs.io/en/4.0.0/reference/authenticators.html#registering-custom-authenticators-via-entry-points
        #
        'jupyterhub.authenticators': [
            'tmp = tmpauthenticator:TmpAuthenticator',
        ],
    },
    packages=find_packages(),
)
