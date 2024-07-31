from .base import *  # noqa: F403, F401

environment = env("DJANGO_ENV")  # noqa: F403, F401

if environment == "prod":
    from .prod import *  # noqa: F403, F401
else:
    from .test import *  # noqa: F403, F401
