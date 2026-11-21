"""接口契约快照测试: 只锁结构与稳定字段(纯标准库)。"""
import json


def shape(value):
    """把值变成类型树: 字典递归, 列表取首个元素形状, 标量记类型名。"""
    if isinstance(value, dict):
        return {k: shape(v) for k, v in sorted(value.items())}
    if isinstance(value, list):
        return [shape(value[0])] if value else "empty[]"
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, str):
        return "str"
    return type(value).__name__


def snapshot_response(resp):
    """快照 = 结构形状 + 指定的语义稳定字段值(随机值不进快照)。"""
    snap = shape(resp)
    snap["stable.id"] = resp.get("id")
    snap["stable.status"] = resp.get("status")
    return snap


ORDER_V1 = {"id": "ord_1", "status": "paid", "amount": 99.0,
            "buyer": {"uid": "u9", "nickname": "rand-3482"}}

snapshot = snapshot_response(ORDER_V1)
print("快照:", json.dumps(snapshot, ensure_ascii=False, sort_keys=True))
print("回归一致:", snapshot_response(ORDER_V1) == snapshot)

ORDER_V2 = dict(ORDER_V1, coupon=None)           # 新版本加了可选字段
diff = set(snapshot_response(ORDER_V2)) - set(snapshot)
print("新增字段触发快照 diff:", sorted(diff), "-> 人工确认后更新快照")
