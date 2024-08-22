import orjson
from loguru import logger

from bin_lookup_api.datasources.index import index_manager
from bin_lookup_api.datasources.redis import redis_manager
from bin_lookup_api.api.models import BinResponse


async def get_bin_data(bin: int) -> BinResponse:
    # Query the index tree to get the Redis key
    start, end, key = index_manager.get_index().search(int(str(bin).ljust(18, '0')))

    if key is None:
        logger.debug(f"bin {bin} not found in index")
        return None

    logger.debug(f"Retrieved redis key {key}")

    # Retrieve the BIN data from Redis
    bin_data = await redis_manager.client.get(key)

    if bin_data is None:
        logger.debug(f"bin {bin} not found in redis")
        return None

    # Deserialize the data from Redis using orjson
    bin_data_dict = orjson.loads(bin_data.decode('utf-8'))
    bin_data_dict['BIN']=bin

    logger.debug(f"Retrieved BIN data {bin_data_dict}")

    # Convert the dictionary to a BinResponse model and return
    return BinResponse(**bin_data_dict)
