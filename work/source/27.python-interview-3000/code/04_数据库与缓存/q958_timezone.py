"""UTC 存储 + 按用户时区展示的最小闭环"""
from datetime import datetime, timezone, timedelta

def now_utc() -> datetime:
    return datetime.now(timezone.utc)             # 全库统一时区

def to_user_tz(dt: datetime, offset_hours: int) -> str:
    return dt.astimezone(timezone(timedelta(hours=offset_hours))).strftime(
        "%Y-%m-%d %H:%M")

if __name__ == "__main__":
    ts = now_utc()
    print("库存 UTC:", ts.isoformat())
    print("东京用户(+9):", to_user_tz(ts, 9))
    print("北京用户(+8):", to_user_tz(ts, 8))

    try:
        ts - datetime.now()                        # naive 与 aware 相减
    except TypeError as e:
        print("防线生效:", e)

    legacy = datetime(2026, 11, 1, 12, 0)          # 老数据无时区
    print("旧数据按 UTC 补齐:", legacy.replace(tzinfo=timezone.utc).isoformat())
