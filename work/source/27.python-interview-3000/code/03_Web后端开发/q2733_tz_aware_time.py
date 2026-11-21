"""时区感知的时间序列化: 全链路一个标准, 偏移量随报文走(纯标准库)。"""
from datetime import datetime, timedelta, timezone

UTC = timezone.utc
CST = timezone(timedelta(hours=8))


def serialize(dt):
    """出接口一律转 UTC 并带 +00:00 偏移; naive 时间直接拒收, 不猜时区。"""
    if dt.tzinfo is None:
        raise ValueError("naive datetime 必须先补时区")
    return dt.astimezone(UTC).isoformat()


def parse(text):
    """入接口兼容 Z 与数值偏移, 统一转回 aware UTC。"""
    return datetime.fromisoformat(text.replace("Z", "+00:00")).astimezone(UTC)


created = datetime(2026, 11, 5, 0, 30, tzinfo=CST)  # 北京时间凌晨 0:30
text = serialize(created)
assert text == "2026-11-04T16:30:00+00:00", text  # 东八区 0:30 是 UTC 前一天 16:30
back = parse(text)
assert back == created and back.tzinfo is not None

utc_day = parse(text).date()
local_day = created.astimezone(CST).date()
assert utc_day != local_day, "日期字段必须声明按哪个时区取, 两个时区差一天"

try:
    serialize(datetime(2026, 11, 5, 12, 0))
except ValueError as e:
    print("naive 拒收:", e)
print("序列化:", text, "| 原始偏移 +08:00 保留在入参, 出参统一 UTC")
print("排序/比较用 aware datetime 永不出错; 展示层再转用户本地时区")
