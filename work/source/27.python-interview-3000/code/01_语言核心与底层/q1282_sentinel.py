MISSING = object()                      # 模块级哨兵:身份唯一


def config_get(conf, key, default=MISSING):
    if key in conf:
        return conf[key]
    if default is MISSING:
        raise KeyError("missing config key: %r" % (key,))
    return default


if __name__ == "__main__":
    conf = {"retries": None}            # None 表示显式禁用,与缺失不同
    print("retries (显式 None):", config_get(conf, "retries", default=3))
    print("timeout (未配置)    :", config_get(conf, "timeout", default=30))
    try:
        config_get(conf, "missing")
    except KeyError as e:
        print("missing key ->", e)
