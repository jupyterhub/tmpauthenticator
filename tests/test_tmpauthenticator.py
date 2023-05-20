import pytest
from yarl import URL


async def _get_username(browser_session, app_url):
    """
    Visits /hub/home to get an _xsrf token set to cookies, that we can then
    pass as a X-XSRFToken header when accessing /hub/api, then the function
    visit /hub/api/user to get the username as recognized by JupyterHub
    based on cookies passed.
    """
    hub_url = str(app_url / "hub/")
    home_url = str(app_url / "hub/home")
    api_user_url = str(app_url / "hub/api/user")

    r = await browser_session.get(home_url)
    assert r.status == 200

    hub_cookies = browser_session.cookie_jar.filter_cookies(home_url)
    if "_xsrf" in hub_cookies:
        _xsrf = hub_cookies["_xsrf"].value
    else:
        _xsrf = ""
    headers = {
        "X-XSRFToken": _xsrf,  # required for jupyterhub>=4
        "Referer": hub_url,  # required for jupyterhub<4
        "Accept": "application/json",
    }

    r = await browser_session.get(api_user_url, headers=headers)
    assert r.status == 200
    user_api_response = await r.json()
    return user_api_response["name"]


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
    Tests that the user is redirected and finally authorized for /hub/home.
    """
    app = await hub_app(hub_config)
    app_port = URL(app.bind_url).port
    app_url = URL(f"http://localhost:{app_port}{app.base_url}")

    home_url = str(app_url / "hub/home")
    r = await browser_session.get(home_url)

    assert r.status == 200


@pytest.mark.parametrize(
    "test_setting_admin_to, test_status",
    [
        (True, 200),
        (False, 403),
    ],
)
async def test_post_auth_hook_config(
    hub_app,
    hub_config,
    browser_session,
    test_setting_admin_to,
    test_status,
):
    """
    Tests that the inherited Authenticator.post_auth_hook is respected by
    updating the authentication dictionary's admin key and accessing /hub/admin,
    which should result in a forbidden response if not configured as admin via
    the post_auth_hook.
    """

    def set_admin_post_auth_hook(authenticator, handler, authentication):
        authentication["admin"] = test_setting_admin_to
        return authentication

    hub_config.TmpAuthenticator.post_auth_hook = set_admin_post_auth_hook

    app = await hub_app(hub_config)
    app_port = URL(app.bind_url).port
    app_url = URL(f"http://localhost:{app_port}{app.base_url}")

    admin_url = str(app_url / "hub/admin")
    r = await browser_session.get(admin_url)

    assert r.status == test_status


async def test_revisit_tmplogin(
    hub_app,
    hub_config,
    browser_session,
):
    """
    Tests that we get a new user if visiting /hub/tmplogin, even if we already
    were authenticated as one as recognized by cookies.

    This is done by first visiting /hub/home which should get us logged in and
    inspecting the user via a cookie, and then /hub/tmplogin to again inspect
    the user via a cookie.
    """
    app = await hub_app(hub_config)
    app_port = URL(app.bind_url).port
    app_url = URL(f"http://localhost:{app_port}{app.base_url}")

    # first access, so we receive a new user
    first_username = await _get_username(browser_session, app_url)
    assert first_username

    # when we visit /hub/home again, we are recognized and that doesn't make us
    # arrive at /hub/login -> /hub/tmplogin, and therefore we shouldn't get a
    # new user
    assert first_username == await _get_username(browser_session, app_url)

    # we visit /hub/tmplogin and should get a _new_ user
    tmplogin_url = str(app_url / "hub/tmplogin")
    r = await browser_session.get(tmplogin_url)
    assert r.status == 200
    second_username = await _get_username(browser_session, app_url)
    assert first_username != second_username
