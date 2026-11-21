"""定时任务错峰: 泳道排布压平峰值"""

from collections import namedtuple

Job = namedtuple("Job", "name dur_min lane")
JOBS = [
    Job("dwd_a", 25, 0), Job("dwd_b", 20, 0), Job("dwd_c", 30, 0),
    Job("dws_a", 15, 1), Job("dws_b", 10, 1),
    Job("export_mail", 8, 2), Job("cleanup", 12, 2),
]
WINDOW = 90   # 凌晨维护窗口分钟数


def stagger(jobs):
    """任务进当前负载最小的泳道, 泳道内顺序排"""
    lanes, load = {}, {}
    for j in jobs:
        start = load.get(j.lane, 0)
        end = start + j.dur_min
        lanes.setdefault(j.lane, []).append((start, end, j.name))
        load[j.lane] = end
    return lanes


if __name__ == "__main__":
    lanes = stagger(JOBS)
    peak = 0
    for lane in sorted(lanes):
        print(f"泳道 {lane}: " + "  ".join(f"{name}[{s}-{e}]" for s, e, name in lanes[lane]))
        peak = max(peak, max(e for _, e, _ in lanes[lane]))
    over = [l for l, items in lanes.items() if max(e for _, e, _ in items) > WINDOW]
    print(f"总工期 {peak} 分钟, 峰值并发 <= 泳道数 {len(lanes)}, 超窗泳道: {over if over else '无'}")
    print("要点: 整点扎堆是自造故障; 泳道数硬限峰值并发; 依赖先于错峰, 窗口超限要告警而不是默默溢出")
