"""配置启动校验: 缺什么一次报全, fail-fast 拒绝带病启动(纯标准库)。"""


class ConfigError(Exception):
    pass


REQUIRED = ("db_url", "port", "workers", "secret_key")


def validate(cfg):
    errors = []
    for key in REQUIRED:
        if key not in cfg:
            errors.append(f"{key} 必填")
    db_url = cfg.get("db_url", "")
    if db_url and not db_url.startswith(("postgres://", "mysql://", "sqlite://")):
        errors.append("db_url 协议不受支持")
    try:
        port = int(cfg["port"])
        if not 1 <= port <= 65535:
            errors.append(f"port 超出 1-65535: {port}")
    except (KeyError, ValueError, TypeError):
        errors.append("port 必须是 1-65535 的整数")
    workers = cfg.get("workers")
    if not isinstance(workers, int) or workers < 1:
        errors.append(f"workers 必须是 >= 1 的整数, 当前 {workers!r}")
    secret = cfg.get("secret_key", "")
    if secret in ("", "changeme", "secret"):
        errors.append("secret_key 不能为空或使用默认值")
    if errors:
        raise ConfigError("配置校验失败:\n  - " + "\n  - ".join(errors))
    return {"db_url": db_url, "port": port, "workers": workers}


bad = {"db_url": "ftp://x", "port": "80800", "workers": 0, "secret_key": "changeme"}
try:
    validate(bad)
except ConfigError as e:
    print("坏配置一次报全:")
    print(e)

good = {"db_url": "postgres://db/app", "port": "8000", "workers": 4, "secret_key": "from-vault"}
print("修复后启动:", validate(good))
print("要点: 校验放启动期而不是首个请求期; 一次报全所有错误, 省去逐个试错的发布来回")
