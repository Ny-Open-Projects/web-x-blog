"""字段级 diff 报告: 新增 删除 变更与列级汇总"""

try:
    import pandas as pd
except ImportError:
    pd = None

OLD = {
    "o1": {"city": "北京", "amt": 100},
    "o2": {"city": "上海", "amt": 200},
    "o3": {"city": "深圳", "amt": 300},
}
NEW = {
    "o1": {"city": "北京", "amt": 120},
    "o2": {"city": "上海", "amt": 200},
    "o4": {"city": "广州", "amt": 400},
}
FIELDS = ["city", "amt"]


def diff(old, new):
    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    changed = {}
    for k in sorted(set(old) & set(new)):
        field_changes = [(f, old[k][f], new[k][f]) for f in FIELDS if old[k][f] != new[k][f]]
        if field_changes:
            changed[k] = field_changes
    return added, removed, changed


def render(added, removed, changed):
    lines = [f"新增 {len(added)} 行: {','.join(added) or '无'}",
             f"删除 {len(removed)} 行: {','.join(removed) or '无'}",
             f"变更 {len(changed)} 行:"]
    col_hits = {f: 0 for f in FIELDS}
    for k, changes in changed.items():
        detail = ", ".join(f"{f}: {o}->{n}" for f, o, n in changes)
        lines.append(f"  {k}: {detail}")
        for f, _, _ in changes:
            col_hits[f] += 1
    lines.append("列级汇总: " + ", ".join(f"{f} 变更 {c} 行" for f, c in col_hits.items()))
    return lines, col_hits


if __name__ == "__main__":
    added, removed, changed = diff(OLD, NEW)
    lines, col_hits = render(added, removed, changed)
    print("\n".join(lines))
    assert added == ["o4"] and removed == ["o3"]
    assert col_hits == {"city": 0, "amt": 1}, "只有 amt 变了 1 行"
    if pd is not None:
        df_o = pd.DataFrame([{"k": k, **v} for k, v in OLD.items()])
        df_n = pd.DataFrame([{"k": k, **v} for k, v in NEW.items()])
        m = df_o.merge(df_n, on="k", how="outer", suffixes=("_old", "_new"), indicator=True)
        print("pandas 视角: ", m["_merge"].value_counts().to_dict())
    print("要点: 行级 diff 告诉谁变了, 字段级 diff 告诉变了什么, 列级汇总是发周报和写变更说明的素材")
