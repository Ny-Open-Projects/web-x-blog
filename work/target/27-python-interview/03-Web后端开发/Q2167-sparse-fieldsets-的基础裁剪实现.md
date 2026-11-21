---
title: [Q2167] sparse fieldsets 的基础裁剪实现
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2167 · sparse fieldsets 的基础裁剪实现

> 难度:★★☆☆ | 标签:REST, 字段裁剪

**问**:客户端只要部分字段,sparse fieldsets 该怎么实现?未知字段怎么处理?

**答**:实现是三层漏斗:第一层是字段白名单,把内部字段(internal_score、成本类)从可选集合里排除,任何参数都拿不到;第二层解析 fields=title,views 这样的参数,与白名单求交集得到输出集合;第三层在序列化时按集合裁剪,而不是先序列化再删——裁剪要尽量下推到 SQL 的列选择,才能真正省带宽与序列化开销。未知字段有两种处理:JSON:API 口径是忽略并继续(利于演进),严格口径是 400(利于暴露拼写错误);全库统一选一种并写进文档,不传 fields 参数时返回完整公开表示。注意 fields 是裁剪不是过滤:它决定输出哪些键,不改变行集。

```python
# file: code/03_Web后端开发/q2167_sparse_fieldsets.py
"""sparse fieldsets 基础: fields 参数的序列化裁剪(纯标准库)。"""

FULL_ARTICLE = {
    "id": 1, "title": "游标分页", "body": "很长很长的正文", "author_id": 7,
    "views": 1024, "internal_score": 0.83,
}
PUBLIC_FIELDS = {"id", "title", "body", "author_id", "views"}   # 白名单先挡内部字段


def parse_fields(param, allowed):
    """fields=title,views -> 字段集合; 未知字段忽略并返回提示。"""
    if not param:
        return set(allowed), []
    requested = [f.strip() for f in param.split(",") if f.strip()]
    unknown = [f for f in requested if f not in allowed]
    chosen = set(requested) & allowed
    if not chosen:
        chosen = set(allowed)                       # 全部未知时回退完整表示
    return chosen, unknown


def serialize(row, fields):
    return {k: v for k, v in row.items() if k in fields}


param = "title,views,internal_score"
chosen, unknown = parse_fields(param, PUBLIC_FIELDS)
print("fields={}".format(param))
print("裁剪结果:", serialize(FULL_ARTICLE, chosen))
print("被忽略的未知字段:", unknown)
assert "internal_score" not in chosen and unknown == ["internal_score"]
chosen2, _ = parse_fields(None, PUBLIC_FIELDS)
print("不传 fields 时:", sorted(serialize(FULL_ARTICLE, chosen2)))
print("要点: 白名单挡内部字段, 参数决定输出子集, 未知字段的策略要全库统一并写进契约")
```

**追问**:
- 裁剪为什么强调下推到 SQL?——只省响应体不省查询,大字段(正文、BLOB)照样拖垮 DB 与序列化,字段选择要贯穿到列选择。
- fields 与 ETag 的关系?——不同 fields 组合是不同表示,缓存键或 Vary 必须包含 fields,否则会串档。
