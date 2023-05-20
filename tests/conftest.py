import aiohttp
import pytest
from traitlets.config import Config
from yarl import URL

# pytest-jupyterhub provides a pytest-plugin, and from it we get various
# fixtures, where we make use of hub_app that builds on MockHub, which defaults
# to providing a MockSpawner.
#
# ref: https://github.com/jupyterhub/pytest-jupyterhub
# ref: https://github.com/jupyterhub/jupyterhub/blob/4.0.0/jupyterhub/tests/mocking.py#L224
#
pytest_plugins = [
    "jupyterhub-spawners-plugin",
]

@pytest.fixture
async def hub_config():
    """
    Represents the base configuration of relevance to test TmpAuthenticator.
    """
    config = Config()
    config.JupyterHub.authenticator_class = "tmp"
    return config

@pytest.fixture
async def browser_session():
    """
    Returns a ClientSession object from aiohttp, allowing cookies to be stored
    in between requests etc, allowing us to simulate a browser.

    ref: https://docs.aiohttp.org/en/stable/client_reference.html#client-session
    ref: https://docs.aiohttp.org/en/stable/client_reference.html#response-object
    """
    browser_session = aiohttp.ClientSession()
    try:
        yield browser_session
    finally:
        await browser_session.close()
