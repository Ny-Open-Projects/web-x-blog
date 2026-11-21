"""数据冻结快照读:报表按 as_of 读当时版本,回刷不影响已发布数字"""

SNAPSHOTS = {
    "dws_gmv_day": [
        # (快照版本日, 该版本下的数据)
        ("2026-11-01", {"11-01": 1210, "10-31": 980}),
        ("2026-11-02", {"11-01": 1235, "11-02": 1102, "10-31": 980}),
        # 11-03 版本里 11-01 被回刷修正
        ("2026-11-03", {"11-01": 1301, "11-02": 1140, "11-03": 1188, "10-31": 995}),
    ],
}


def read_as_of(table, as_of, dt):
    versions = [v for v in SNAPSHOTS[table] if v[0] <= as_of]
    if not versions:
        raise KeyError(f"{table} 在 {as_of} 之前无快照")
    version_day, data = versions[-1]
    return data.get(dt), version_day


if __name__ == "__main__":
    for as_of in ("2026-11-02", "2026-11-03"):
        val, snap = read_as_of("dws_gmv_day", as_of, "11-01")
        print(f"as_of={as_of} 读 11-01 GMV = {val}(来自快照 {snap})")
    try:
        read_as_of("dws_gmv_day", "2026-10-31", "11-01")
    except KeyError as e:
        print("故意越界读:", e)
    print("要点:对账与复盘必须走 as_of 快照读,当期看板读最新版,两者要能互相切换;快照按报表等级定保留期;没有版本化,回刷会让昨天的汇报永远对不上")
