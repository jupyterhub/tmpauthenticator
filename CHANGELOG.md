# Changelog

## 1.0

### [1.0.0] - 2023-04-22

#### Breaking Changes

- Python >=3.8 and JupyterHub >=2.3.0 is now required
- Logging in while already logged in by visiting `/hub/tmplogin` now provides
  the visitor with a new user identity to allow startup of a new server. The
  `TmpAuthenticator.force_new_server` config is removed as no longer relevant as
  part of this change.
- The `TmpAuthenticator.process_user` function is no longer provided for
  subclasses to override. The configurable [`Authenticator.post_auth_hook`] can
  be used to accomplish the same things though.

[`Authenticator.post_auth_hook`]: https://jupyterhub.readthedocs.io/en/stable/reference/api/auth.html#jupyterhub.auth.Authenticator.post_auth_hook

#### Bugs fixed

- BREAKING: Logout current user when new user logs in (removes `force_new_server`) [#22](https://github.com/jupyterhub/tmpauthenticator/pull/22) ([@yuvipanda](https://github.com/yuvipanda))
- Fix reference to unbound variable [#25](https://github.com/jupyterhub/tmpauthenticator/pull/25) ([@yuvipanda](https://github.com/yuvipanda))

#### Maintenance improvements

- setup.py: update author, comment about being founded by Yuvi [#48](https://github.com/jupyterhub/tmpauthenticator/pull/48) ([@consideratio](https://github.com/consideratio))
- Add tests, require py38 and jupyterhub 2.3+ [#47](https://github.com/jupyterhub/tmpauthenticator/pull/47) ([@consideratio](https://github.com/consideratio))
- Remove process_user and fix support for post_auth_hook [#45](https://github.com/jupyterhub/tmpauthenticator/pull/45) ([@consideratio](https://github.com/consideratio))

#### Documentation improvements

- docs: backfill changelog for 0.1-0.6, add changelog for 1.0.0 [#32](https://github.com/jupyterhub/tmpauthenticator/pull/32) ([@consideratio](https://github.com/consideratio))
- Update CONTRIBUTING.md [#24](https://github.com/jupyterhub/tmpauthenticator/pull/24) ([@evanlinde](https://github.com/evanlinde))

#### Contributors to this release

[@evanlinde](https://github.com/search?q=repo%3Ajupyterhub%2Ftmpauthenticator+involves%3Aevanlinde+updated%3A2016-12-30..2023-04-19&type=Issues) | [@fm75](https://github.com/search?q=repo%3Ajupyterhub%2Ftmpauthenticator+involves%3Afm75+updated%3A2016-12-30..2023-04-19&type=Issues) | [@hilhert](https://github.com/search?q=repo%3Ajupyterhub%2Ftmpauthenticator+involves%3Ahilhert+updated%3A2016-12-30..2023-04-19&type=Issues) | [@manics](https://github.com/search?q=repo%3Ajupyterhub%2Ftmpauthenticator+involves%3Amanics+updated%3A2016-12-30..2023-04-19&type=Issues) | [@minrk](https://github.com/search?q=repo%3Ajupyterhub%2Ftmpauthenticator+involves%3Aminrk+updated%3A2016-12-30..2023-04-19&type=Issues) | [@mohirio](https://github.com/search?q=repo%3Ajupyterhub%2Ftmpauthenticator+involves%3Amohirio+updated%3A2016-12-30..2023-04-19&type=Issues) | [@sridhar562345](https://github.com/search?q=repo%3Ajupyterhub%2Ftmpauthenticator+involves%3Asridhar562345+updated%3A2016-12-30..2023-04-19&type=Issues) | [@takluyver](https://github.com/search?q=repo%3Ajupyterhub%2Ftmpauthenticator+involves%3Atakluyver+updated%3A2016-12-30..2023-04-19&type=Issues) | [@tkw1536](https://github.com/search?q=repo%3Ajupyterhub%2Ftmpauthenticator+involves%3Atkw1536+updated%3A2016-12-30..2023-04-19&type=Issues) | [@willingc](https://github.com/search?q=repo%3Ajupyterhub%2Ftmpauthenticator+involves%3Awillingc+updated%3A2016-12-30..2023-04-19&type=Issues) | [@yuvipanda](https://github.com/search?q=repo%3Ajupyterhub%2Ftmpauthenticator+involves%3Ayuvipanda+updated%3A2016-12-30..2023-04-19&type=Issues)

## 0.6

### [0.6] - 2019-05-18

- Compatibility with JupyterHub v1.0.0 [#18](https://github.com/jupyterhub/tmpauthenticator/pull/18) ([@mohirio](https://github.com/mohirio))

## 0.5

### [0.5] - 2017-11-02

- Bump version number [#9](https://github.com/jupyterhub/tmpauthenticator/pull/9) ([@yuvipanda](https://github.com/yuvipanda))
- Add MANIFEST.in [#8](https://github.com/jupyterhub/tmpauthenticator/pull/8) ([@takluyver](https://github.com/takluyver))
- Respect 'next' parameter after login [#6](https://github.com/jupyterhub/tmpauthenticator/pull/6) ([@tkw1536](https://github.com/tkw1536))
- Update LICENSE [#4](https://github.com/jupyterhub/tmpauthenticator/pull/4) ([@fm75](https://github.com/fm75))
- Update to work with JupyterHub 0.8 [#2](https://github.com/jupyterhub/tmpauthenticator/pull/2) ([@yuvipanda](https://github.com/yuvipanda))
- Create CONTRIBUTING.md [c9db294](https://github.com/jupyterhub/tmpauthenticator/commit/c9db294) ([@yuvipanda](https://github.com/willingc))
- simplify logic a bit [#1](https://github.com/jupyterhub/tmpauthenticator/pull/1) ([@minrk](https://github.com/minrk))
- Respect force_new_server setting properly [1804b92](https://github.com/jupyterhub/tmpauthenticator/commit/1804b92) ([@yuvipanda](https://github.com/yuvipanda))

## 0.4

### [0.4] - 2017-05-08

- Bump package version [6964764](https://github.com/jupyterhub/tmpauthenticator/commit/6964764) ([@yuvipanda](https://github.com/yuvipanda))
- Attempt to fix force_new_servers [313b8f2](https://github.com/jupyterhub/tmpauthenticator/commit/313b8f2) ([@yuvipanda](https://github.com/yuvipanda))
- Add a hack to make the force_new_server 'work'[4ee14d8](https://github.com/jupyterhub/tmpauthenticator/commit/4ee14d8) ([@yuvipanda](https://github.com/yuvipanda))
- Make starting a new server actually stop the old one [6300859](https://github.com/jupyterhub/tmpauthenticator/commit/6300859) ([@yuvipanda](https://github.com/yuvipanda))
- Bump version number [45b2062](https://github.com/jupyterhub/tmpauthenticator/commit/45b2062) ([@yuvipanda](https://github.com/yuvipanda))

## 0.3

### [0.3] - 2017-05-04

- Add ability for subclasses to modify created user before spawning [8231fda](https://github.com/jupyterhub/tmpauthenticator/commit/8231fda) ([@yuvipanda](https://github.com/yuvipanda))
- Add feature to force a new single-user server each time [b7aa546](https://github.com/jupyterhub/tmpauthenticator/commit/b7aa546) ([@yuvipanda](https://github.com/yuvipanda))

## 0.2

### [0.2] - 2017-05-01

- Version bump [0c81ac0](https://github.com/jupyterhub/tmpauthenticator/commit/0c81ac0) ([@yuvipanda](https://github.com/yuvipanda))
- Add .gitignore [bed1a79](https://github.com/jupyterhub/tmpauthenticator/commit/bed1a79) ([@yuvipanda](https://github.com/yuvipanda))

## 0.1

### [0.1] - 2016-12-30

- Initial commit [cf52bc2](https://github.com/jupyterhub/tmpauthenticator/commit/cf52bc2) ([@yuvipanda](https://github.com/yuvipanda))

[1.0.0]: https://github.com/jupyterhub/tmpauthenticator/compare/v0.6...v1.0.0
[0.6]: https://github.com/jupyterhub/tmpauthenticator/compare/v0.5...v0.6
[0.5]: https://github.com/jupyterhub/tmpauthenticator/compare/v0.4...v0.5
[0.4]: https://github.com/jupyterhub/tmpauthenticator/compare/v0.3...v0.4
[0.3]: https://github.com/jupyterhub/tmpauthenticator/compare/v0.2...v0.3
[0.2]: https://github.com/jupyterhub/tmpauthenticator/compare/v0.1...v0.2
[0.1]: https://github.com/jupyterhub/tmpauthenticator/commit/cf52bc2
