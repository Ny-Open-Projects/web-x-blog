"""乱序到达的水位修正: 迟到触发更正记录与桶重算"""

from datetime import datetime, timedelta

EVENTS = [
    # 到达顺序: 事件时间, 值
    ("10:02", 10), ("10:07", 20), ("10:14", 30), ("10:19", 40),
    ("10:24", 50), ("10:29", 60),
    ("10:06", 70),      # 迟到: 属于已关闭的 10:00 桶
    ("10:31", 80),
    ("10:22", 90),      # 迟到: 属于已关闭的 10:20 桶
]
BUCKET = timedelta(minutes=10)
EPOCH = datetime(1900, 1, 1)
FMT = "%H:%M"


def bucket_start(t):
    return EPOCH + BUCKET * ((t - EPOCH) // BUCKET)


if __name__ == "__main__":
    buckets, corrections, log, max_seen = {}, [], [], None
    for ts, val in EVENTS:
        t = datetime.strptime(ts, FMT)
        b = bucket_start(t)
        if max_seen is not None and b < bucket_start(max_seen):
            corrections.append((b, val))
            buckets[b] = buckets.get(b, 0) + val
            log.append(f"更正: {ts} 值 {val} 属已关闭桶 {b:%H:%M}, 发更正记录并重算")
        else:
            buckets[b] = buckets.get(b, 0) + val
            log.append(f"并入: {ts} 值 {val} -> 桶 {b:%H:%M}")
        max_seen = t if max_seen is None else max(max_seen, t)
    for line in log:
        print(" ", line)
    print("更正记录:", [(f"{b:%H:%M}", v) for b, v in corrections])
    for b in sorted(buckets):
        print(f"最终桶 {b:%H:%M} -> {buckets[b]}")
    print("要点: 更正不改历史输出而是发增量记录; 更正率突变要回头调水位延迟")
