---
title: [Q369] JSON 序列化进阶:default 与自定义 Encoder
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q369 · JSON 序列化进阶:default 与自定义 Encoder

> 难度:★★☆ | 标签:JSON, 序列化

**问**:`json.dumps` 遇到 `datetime`、`Decimal`、自定义对象会怎样?怎么优雅支持?

**答**:会抛 `TypeError`。方案:①给 `dumps` 传 `default=` 回调,遇到不认识的类型时返回可序列化对象,回调里再不认识就 `raise TypeError`;②继承 `json.JSONEncoder` 覆写 `default`(效果同①,可复用);③反序列化用 `object_hook` 把 dict 还原成对象。注意约定一种统一格式,如时间用 ISO8601 字符串、Decimal 转字符串避免精度丢失。

```python
# file: code/02_并发与网络工程/q369_json_default.py
"""json 自定义序列化与反序列化。"""
import datetime as dt
import json
from decimal import Decimal


def json_default(obj):
    if isinstance(obj, (dt.datetime, dt.date)):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return str(obj)  # 金额转字符串,防浮点精度丢失
    if isinstance(obj, set):
        return sorted(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def _revive(d: dict):
    if "created_at" in d:
        d["created_at"] = dt.datetime.fromisoformat(d["created_at"])
    return d


class Order:
    def __init__(self):
        self.id = "A001"
        self.amount = Decimal("19.99")
        self.tags = {"vip", "paid"}
        self.created_at = dt.datetime(2026, 11, 1, 10, 0, 0)


if __name__ == "__main__":
    order = Order()
    text = json.dumps(order.__dict__, default=json_default, ensure_ascii=False, indent=2)
    print(text)
    back = json.loads(text, object_hook=_revive)
    print(type(back["created_at"]), back["amount"])
```

**追问**:
- `ensure_ascii=False` 有什么用?默认会把中文转成 `\uXXXX` 转义,关掉后输出可读中文,但写文件时要显式 `encoding="utf-8"`。
- NaN 和 Infinity 能进 JSON 吗?标准 JSON 不允许,但 Python json 默认放行 `NaN`,严格场景传 `allow_nan=False` 强制报错。
