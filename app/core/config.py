import os
from pydantic_settings import BaseSettings # BaseSettings comes from pydantic_settings
from pydantic import ConfigDict          # ConfigDict comes from pydantic

class Settings(BaseSettings):
  DB_URL: str

  model_config = ConfigDict(from_attributes=True)

settings = Settings()

# Add this for debugging:
print(f"DEBUG: DB_URL from environment: {os.getenv('DB_URL')}")
settings = Settings()
print(f"DEBUG: Settings loaded DB_URL: {settings.DB_URL}")