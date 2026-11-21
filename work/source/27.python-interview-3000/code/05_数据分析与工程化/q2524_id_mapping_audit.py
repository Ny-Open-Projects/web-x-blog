"""合并后的 ID 映射与解绑审计: 可解析 可反悔 可追责"""

from datetime import datetime

MAPPING = {}      # old_id -> {"canonical": ..., "merged_at": ..., "reason": ..., "operator": ...}
AUDIT = []


def apply_merge(canonical, old_id, operator, reason, now=None):
    if old_id == canonical:
        raise ValueError("不能把主 ID 合并进自己")
    if old_id in MAPPING:
        raise ValueError(f"{old_id} 已合并过, 需先解绑")
    MAPPING[old_id] = {"canonical": canonical, "merged_at": now or datetime(2026, 3, 1, 10),
                       "reason": reason, "operator": operator}


def resolve(uid, _seen=None):
    """沿映射链解析到规范 ID, 带环检测"""
    seen = _seen or set()
    if uid in seen:
        raise ValueError(f"映射链出现环: {uid}")
    seen.add(uid)
    if uid in MAPPING:
        return resolve(MAPPING[uid]["canonical"], seen)
    return uid


def unmerge(canonical, old_id, operator, reason, now=None):
    """解绑必须写审计: 谁 何时 为什么; 主 ID 不可解绑"""
    if old_id not in MAPPING:
        raise ValueError(f"{old_id} 不存在合并记录")
    if MAPPING[old_id]["canonical"] != canonical:
        raise ValueError(f"{old_id} 的主 ID 不是 {canonical}")
    MAPPING.pop(old_id)
    AUDIT.append({"event": "UNMERGE", "old_id": old_id, "canonical": canonical,
                  "operator": operator, "reason": reason, "at": now or datetime(2026, 3, 5, 15)})


if __name__ == "__main__":
    apply_merge("u_main", "a2", "op_chen", "客服确认同手机号")
    apply_merge("u_main", "a3", "auto_job", "同名同市自动合并")
    print("合并后: resolve(a2) =", resolve("a2"), ", resolve(a3) =", resolve("a3"))
    assert resolve("a2") == "u_main" and resolve("a3") == "u_main"
    unmerge("u_main", "a3", "op_liu", "误合并, 用户申诉成立")
    print("解绑后: resolve(a3) =", resolve("a3"))
    assert resolve("a3") == "a3"
    for item in AUDIT:
        print(f"审计: {item['at']} {item['operator']} 解绑 {item['old_id']} <- {item['canonical']}, 原因: {item['reason']}")
    try:
        unmerge("u_main", "u_main", "op_x", "误操作")
    except ValueError as e:
        print("主 ID 不可解绑:", e)
    print("要点: 合并只加映射不改历史数据, 解绑走审计留痕, 报表随时可按当前映射重算")
