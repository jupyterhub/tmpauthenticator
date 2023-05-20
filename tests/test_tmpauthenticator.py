"""
Test ideas:

- Validate that TmpAuthenticateHandler.get() creates a new user and updates the
  login cookie even if it was already set.
- Validate that a configured post_auth_hook is executed.
"""
import pytest
from yarl import URL


@pytest.mark.parametrize(
    "test_config, test_status, test_location, test_url",
    [
        ({}, 302, "hub/tmplogin", None),
        ({"TmpAuthenticator": {"auto_login": True}}, 302, "hub/tmplogin", None),
        ({"TmpAuthenticator": {"auto_login": False}}, 200, None, "hub/login"),
    ],
)
async def test_auto_login_config(
    hub_app,
    hub_config,
    browser_session,
    test_config,
    test_status,
    test_location,
    test_url,
):
    """
    Tests TmpAuthenticator.auto_login's behavior when its default value is used,
    and when its explicitly set.
    """
    hub_config.merge(test_config)

    app = await hub_app(hub_config)
    app_port = URL(app.bind_url).port
    app_url = URL(f"http://localhost:{app_port}{app.base_url}")

    login_url = str(app_url / "hub/login")
    r = await browser_session.get(login_url, allow_redirects=False)

    assert r.status == test_status
    if test_url:
        assert test_url in str(r.url)
    if test_location:
        assert test_location in r.headers["Location"]


async def test_login(
    hub_app,
    hub_config,
    browser_session,
):
    """
    Tests that the user is redirected and finally authorized for /hub/home
    """
    app = await hub_app(hub_config)
    app_port = URL(app.bind_url).port
    app_url = URL(f"http://localhost:{app_port}{app.base_url}")

    home_url = str(app_url / "hub/home")
    r = await browser_session.get(home_url)

    assert r.status == 200
