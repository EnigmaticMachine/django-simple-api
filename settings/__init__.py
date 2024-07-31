from .base import *  # noqa: F403, F401

environment = env("DJANGO_ENV")  # noqa: F403, F401

if environment == "test":
    from .test import *  # noqa: F403, F401
