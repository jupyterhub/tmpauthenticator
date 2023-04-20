from setuptools import find_packages, setup

setup(
    name='jupyterhub-tmpauthenticator',
    version='1.0',
    description='JupyterHub authenticator that hands out temporary accounts for everyone',
    url='https://github.com/jupyterhub/tmpauthenticator',
    author='Yuvi Panda',
    author_email='yuvipanda@gmail.com',
    license='3 Clause BSD',
    packages=find_packages(),
)
