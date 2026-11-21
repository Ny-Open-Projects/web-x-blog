---
title: [Q2159] 批量端点的 per-item 结果体设计
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2159 · 批量端点的 per-item 结果体设计

> 难度:★★★☆ | 标签:REST, 批量

**问**:批量创建接口里一半成功一半失败,响应体怎么设计才能让调用方准确对账?

**答**:核心是用 index 对齐请求与结果:响应里的每个条目带 index、自身 status、成功时带 resource、失败时带 error,整体状态码只表达"批次受理成功"(200),条目级成败由各自 status 表达。这样调用方可以按 index 精确回查,不需要靠顺序猜。响应里再给一个 summary(total/created/failed)方便日志与监控,但契约的主体永远是 items 数组。三条纪律:items 的顺序必须与请求顺序一致;单项失败不中断批次(除非是原子模式);单项错误要带机器可读的错误码与字段定位,而不是一句 message。

```python
# file: code/03_Web后端开发/q2159_batch_per_item.py
"""批量端点的 per-item 结果体: 每项独立状态码与错误定位(纯标准库)。"""


def create_one(item, existing_ids):
    """模拟单条创建: 校验加查重。"""
    if "name" not in item:
        return 422, None, {"error": "validation_failed", "field": "name"}
    if item["name"] in existing_ids:
        return 409, None, {"error": "duplicate", "field": "name"}
    return 201, {"id": "id-" + item["name"], "name": item["name"]}, None


def process_batch(payload, existing_ids):
    """整体 200 加 per-item 结果; index 保留请求顺序, 单项失败不中断批次。"""
    results = []
    for index, item in enumerate(payload.get("items", [])):
        status, data, err = create_one(item, existing_ids)
        entry = {"index": index, "status": status}
        if data:
            entry["resource"] = data
            existing_ids.add(item["name"])          # 批内创建的也会被后续项查重
        if err:
            entry["error"] = err
        results.append(entry)
    created = sum(1 for r in results if r["status"] == 201)
    summary = {"total": len(results), "created": created, "failed": len(results) - created}
    return 200, {"items": results, "summary": summary}


existing = {"boom"}
code, body = process_batch(
    {"items": [{"name": "alpha"}, {"name": "boom"}, {"bad": 1}, {"name": "alpha"}]},
    existing)
print("HTTP", code)
for entry in body["items"]:
    print("  index {} status {} {}".format(entry["index"], entry["status"],
                                           entry.get("error") or entry["resource"]))
print("summary:", body["summary"])
assert body["summary"] == {"total": 4, "created": 1, "failed": 3}   # boom 预存冲突, alpha 批内重复
print("要点: index 对齐请求与结果, 单项失败用 4xx 表达原因, 整体状态码只表达批次受理成功")
```

**追问**:
- 整体状态码用 207 Multi-Status 行不行?——可以但语义负担重,207 要求每个条目都是完整状态行,实践上 200 加条目级 status 更易消费。
- 批内第二项与第一项重名算冲突吗?——算,处理过程中要可见前项的写入,本题用 existing_ids 边处理边登记来模拟。
