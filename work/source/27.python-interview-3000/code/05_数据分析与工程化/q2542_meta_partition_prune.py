"""元数据驱动的分区裁剪: 注册表求交规划, 覆盖不全必须显式放行"""

from datetime import date, timedelta

REGISTRY = [(date(2026, 2, 1) + timedelta(days=i)).isoformat() for i in range(58)]   # 02-01..03-30


def plan_partitions(query_start, query_end, registry, allow_full_scan=False):
    """规划要读的分区; 注册表覆盖不住查询区间时拒绝静默全扫"""
    qs, qe = date.fromisoformat(query_start), date.fromisoformat(query_end)
    wanted = []
    d = qs
    while d <= qe:
        wanted.append(d.isoformat())
        d += timedelta(days=1)
    missing = [w for w in wanted if w not in registry]
    if missing:
        if not allow_full_scan:
            raise ValueError(f"注册表缺少 {len(missing)} 个分区 {missing[0]}..{missing[-1]},"
                             "需补元数据或显式 allow_full_scan")
        return sorted(registry), missing
    return sorted(set(wanted) & set(registry)), []


if __name__ == "__main__":
    plan, missing = plan_partitions("2026-03-02", "2026-03-04", REGISTRY)
    print(f"查询 03-02..03-04: 计划读 {len(plan)} 个分区 {plan}, 全库 {len(REGISTRY)} 个, 省扫描 {1 - len(plan) / len(REGISTRY):.0%}")
    assert len(plan) == 3 and not missing
    try:
        plan_partitions("2026-03-25", "2026-04-02", REGISTRY)
    except ValueError as e:
        print("裁剪守卫拦截:", e)
    else:
        raise AssertionError("覆盖缺口必须被拦截")
    fallback, missing = plan_partitions("2026-03-25", "2026-04-02", REGISTRY, allow_full_scan=True)
    print(f"显式放行后: 全量 {len(fallback)} 分区兜底, 缺口 {missing[0]}..{missing[-1]} 已留痕")
    print("要点: 裁剪计划来自元数据注册表, 缺分区是元数据事故, 不许悄悄退化成全表扫")
