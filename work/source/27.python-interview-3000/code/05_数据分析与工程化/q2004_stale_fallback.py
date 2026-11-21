"""上游延迟降级读:目标分区未就绪时回退旧分区并标注新鲜度"""

from datetime import date, timedelta

READY = {
    "2026-11-04": False,   # 今日分区上游迟到
    "2026-11-03": True,
    "2026-11-02": True,
    "2026-11-01": True,
}
ROWCOUNTS = {"2026-11-03": 122_000, "2026-11-02": 118_000, "2026-11-01": 90_000}
STALE_LIMIT = 2   # 最多回退 2 天,这是 SLA 的一部分


def choose_partition(target, ready, limit):
    d = date.fromisoformat(target)
    for back in range(limit + 1):
        cand = (d - timedelta(days=back)).isoformat()
        if ready.get(cand):
            return cand, back
    return None, limit + 1


if __name__ == "__main__":
    part, back = choose_partition("2026-11-04", READY, STALE_LIMIT)
    if part is None:
        print("降级失败:回退范围内无就绪分区,接口应报错而不是给空结果")
    else:
        tag = "最新" if back == 0 else f"降级 T-{back}"
        print(f"请求 2026-11-04 -> 实际读 {part} [{tag}],行数 {ROWCOUNTS.get(part, 0):,}")
        if back:
            print(f"响应打标 data_date={part},前端展示'数据截至 {part}'")
    print("要点:降级读必须有显式标注与最大回退天数;宁可报错也不静默给更旧的数据;回退天数与上游 SLA 联动,不是拍脑袋")
