from langgraph.checkpoint.mongodb import MongoDBSaver

from app.core.config import Settings, settings
from app.infrastructure.mongo_store import create_mongo_client


def create_mongodb_checkpointer(config: Settings = settings) -> MongoDBSaver:
    return MongoDBSaver(
        create_mongo_client(config),
        db_name=config.mongo_db,
        checkpoint_collection_name=config.checkpoint_collection,
        writes_collection_name=config.checkpoint_writes_collection,
    )
