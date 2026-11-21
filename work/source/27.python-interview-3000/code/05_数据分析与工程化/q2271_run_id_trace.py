"""管道 run_id 贯穿: 从混合日志还原一次数据生产的完整时间线"""

from collections import defaultdict

LOGS = [
    ("d1 09:00:05", "extract", "run_20260301", "START rows=0"),
    ("d1 09:00:40", "extract", "run_20260301", "DONE rows=182000"),
    ("d1 09:01:02", "extract", "run_20260228", "RETRY rows=0"),   # 别的运行, 混在同一日志
    ("d1 09:02:00", "dwd_build", "run_20260301", "START"),
    ("d1 09:31:00", "dwd_build", "run_20260301", "DONE rows=181000"),
    ("d1 09:31:30", "quality_check", "run_20260301", "FAIL rows_mismatch=1000"),
    ("d1 09:35:00", "dwd_build", "run_20260301", "RERUN rows=182000"),
]


def timeline(logs, run_id):
    events = defaultdict(list)
    for ts, task, rid, msg in logs:
        if rid == run_id:
            events[task].append((ts, msg))
    return events


if __name__ == "__main__":
    events = timeline(LOGS, "run_20260301")
    flat = sorted(((ts, task, msg) for task, evs in events.items() for ts, msg in evs),
                  key=lambda x: x[0])
    for ts, task, msg in flat:
        print(f"{ts} [{task:<13}] {msg}")
    starts = sum(1 for _, _, m in flat if m.startswith("START"))
    print(f"该 run 共 {len(flat)} 条事件, START 出现 {starts} 次 -> dwd_build 重跑 1 次, 起因是行数校验不平")
    print("要点: run_id 调度器单点生成全程透传; 统一动词 START DONE FAIL RERUN 便于聚合")
