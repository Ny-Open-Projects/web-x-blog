
def reconcile(src, dst, keys, value_cols):
    src_map = {tuple(r[k] for k in keys): r for r in src}
    dst_map = {tuple(r[k] for k in keys): r for r in dst}
    only_src = sorted(set(src_map) - set(dst_map))
    only_dst = sorted(set(dst_map) - set(src_map))
    diffs = []
    for k in set(src_map) & set(dst_map):
        for c in value_cols:
            if src_map[k][c] != dst_map[k][c]:
                diffs.append({"key": k, "col": c, "src": src_map[k][c], "dst": dst_map[k][c]})
    return {"only_src": only_src, "only_dst": only_dst, "value_diffs": diffs}

src = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}, {"id": 3, "amount": 300}]
dst = [{"id": 1, "amount": 100}, {"id": 2, "amount": 250}]
report = reconcile(src, dst, ["id"], ["amount"])
print("仅源表:", report["only_src"])
print("仅目标表:", report["only_dst"])
print("值差异:", report["value_diffs"])
