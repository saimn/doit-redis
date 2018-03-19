# Redis backend for [doit](https://github.com/pydoit/doit).

This plugin for [doit](https://github.com/pydoit/doit) add a new `redis`
backend, using the [redis-py](https://github.com/andymccurdy/redis-py) client.

This allows to have a more suitable backend for multi-processing, and it even
allows to run multiple doit processes in parallel.

Install:
```
$ pip install doit-redis
```

Usage:
```
DOIT_CONFIG = {
    'backend': 'redis',
    'dep_file': 'redis://[:password]@localhost:6379/0',  # optional
}
```
