---
title: [Q1282] 哨兵对象:None 不够用时的「缺失」表达
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1282 · 哨兵对象:None 不够用时的「缺失」表达

> 难度:★★☆☆☆ | 标签:哨兵, API 设计, 默认参数

**问**:函数默认参数想表达「调用方没传」,可 None 又是合法业务值,怎么办?为什么不直接用 `default=None`?

**答**:模块级哨兵 `_MISSING = object()`:身份唯一、不可能与任何用户值冲突,参数默认 `default=_MISSING`,函数内用 `is` 判断调用方是否显式传值。经典场景是配置读取——`{"retries": None}` 表示「显式禁用」,键缺失表示「未配置」,两者语义不同,`default=None` 会把它们合并成一个。这也是 Q017/Q004 之外第三个默认参数话题:可变默认参数用 None 兜,「缺失与 None 有别」用哨兵兜。公开 API 里哨兵命名要导出(如 `UNSET`),调用方需要「把参数显式置为缺失」时可以引用它;标准库自己的例子是 `dict.setdefault` 返回值、`dataclasses.MISSING`、`argparse` 的 SUPPRESS。

```python
# file: code/01_语言核心与底层/q1282_sentinel.py
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
```

**追问**:1) 能用字符串或类对象当哨兵吗?——能但脆弱:用户可能恰好传同值字符串;object() 身份唯一且无值语义,`is` 判断永不错配,是唯一推荐形态。2) 哨兵的惯用法?——模块级 _MISSING = object(),函数签名 default=_MISSING,内部 `if value is _MISSING:` 区分「未传」与「传了 None」;dict.get(key, sentinel) 同理。3) 与枚举的配合?——语义化哨兵可定义 enum(auto() 单例),既保身份唯一又有可读名字;序列化边界要转回普通值。4) 生产陷阱?——None 一词两义(缺失 vs 值就是 None)导致语义坍缩;字符串哨兵被用户输入碰撞;哨兵对象进 pickle/JSON 失败(要模块级可寻址或序列化前转换)。
