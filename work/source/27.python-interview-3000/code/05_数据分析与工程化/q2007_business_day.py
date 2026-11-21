"""业务日切:UTC 时间戳按东八区 0 点切业务日,决定分区归属"""

from datetime import datetime, timedelta, timezone

CST = timezone(timedelta(hours=8))
CASES = [
    "2026-11-04T15:59:00+00:00",   # 北京 23:59,业务日 11-04
    "2026-11-04T16:01:00+00:00",   # 北京 00:01,业务日 11-05
    "2026-11-04T07:00:00+00:00",   # 北京 15:00,业务日 11-04
    "2026-11-04T18:30:00+00:00",   # 北京 02:30,已属次日
]


def business_day(ts_str):
    ts = datetime.fromisoformat(ts_str).astimezone(CST)
    return ts.date(), ts.strftime("%H:%M")


if __name__ == "__main__":
    for s in CASES:
        d, hm = business_day(s)
        print(f"UTC {s}  北京 {hm} -> 业务日 {d}  分区 dt={d}")
    print("要点:分区按业务日切而不是 UTC 日,日切边界由业务定并写入口径字典;改动日切定义等于重写全部分区,必须评审;跨时区业务要一司一套业务日,禁止各管道自定义")
