# Contributing

Welcome! As a [Jupyter](https://jupyter.org) project, we follow the [Jupyter contributor guide](https://docs.jupyter.org/en/latest/contributing/content-contributor.html).

## Setting up a local development environment

We ship a `jupyterhub_config.py` file that helps you test `tmpauthenticator`
locally.

1.  Clone this repository

    ```sh
    git clone https://github.com/jupyterhub/tmpauthenticator.git
    ```

2.  Setup a virtual environment. After cloning the repository, you should set up an
    isolated environment to install libraries required for running / developing
    kubespawner.

    There are many ways of doing this: conda envs, virtualenv, pipenv, etc. Pick
    your favourite. We show you how to use venv:

    ```sh
    cd tmpauthenticator

    python3 -m venv .
    source bin/activate
    ```

3.  Install a locally editable version of tmpauthenticator and its dependencies for
    running it and testing it.

    ```sh
    pip install -e .
    ```

4.  Install the nodejs based [Configurable HTTP Proxy
    (CHP)](https://github.com/jupyterhub/configurable-http-proxy), and make it
    accessible to JupyterHub.

    ```sh
    npm install configurable-http-proxy
    export PATH=$(pwd)/node_modules/.bin:$PATH
    ```

5.  Start JupyterHub

    ```sh
    # Run this from the tmpauthenticator repo's root directory where the preconfigured
    # jupyterhub_config.py file resides!
    jupyterhub
    ```

6.  Visit [http://localhost:8000/](http://localhost:8000/)!
