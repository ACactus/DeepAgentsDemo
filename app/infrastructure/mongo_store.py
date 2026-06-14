from langgraph.store.mongodb import MongoDBStore
from pymongo import MongoClient

from app.core.config import Settings, settings


def create_mongodb_store(config: Settings = settings) -> MongoDBStore:
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

    client = MongoClient(**client_kwargs)
    collection = client[config.mongo_db][config.mongo_collection]
    return MongoDBStore(collection=collection)
