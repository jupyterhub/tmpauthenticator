from setuptools import find_packages, setup

with open("README.md", encoding="utf8") as f:
    readme = f.read()

setup(
    name="jupyterhub-tmpauthenticator",
    version="1.0.0",
    description="JupyterHub authenticator that hands out temporary accounts for everyone",
    url="https://github.com/jupyterhub/tmpauthenticator",
    author="Project Jupyter Contributors",  # founded by Yuvi Panda
    author_email="jupyter@googlegroups.com",
    license="3 Clause BSD",
    long_description=readme,
    long_description_content_type="text/markdown",
    entry_points={
        # Thanks to this, user are able to do:
        #
        #     c.JupyterHub.authenticator_class = "tmp"
        #
        # ref: https://jupyterhub.readthedocs.io/en/4.0.0/reference/authenticators.html#registering-custom-authenticators-via-entry-points
        #
        "jupyterhub.authenticators": [
            "tmp = tmpauthenticator:TmpAuthenticator",
        ],
    },
    packages=find_packages(),
    python_requires=">=3.8",
    install_require={
        "jupyterhub>=2.3.0",
        "traitlets",
    },
    extras_require={
        "test": [
            "aiohttp",
            "pytest",
            "pytest-asyncio",
            "pytest-cov",
            "pytest-jupyterhub",
        ],
    },
)
