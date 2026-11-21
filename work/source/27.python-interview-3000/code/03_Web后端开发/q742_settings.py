import os
try:
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ImportError:
    print("pip install pydantic-settings 后再运行")
    raise SystemExit(0)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="APP_", env_file=".env", extra="ignore")
    env: str = "dev"
    debug: bool = False
    db_url: str = "sqlite:///dev.db"
    redis_url: str = "redis://localhost:6379/0"

os.environ["APP_ENV"] = "prod"
os.environ["APP_DEBUG"] = "false"

s = Settings()
print(s.env, s.debug, s.db_url)
print("构造参数优先级最高:", Settings(env="staging").env)
