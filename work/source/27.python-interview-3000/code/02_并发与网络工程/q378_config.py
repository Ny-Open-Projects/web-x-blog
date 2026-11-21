"""配置加载与校验:环境变量 + fail-fast + 脱敏。"""
import os


class ConfigError(Exception):
    pass


REQUIRED_KEYS = ("DATABASE_URL", "REDIS_URL", "JWT_SECRET")


def load_config(environ=None) -> dict:
    env = environ if environ is not None else os.environ
    missing = [k for k in REQUIRED_KEYS if not env.get(k)]
    if missing:
        raise ConfigError(f"缺少必需配置: {missing}, 请通过环境变量注入")
    cfg = {k: env[k] for k in REQUIRED_KEYS}
    cfg["DEBUG"] = env.get("DEBUG", "false").lower() == "true"
    return cfg


def mask(secret: str, keep: int = 4) -> str:
    """日志脱敏:只保留尾部 4 位。"""
    if len(secret) <= keep:
        return "*" * len(secret)
    return "*" * (len(secret) - keep) + secret[-keep:]


if __name__ == "__main__":
    fake_env = {
        "DATABASE_URL": "postgres://u:p@db/prod",
        "REDIS_URL": "redis://r:6379/0",
        "JWT_SECRET": "0123456789abcdef",
    }
    cfg = load_config(fake_env)
    print("JWT_SECRET 脱敏输出:", mask(cfg["JWT_SECRET"]))
    try:
        load_config({})
    except ConfigError as e:
        print("fail-fast:", e)
