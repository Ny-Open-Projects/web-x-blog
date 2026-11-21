---
title: [Q1617] 问题详情的 type 目录与扩展演进
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1617 · 问题详情的 type 目录与扩展演进

> 难度:★★★☆ | 标签:HTTP, 接口演进

**问**:problem+json 的 type URI 和扩展字段,在多版本演进中怎么管理才不会坑到老调用方?

**答**:把每种错误注册成稳定的 type URI 目录(如 `https://api.example.com/problems/insufficient-funds`),code review 时新错误类型必须先进目录再上线,防止散落的魔法字符串。扩展成员遵守只增不改不删:老客户端按字段名读取,新增字段对它们不可见,所以加字段是兼容变更,改语义或删除都是破坏。title 与 type 绑定保持不变,`detail` 才是放动态信息的地方。未注册的 kind 直接在构造层抛错,让漂移在开发期暴露而不是线上。

```python
# file: code/03_Web后端开发/q1617_problem_ext.py
"""RFC 7807 的 type 目录注册与扩展成员演进(纯标准库)。"""
import json

# 错误目录: type URI 是机器可读的"错误种类", 一旦发布语义就要稳定
CATALOG = {
    "insufficient-funds": "https://api.example.com/problems/insufficient-funds",
    "invalid-param": "https://api.example.com/problems/invalid-param",
}


def problem(kind, status, title, detail=None, **ext):
    uri = CATALOG.get(kind)
    if uri is None:
        raise ValueError(f"未注册的错误类型: {kind}")     # 由调用处捕获
    body = {"type": uri, "title": title, "status": status}
    if detail:
        body["detail"] = detail
    body.update(ext)
    return body


# 扩展成员只能增不能删不能改语义: 老客户端按字段名读, 新增字段对它们不可见
v1 = problem("insufficient-funds", 422, "余额不足", detail="需要 120 元", balance=80.0)
v2 = problem("insufficient-funds", 422, "余额不足", detail="需要 120 元",
             balance=80.0, required=120.0, currency="CNY")
print("v1:", json.dumps(v1, ensure_ascii=False))
print("v2:", json.dumps(v2, ensure_ascii=False))
old_clients = {k: v2[k] for k in v1 if k in v2}
print("老客户端可见字段不变:", old_clients == v1)

try:
    problem("unknown-kind", 500, "x")
except ValueError as e:
    print("未注册类型被拦下:", e)
```

**追问**:
- type URI 会被客户端硬编码吗?——会,所以 URI 一旦发布只加版本不迁移,旧 URI 重定向到新文档。
- 扩展字段名冲突怎么办?——加业务前缀或命名空间,注册表里同时登记字段含义与版本。
