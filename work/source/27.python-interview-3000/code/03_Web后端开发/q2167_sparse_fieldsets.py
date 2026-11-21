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
