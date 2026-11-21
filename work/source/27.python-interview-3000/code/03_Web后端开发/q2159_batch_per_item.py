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
