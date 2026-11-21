"""配置对象的多环境加载: 分层覆盖 + 类型收敛 + 冻结只读(纯标准库)。"""
import os


BASE = {"debug": False, "port": 8000, "log_level": "info", "db_url": ""}
ENV_FILES = {
    "dev": {"debug": True, "log_level": "debug", "db_url": "sqlite:///dev.db"},
    "test": {"debug": True, "log_level": "warning", "db_url": "sqlite:///:memory:"},
    "prod": {"debug": False, "log_level": "warning", "db_url": "postgres://prod/db"},
    "staging": {"debug": False, "log_level": "info", "db_url": ""},
}
ENV_PREFIX = "APP_"


def parse_bool(raw):
    lowered = raw.strip().lower()
    if lowered in ("1", "true", "yes", "on"):
        return True
    if lowered in ("0", "false", "no", "off"):
        return False
    raise ValueError("布尔配置无法解析: %r" % raw)


class FrozenConfig:
    """只读配置对象: 属性访问, 拒绝写入, 配置错误在启动期暴露。"""

    def __init__(self, data):
        object.__setattr__(self, "_data", dict(data))

    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, "_data")[name]
        except KeyError:
            raise AttributeError("配置无此项: %s" % name)

    def __setattr__(self, name, value):
        raise TypeError("配置对象只读, 请在加载层改")

    def as_dict(self):
        return dict(object.__getattribute__(self, "_data"))


def load(env_name, environ):
    """三层覆盖: 基础默认 -> 环境文件 -> APP_ 前缀环境变量; 类型按默认值收敛。"""
    if env_name not in ENV_FILES:
        raise ValueError("未知环境: %s, 可选: %s" % (env_name, ",".join(sorted(ENV_FILES))))
    merged = dict(BASE)
    merged.update(ENV_FILES[env_name])
    for key, raw in environ.items():
        if not key.startswith(ENV_PREFIX):
            continue
        name = key[len(ENV_PREFIX):].lower()
        if name not in merged:
            continue  # 不认识的 APP_ 变量忽略, 防止拼错悄悄生效
        current = merged[name]
        if isinstance(current, bool):
            merged[name] = parse_bool(raw)
        elif isinstance(current, int):
            merged[name] = int(raw)
        else:
            merged[name] = raw
    if not merged["db_url"]:
        raise ValueError("db_url 未配置, fail-fast 拒绝启动")
    return FrozenConfig(merged)


cfg = load("dev", {})
print("dev:", cfg.as_dict())
assert cfg.debug is True and cfg.port == 8000 and cfg.log_level == "debug"

cfg = load("prod", {"APP_PORT": "9000", "APP_DEBUG": "1", "APP_LOG_LEVEL": "info"})
print("prod+env:", cfg.as_dict())
assert cfg.port == 9000 and isinstance(cfg.port, int), "字符串环境变量收敛为 int"
assert cfg.debug is True, "布尔环境变量按语义解析"

cfg = load("test", {"APP_DEBUG": "0"})
assert cfg.debug is False

for bad_env, why in [
    ({"APP_PORT": "abc"}, "int 转型失败"),
    ({"APP_DEBUG": "maybe"}, "布尔解析失败"),
]:
    try:
        load("prod", bad_env)
        raise AssertionError("应当报错: %s" % why)
    except ValueError as e:
        print("启动期报错 [%s]:" % why, e)

try:
    load("staging", {})
except ValueError as e:
    print("必填缺失 fail-fast:", e)

try:
    load("uat", {})
except ValueError as e:
    print("未知环境拒绝:", e)

cfg = load("prod", {})
try:
    cfg.port = 1
    raise AssertionError("配置对象应当只读")
except TypeError as e:
    print("写入被拒:", e)
try:
    cfg.por
except AttributeError as e:
    print("拼错键暴露:", e)
print("多环境配置加载演示通过")
