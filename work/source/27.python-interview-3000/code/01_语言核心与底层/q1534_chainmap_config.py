from collections import ChainMap
import os

FILE_DEFAULTS = {"host": "localhost", "port": "5432", "debug": "0", "retries": "3"}


def load_settings(cli_opts, env=None):
    """优先级:CLI 参数 > 环境变量 > 配置文件默认值。"""
    if env is None:
        env = {k[4:].lower(): v for k, v in os.environ.items()
               if k.startswith("APP_")}
    return ChainMap(cli_opts, env, FILE_DEFAULTS)


if __name__ == "__main__":
    env = {"debug": "1", "host": "db.internal"}
    cfg = load_settings({"port": "6432"}, env=env)
    print("port   :", cfg["port"], "   # CLI 层覆盖")
    print("host   :", cfg["host"], " # env 层覆盖")
    print("debug  :", cfg["debug"], "   # env 覆盖文件默认")
    print("retries:", cfg["retries"], "   # 三层都命中不了才落到文件默认")

    # 写操作只落到第一层:默认配置不被污染
    cfg["retries"] = "5"
    print("after write:", cfg["retries"], "| defaults untouched:",
          FILE_DEFAULTS["retries"])

    # new_child 派生作用域:请求级覆盖,丢弃 child 即回滚
    request_cfg = cfg.new_child({"timeout": "30"})
    print("request scope timeout:", request_cfg["timeout"])
    print("outer scope has no timeout:", "timeout" in cfg)

    # 上游 dict 更新实时可见:零拷贝
    env["extra"] = "seen"
    print("live view:", cfg["extra"])

    print("maps count:", len(cfg.maps), "| parents layers:", len(cfg.parents.maps))
