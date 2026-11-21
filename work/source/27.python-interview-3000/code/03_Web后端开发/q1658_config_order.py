"""配置三层覆盖顺序: 内置默认 < 环境文件 < 环境变量(纯标准库深合并)。"""
import copy

DEFAULTS = {"debug": False, "db": {"host": "localhost", "port": 5432, "name": "app"},
            "log_level": "INFO", "workers": 4}
FILE_CFG = {"db": {"host": "db.internal"}, "log_level": "WARNING"}
ENV_CFG = {"db": {"port": "6543"}, "debug": "true"}      # 环境变量都是字符串


def deep_merge(base, override):
    out = copy.deepcopy(base)
    for k, v in override.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out


def coerce(env_cfg):
    """环境变量按约定转类型: bool 与数字要显式转换。"""
    fixed = {}
    for k, v in env_cfg.items():
        if k == "db":
            continue
        fixed[k] = (v.lower() == "true") if isinstance(v, str) and v.lower() in ("true", "false") else v
    fixed["db"] = {k: (int(x) if str(x).isdigit() else x) for k, x in env_cfg.get("db", {}).items()}
    return fixed


final = deep_merge(deep_merge(DEFAULTS, FILE_CFG), coerce(ENV_CFG))
for k, v in final.items():
    print(f"{k} = {v!r}")
print("顺序: 内置默认 -> 环境配置文件 -> 环境变量, 越靠后优先级越高, 12-Factor 用环境变量做运行时覆盖")
print("注意: 列表类配置整体覆盖不做合并, 避免半新半旧的中间态")
