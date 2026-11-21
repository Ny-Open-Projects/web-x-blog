try:
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ImportError:
    print("该题演示需要第三方库 pydantic_settings:pip install pydantic-settings,原理见正文")
    raise SystemExit(0)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "demo"
    debug: bool = False
    db_url: str
    api_keys: list[str] = []


def load_settings(monkeypatch_env: dict) -> Settings:
    import os
    for k, v in monkeypatch_env.items():
        os.environ[k] = v
    return Settings(_env_file=None)


def test_settings_from_env():
    s = load_settings({
        "DB_URL": "postgres://localhost/t",
        "DEBUG": "true",
        "API_KEYS": '["k1","k2"]',
    })
    assert s.debug is True
    assert s.api_keys == ["k1", "k2"]
    assert s.db_url.startswith("postgres")
