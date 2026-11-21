"""or 默认值的陷阱:falsy 值会被误替换,is None 才是精确判断。"""


def timeout_or(config):
    return config.get("timeout") or 30         # 0 也会被换成 30


def timeout_none(config):
    value = config.get("timeout")
    return 30 if value is None else value      # 只有缺失才用默认


if __name__ == "__main__":
    for cfg in ({}, {"timeout": 0}, {"timeout": ""}, {"timeout": 5}):
        print(cfg, "-> or 写法:", timeout_or(cfg), "| is None 写法:", timeout_none(cfg))
    print("falsy 家族:", [bool(v) for v in (0, 0.0, "", [], {}, set(), None)])
    print("结论:缺失语义用 is None;or 只用于空值与缺失本就等价的场景")
