from pydantic_seattings import BaseSettings
from typing import Any


class settings(BaseSettings):
    OPENAI_API_KEY: Any 

    class confid():
        env_file = ".env"


Settings = settings()

