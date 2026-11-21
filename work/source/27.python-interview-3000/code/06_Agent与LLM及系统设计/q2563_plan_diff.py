"""Q2563 Agent 计划的版本对比:步骤增删改与顺序变化四类归并。

计划被重写后,先用 id 对齐新旧两版,再按 增/删/改/序 四类归并差异,
产出机器可读的 diff,供审批、审计与回归使用。
"""


def index_plan(plan):
    return {step["id"]: step for step in plan}


def diff_plans(old, new):
    oi, ni = index_plan(old), index_plan(new)
    added = sorted(set(ni) - set(oi))
    removed = sorted(set(oi) - set(ni))
    changed = sorted(sid for sid in set(oi) & set(ni) if oi[sid] != ni[sid])
    seq_old = [s["id"] for s in old if s["id"] in ni]
    seq_new = [s["id"] for s in new if s["id"] in oi]
    return {"added": added, "removed": removed, "changed": changed,
            "reordered": seq_old != seq_new}


def main():
    old = [
        {"id": "s1", "tool": "search", "kw": "财报"},
        {"id": "s2", "tool": "extract", "src": "s1"},
        {"id": "s3", "tool": "summary", "src": "s2"},
    ]
    new = [
        {"id": "s2b", "tool": "crawl", "url": "x"},    # 新增
        {"id": "s3", "tool": "summary", "src": "s2"},  # 保留但挪到 s1 前
        {"id": "s1", "tool": "search", "kw": "年报"},  # 参数漂移
    ]
    d = diff_plans(old, new)
    assert d["added"] == ["s2b"], d
    assert d["removed"] == ["s2"], d
    assert d["changed"] == ["s1"], d
    assert d["reordered"] is True, d
    print("新增:", d["added"])
    print("删除:", d["removed"])
    print("参数变更:", d["changed"])
    print("顺序有变化:", d["reordered"])


if __name__ == "__main__":
    main()
