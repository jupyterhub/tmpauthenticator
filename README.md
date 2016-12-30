# Temporary JupyterHub Authenticator #

Simple authenticator for [JupyterHub](http://github.com/jupyter/jupyterhub/)
that gives anyone who visits the home page a user account without having to
log in using any UI at all. It also spawns a single-user server and directs
the user to it immediately, without them having to press a button.

Built primarily to help run [tmpnb](https://tmpnb.org) with JupyterHub.

## Installation ##

```
pip install jupyterhub-tmpauthenticator
```

Should install it. It has no additional dependencies beyond JupyterHub.

You can then use this as your authenticator by adding the following line to
your `jupyterhub_config.py`:

```
c.JupyterHub.authenticator_class = tmpauthenticator.TmpAuthenticator
```
