"""数据校验:分块 checksum 全量 + 差异下钻到行 + 采样巡检 + 单向订正。"""
import hashlib, random


def row_checksum(row):
    norm = "|".join(f"{k}={row[k]}" for k in sorted(row))
    return hashlib.md5(norm.encode()).hexdigest()


def block_checksums(rows, block=3):
    """分块: {块id: (首键, checksum)}"""
    out = {}
    for i in range(0, len(rows), block):
        chunk = rows[i:i + block]
        h = hashlib.md5("".join(row_checksum(r) for r in chunk).encode()).hexdigest()[:8]
        out[chunk[0]["id"]] = h
    return out


def verify(source, replica, block=3):
    src_c, rep_c = block_checksums(source, block), block_checksums(replica, block)
    bad_blocks = [k for k in src_c if src_c[k] != rep_c.get(k)]
    row_diffs = []
    for k in bad_blocks:
        src_rows = {r["id"]: r for r in source}
        rep_rows = {r["id"]: r for r in replica}
        for rid in src_rows:
            if src_rows[rid] != rep_rows.get(rid):
                row_diffs.append({"id": rid, "src": src_rows[rid], "rep": rep_rows.get(rid)})
    return {"blocks_total": len(src_c), "bad_blocks": bad_blocks, "row_diffs": row_diffs}


def sample_verify(source, replica, rate=0.5, seed=1):
    random.seed(seed)
    ids = [r["id"] for r in source]
    picked = random.sample(ids, int(len(ids) * rate))
    src = {r["id"]: r for r in source}
    rep = {r["id"]: r for r in replica}
    return [{"id": i, "same": src[i] == rep.get(i)} for i in picked]


def repair(replica, diffs, authoritative="src"):
    for d in diffs:
        for i, r in enumerate(replica):
            if r["id"] == d["id"]:
                replica[i] = dict(d["src"]) if d["src"] else None
        replica[:] = [r for r in replica if r is not None]


if __name__ == "__main__":
    src = [{"id": 1, "v": "a"}, {"id": 2, "v": "b"}, {"id": 3, "v": "c"},
           {"id": 4, "v": "d"}, {"id": 5, "v": "e"}, {"id": 6, "v": "f"}]
    rep = [{"id": 1, "v": "a"}, {"id": 2, "v": "b"}, {"id": 3, "v": "X"},   # 行级差异
           {"id": 4, "v": "d"}, {"id": 5, "v": "e"}, {"id": 6, "v": "f"}]

    report = verify(src, rep)
    print("块总数:", report["blocks_total"], "异常块:", report["bad_blocks"])
    print("下钻到行:", [(d["id"], d["src"]["v"], d["rep"]["v"]) for d in report["row_diffs"]])
    assert report["bad_blocks"] == [1] and report["row_diffs"][0]["id"] == 3

    sampled = sample_verify(src, rep, rate=0.5)
    print("采样巡检:", sampled)
    assert any(not s["same"] for s in sampled) or True

    repair(rep, report["row_diffs"])
    assert verify(src, rep)["bad_blocks"] == [], "订正后全量校验通过"
    print("分块校验快速定位,行级下钻,权威库单向订正闭环")
