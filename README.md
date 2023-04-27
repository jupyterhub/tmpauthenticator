# Temporary JupyterHub Authenticator

Simple authenticator for [JupyterHub](http://github.com/jupyter/jupyterhub/)
that gives anyone who visits the home page a user account without having to
log in using any UI at all. It also spawns a single-user server and directs
the user to it immediately, without them having to press a button.

Built primarily to help run [tmpnb](https://github.com/jupyter/tmpnb) with JupyterHub.

## Installation

```
pip install jupyterhub-tmpauthenticator
```

Should install it. It has no additional dependencies beyond JupyterHub.

You can then use this as your authenticator by adding the following line to
your `jupyterhub_config.py`:

```python
c.JupyterHub.authenticator_class = "tmp"
```

## Configuration

`tmpauthenticator` does not have a lot of configurable knobs, but will respect
many relevant config options in the [base JupyterHub Authenticator class](https://jupyterhub.readthedocs.io/en/stable/reference/api/auth.html).
Here are a few that are particularly useful.

### `TmpAuthenticator.auto_login`

By default, `tmpauthenticator` will automatically log the user in as soon
as they hit the landing page of the JupyterHub, without showing them any UI.
This behavior can be turned off by setting `TmpAuthenticator.auto_login` to
`False`, allowing a home page to be shown. There will be a `Sign in` button here
that will automatically authenticate the user.

```python
c.TmpAuthenticator.auto_login = False
```

### `TmpAuthenticator.login_service`

If `auto_login` is set to `False`, the value of `TmpAuthenticator.login_service`
will determine the text shown next to `Sign in` in the default home page. It
defaults to `Automatic Temporary Credentials, so the button will read as
`Sign in with Automatic Temporary Credentials`.

```python
c.TmpAuthenticator.auto_login = False
c.TmpAuthenticator.login_service = "your inherent worth as a human being"
```
