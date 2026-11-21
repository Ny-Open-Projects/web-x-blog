"""死信区:坏数据隔离、带原因归档与修复后回放"""

import json

RECORDS = [
    '{"row_id": "r1", "amount": "100"}',
    '{"row_id": "r2", "amount": "abc"}',        # 类型坏
    'not-json-at-all',                          # 结构坏
    '{"row_id": "", "amount": "30"}',           # 业务校验失败
    '{"row_id": "r4", "amount": "88"}',
]

DEAD_LETTER = []


def validate(payload):
    if not isinstance(payload, dict):
        return "结构非法: 不是 JSON 对象"
    if not payload.get("row_id"):
        return "业务非法: row_id 为空"
    try:
        float(payload["amount"])
    except (KeyError, TypeError, ValueError):
        return "类型非法: amount 不可解析"
    return None


def process(records):
    good = []
    for raw in records:
        try:
            payload = json.loads(raw) if raw.startswith("{") else None
        except json.JSONDecodeError:
            payload = None
        reason = validate(payload)
        if reason is None:
            good.append(payload)
        else:
            DEAD_LETTER.append({"reason": reason, "raw": raw})
    return good


def replay(dead_items, fixer):
    """修复函数处理原始载荷后再次入队,成功即从死信移除"""
    still_dead = []
    for item in dead_items:
        fixed = fixer(item["raw"])
        reason = validate(fixed)
        if reason is None:
            process([json.dumps(fixed)])
        else:
            still_dead.append(item)
    return still_dead


if __name__ == "__main__":
    good = process(RECORDS)
    print("正常入库:", [g["row_id"] for g in good])
    for d in DEAD_LETTER:
        print("死信:", d["reason"], "|", d["raw"][:40])
    print("\n修复后回放:", len(replay(
        [d for d in DEAD_LETTER if "amount" in d["raw"]],
        lambda raw: {"row_id": "r2", "amount": "0"})), "条仍滞留")
    print("要点:死信必须带原因与原始载荷,且要有回放通道和滞留量监控")
