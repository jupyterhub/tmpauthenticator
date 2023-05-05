"""
Test ideas:

- Validate that TmpAuthenticateHandler.get() creates a new user.
- Validate that TmpAuthenticateHandler.get() creates a new user and updates the
  login cookie even if it was already set.
- Validate that TmpAuthenticateHandler.get() redirects to something sensible.
- Validate that a configured post_auth_hook is executed.
"""
