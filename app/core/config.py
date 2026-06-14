import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    namespace_root: str = os.getenv("NAMESPACE_ROOT", "deepagents")
    app_id: str = os.getenv("APP_ID", "jarvis")
    agent_id: str = os.getenv("AGENT_ID", "main")
    default_user_id: str = os.getenv("USER_ID", "default_user")

    model_name: str = os.getenv("MODEL_NAME", "deepseek-ai/DeepSeek-V4-Flash")
    api_key: str | None = os.getenv("API_KEY")
    base_url: str | None = os.getenv("BASE_URL")

    mongo_host: str = os.getenv("MONGODB_HOST", "192.168.31.31")
    mongo_port: int = int(os.getenv("MONGODB_PORT", "27017"))
    mongo_user: str | None = os.getenv("MONGODB_USERNAME")
    mongo_password: str | None = os.getenv("MONGODB_PASSWORD")
    mongo_db: str = os.getenv("MONGODB_DATABASE", "deepagents")
    mongo_collection: str = os.getenv("MONGODB_COLLECTION", "agent_store")
    mongo_auth_source: str = os.getenv("MONGODB_AUTH_SOURCE", "admin")

    checkpoint_collection: str = os.getenv("MONGODB_CHECKPOINT_COLLECTION", "checkpoints")
    checkpoint_writes_collection: str = os.getenv(
        "MONGODB_CHECKPOINT_WRITES_COLLECTION",
        "checkpoint_writes",
    )


settings = Settings()
