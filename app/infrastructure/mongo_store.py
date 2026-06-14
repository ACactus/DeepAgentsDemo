from functools import lru_cache

from langgraph.store.mongodb import MongoDBStore
from pymongo import MongoClient

from app.core.config import Settings, settings


@lru_cache(maxsize=1)
def create_mongo_client(config: Settings = settings) -> MongoClient:
    client_kwargs = {
        "host": config.mongo_host,
        "port": config.mongo_port,
    }
    if config.mongo_user:
        client_kwargs["username"] = config.mongo_user
    if config.mongo_password:
        client_kwargs["password"] = config.mongo_password
    if config.mongo_user or config.mongo_password:
        client_kwargs["authSource"] = config.mongo_auth_source

    return MongoClient(**client_kwargs)


def create_mongodb_store(config: Settings = settings) -> MongoDBStore:
    client = create_mongo_client(config)
    collection = client[config.mongo_db][config.mongo_collection]
    return MongoDBStore(collection=collection)
