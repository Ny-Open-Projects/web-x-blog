import os
try:
    from pydantic import SecretStr
    from pydantic_settings import BaseSettings
except ImportError:
    print("pip install pydantic-settings 后再运行")
    raise SystemExit(0)

os.environ["DB_PASSWORD"] = "hunter2"

class Settings(BaseSettings):
    db_password: SecretStr = SecretStr("")

s = Settings()
print("日志安全打印:", s.db_password)
print("真实值按需取出:", s.db_password.get_secret_value() == "hunter2")
print("掩码不会含明文:", "hunter2" not in str(s))
