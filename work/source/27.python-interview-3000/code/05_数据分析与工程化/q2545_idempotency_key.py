"""任务幂等键的生成规范: 规范化序列化 + 范围隔离 + 语义日期"""

import hashlib
import json


def canonical_json(obj):
    """规范化序列化: 键排序 紧凑分隔符; 列表保持原序, 顺序即语义"""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def idempotency_key(scope, target, logical_date, params):
    payload = {
        "scope": scope,
        "target": target,
        "logical_date": logical_date,
        "params": params,
    }
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


if __name__ == "__main__":
    k1 = idempotency_key("etl", "dwd_orders", "2026-03-01", {"window": 60, "dedup": True})
    k2 = idempotency_key("etl", "dwd_orders", "2026-03-01", {"dedup": True, "window": 60})
    print(f"字典键序不同: {k1[:12]} == {k2[:12]}")
    assert k1 == k2, "同一语义参数必须得到同一键"
    k3 = idempotency_key("etl", "dwd_orders", "2026-03-02", {"window": 60, "dedup": True})
    k4 = idempotency_key("backfill", "dwd_orders", "2026-03-01", {"window": 60, "dedup": True})
    k5 = idempotency_key("etl", "dwd_orders", "2026-03-01", {"window": 30, "dedup": True})
    assert len({k1, k3, k4, k5}) == 4, "日期 范围 参数任一变化都要换键"
    print(f"逻辑日期/范围/参数任一变化 -> 新键: {len({k1, k3, k4, k5})} 个互不相同")
    assert idempotency_key("etl", "t", "d", {"tags": ["a", "b"]}) != \
           idempotency_key("etl", "t", "d", {"tags": ["b", "a"]})
    print("要点: 幂等键四要素 scope+目标+逻辑日期+参数哈希, 规范化序列化保证不同机器算出同一个键")
