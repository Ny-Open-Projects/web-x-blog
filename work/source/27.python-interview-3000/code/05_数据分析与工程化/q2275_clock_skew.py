"""时钟回拨: 设备时钟偏移的检测与事件时间修正"""

from datetime import datetime, timedelta

SERVER_NOW = datetime(2026, 3, 1, 12, 0, 0)
FMT = "%Y-%m-%d %H:%M:%S"
AHEAD_LIMIT = timedelta(minutes=5)     # 事件时间超前 5 分钟视为时钟偏快
BEHIND_LIMIT = timedelta(hours=24)     # 落后超 1 天视为时钟不可信


def correct(raw_event_time, server_now):
    skew = raw_event_time - server_now
    if skew > AHEAD_LIMIT:
        return server_now, f"时钟偏快 {skew.total_seconds() / 60:.0f} 分钟, 夹到服务器时间"
    if skew < -BEHIND_LIMIT:
        return server_now - timedelta(minutes=1), "时钟偏慢, 事件时间不可信, 用到达时间近似并打标"
    return raw_event_time, "正常"


if __name__ == "__main__":
    stream = [
        "2026-03-01 11:59:30",
        "2026-03-01 12:40:00",
        "2026-02-26 08:00:00",
    ]
    for raw in stream:
        t = datetime.strptime(raw, FMT)
        fixed, note = correct(t, SERVER_NOW)
        print(f"原始 {raw} -> 修正 {fixed:%H:%M:%S} ({note})")
    print("要点: 修正列与原始列共存, 永不覆盖原始值; 反复偏移的设备清单化推动校时; 补传流量带显式标记")
