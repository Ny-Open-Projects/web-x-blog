---
title: [Q2892] 序列化往返的一致性测试:json 往返会丢什么
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2892 · 序列化往返的一致性测试:json 往返会丢什么

> 难度:★★★☆☆ | 标签:json, 序列化, 往返测试

**问**:怎么给序列化写「往返一致性」测试?json 的 dumps 与 loads 走一圈,哪些东西会变、哪些直接报错?

**答**:往返测试的骨架是 `json.loads(json.dumps(x))` 后与原值比较,把结果分三类处理:**无变形**的(dict、list、str、int、float、bool、None)直接断言相等,实测连 0.1+0.2 的精度都能保住,json 用 repr 最短表示法,浮点往返无损;**已知变形**的做白名单断言——tuple 变 list、int 键变字符串、NaN 因 nan 不等于自身而在相等性意义上「变形」但值语义无损;**直接失败**的(TypeError:set、datetime)说明这些类型根本不允许出现在 json 边界。最值得演示的坑是**键碰撞静默丢数据**:`{1: "int", "1": "str"}` 序列化成两个 "1" 键,load 回来只剩最后一个,数据无声丢失。工程顺序是先定义序列化契约——键统一字符串、类型白名单,再让测试对契约外类型 fail-fast。

```python
# file: code/01_语言核心与底层/q2892_json_roundtrip.py
"""序列化往返的一致性测试:json 往返会丢什么、改什么。"""
import json
from datetime import datetime


def roundtrip(obj):
    return json.loads(json.dumps(obj))


def check(label, original, expect_equal=True):
    try:
        back = roundtrip(original)
    except (TypeError, ValueError) as e:
        print(f"{label:<18} 序列化直接失败:{type(e).__name__}")
        return
    same = back == original
    note = "往返相等" if same else f"往返变形 {original!r} -> {back!r}"
    flag = "符合预期" if same == expect_equal else "预期外"
    print(f"{label:<18} {note} [{flag}]")


if __name__ == "__main__":
    check("dict 与 list", {"a": [1, 2, {"b": None}]})
    check("tuple 变 list", (1, 2), expect_equal=False)
    check("int 键变字符串", {1: "x"}, expect_equal=False)
    check("键碰撞静默丢数据", {1: "int", "1": "str"}, expect_equal=False)
    check("float 精度", 0.1 + 0.2)
    check("NaN 的往返", float("nan"), expect_equal=False)
    check("set 不受支持", {1, 2})
    check("datetime 不受支持", datetime(2026, 1, 1))

    # 一致性测试的工程写法:规范化负载先断言无变形,已知变形白名单化
    payload = {"id": 7, "tags": ["a", "b"], "score": 0.25}
    assert roundtrip(payload) == payload
    print("规范化负载往返相等:断言通过")
```

**追问**:1) 键碰撞这么危险为什么很少被发现?——它需要「int 键与内容相同的 str 键同时存在」这种少见构造而且不抛任何错;防御手段是序列化前统一把键转成字符串并做冲突检测。2) 往返会丢什么的全清单?——int 键转 str(冲突)、tuple 键变字符串、float/int 边界(大整数精度)、datetime 需要 default、None/NaN 键变 "null"/"NaN";round-trip 测试是唯一的信任来源。3) 一致性测试的设计?——构造覆盖所有边界类型的样本;dumps→loads→相等断言;冲突检测(统一键后查重复);按 schema 演进补样本。4) 生产陷阱?——带 int 键的 dict 直接进 JSON(静默合并);NaN 进 JSON(非标准,前端解析崩);往返测试只有 happy path。
