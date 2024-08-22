import asyncio

import orjson
from avl_range_tree.avl_tree import RangeTree

from bin_lookup_api.logging import logger


class IndexManager:
    _instance = None
    _lock = asyncio.Lock()
    _index_tree = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(IndexManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    async def initialize(self, file_path: str):
        async with self._lock:
            if not self._initialized:
                loop = asyncio.get_event_loop()
                # Run the blocking I/O operation in a thread pool to avoid blocking the event loop
                self._index_tree = await loop.run_in_executor(None, self._load_index, file_path)
                self._initialized = True

    def _load_index(self, file_path: str):
        try:
            with open(file_path, "rb") as f:
                tree_data = f.read()

                def json_deserializer(data: str):
                    return orjson.loads(data)

                index_tree = RangeTree.deserialize(tree_data.decode('utf-8'), json_deserializer)
                return index_tree
        except Exception as e:
            logger.error(f"Failed to load the index tree: {e}")
            raise RuntimeError(f"Failed to load the index tree: {str(e)}")

    def get_index(self):
        if not self._initialized or self._index_tree is None:
            raise RuntimeError("Index tree is not initialized. Call 'initialize' first.")
        return self._index_tree

# Create the IndexManager singleton
index_manager = IndexManager()
