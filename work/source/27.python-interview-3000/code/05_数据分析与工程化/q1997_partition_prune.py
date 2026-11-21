"""分区裁剪:带分区条件的查询只扫命中分区,模拟扫描量对比"""

PARTITIONS = {
    "dt=2026-10-30": 120_000, "dt=2026-10-31": 135_000,
    "dt=2026-11-01": 128_000, "dt=2026-11-02": 122_000,
    "dt=2026-11-03": 130_000, "dt=2026-11-04": 126_000,
}


def plan_scan(partitions, dt_filter=None):
    """dt_filter=None 全表扫描;给日期列表则只扫命中分区"""
    hit = {p: n for p, n in partitions.items()
           if dt_filter is None or any(p.endswith(d) for d in dt_filter)}
    return hit


if __name__ == "__main__":
    full = plan_scan(PARTITIONS)
    pruned = plan_scan(PARTITIONS, ["2026-11-03", "2026-11-04"])
    full_rows, pruned_rows = sum(full.values()), sum(pruned.values())
    print(f"全表扫描: {len(full)} 分区 {full_rows:,} 行")
    print(f"裁剪后:   {len(pruned)} 分区 {pruned_rows:,} 行  扫描量降至 {pruned_rows / full_rows:.0%}")
    for p in sorted(pruned):
        print(f"  命中 {p}: {pruned[p]:,} 行")
    print("要点:裁剪发生在元数据层,不读数据就省了钱;查询必须带分区键,分区键被函数包裹(如 date_format(dt))会让裁剪失效,这是慢查询排查第一现场")
