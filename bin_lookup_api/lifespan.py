"""
    Startup and shutdown code for the whole application
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from bin_lookup_api.datasources.index import index_manager
from bin_lookup_api.datasources.redis import redis_manager
from bin_lookup_api.logging import logger
from bin_lookup_api.settings import settings


async def initialize_redis_client():
    logger.debug("Connecting redis client ...")
    try:

        # Attempt a connection to ensure the client is properly initialized
        await redis_manager.client.ping()  # This will raise an error if the connection fails

        logger.debug("Redis client connected ...")

    except Exception as e:
        logger.error(f"Failed to initialize Redis client: {e}")
        raise RuntimeError(f"Failed to initialize Redis client: {str(e)}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Asynchronous initializations on startup/shutdown
    Substitute old app.on_event("startup")
    """

    # --------------------------------------------------------------
    # Startup section
    # --------------------------------------------------------------

    try:
        # Initialize the IndexManager asynchronously using the file path from settings
        await index_manager.initialize(settings.index.file_path)
        logger.info("Index tree loaded successfully.")

        # Initialize the Redis client
        app.redis_client = initialize_redis_client()
        logger.info("Redis client initialized successfully.")

    except RuntimeError as e:
        logger.error(f"Startup error: {e}")
        raise e  # Reraise the exception to stop the application

    yield  # This point onwards is where the bin_lookup_api runs

    logger.info("Async startup completed ...")

    yield

    # --------------------------------------------------------------
    # Shutdown section
    # --------------------------------------------------------------

    logger.info("Async shutdown completed ...")
