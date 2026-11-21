"""快照更新治理: diff 分级与合并门禁(纯标准库)。"""


def classify_diff(old, new):
    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    changed = sorted(k for k in set(old) & set(new) if old[k] != new[k])
    # 分级: 新增可选输出是兼容变更; 删除或类型变化是破坏性变更
    breaking = removed + changed
    return {"added": added, "removed": removed, "changed": changed, "breaking": breaking}


def merge_gate(diff, approved_breaking=False):
    if not diff["breaking"]:
        return "自动通过", "纯新增, 快照随 PR 更新"
    if approved_breaking:
        return "人工放行", "破坏性变更已评审: " + ", ".join(diff["breaking"])
    return "阻断合并", "请评审破坏性变更并在提交说明中标注 BREAKING"


old_snap = {"buyer": "dict", "id": "str", "status": "str", "stable.id": "ord_1"}

new_snap = dict(old_snap, coupon="NoneType")                # 兼容新增
diff_ok = classify_diff(old_snap, new_snap)
print("新增场景:", diff_ok)
print("门禁:", merge_gate(diff_ok))

removed_snap = {k: v for k, v in old_snap.items() if k != "buyer"}   # 删字段
diff_bad = classify_diff(old_snap, removed_snap)
print("删除场景门禁:", merge_gate(diff_bad))
print("评审后放行:", merge_gate(diff_bad, approved_breaking=True))
