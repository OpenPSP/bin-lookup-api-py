from redis import asyncio as aioredis

from bin_lookup_api.settings import settings
from bin_lookup_api.logging import logger


class RedisManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(RedisManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, host: str, port: int, db: int, password: str = None):
        if not self._initialized:
            self.client = aioredis.Redis(
                host=host,
                port=port,
                db=db,
                password=password,
            )
            self._initialized = True

    def get_client(self):
        return self.client

# Create the Redis client singleton
redis_manager = RedisManager(
    host=settings.redis.host,
    port=settings.redis.port,
    db=settings.redis.db,
    password=settings.redis.password,
)
