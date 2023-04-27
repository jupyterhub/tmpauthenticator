"""
Test ideas:

- Validate that TmpAuthenticateHandler.get() creates a new user.
- Validate that TmpAuthenticateHandler.get() creates a new user and updates the
  login cookie even if it was already set.
- Validate that TmpAuthenticateHandler.get() redirects to something sensible.

Bonus:

- Test process_user by creating a subclass doing something.
"""