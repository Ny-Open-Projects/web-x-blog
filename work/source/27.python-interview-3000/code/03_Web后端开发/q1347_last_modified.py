"""Last-Modified 协商:秒级精度对齐后再比较(纯标准库)。"""
from datetime import datetime, timezone
from email.utils import format_datetime, parsedate_to_datetime


def not_modified_since(last_modified, if_modified_since):
    """last_modified 为 aware datetime;头缺失返回 False 表示要发全量。"""
    if not if_modified_since:
        return False
    client_seen = parsedate_to_datetime(if_modified_since)
    lm = last_modified.replace(microsecond=0)  # 截断到秒,与 HTTP 日期同精度
    return lm <= client_seen


last_modified = datetime(2026, 10, 31, 12, 0, 0, 500000, tzinfo=timezone.utc)
header = format_datetime(last_modified.replace(microsecond=0), usegmt=True)
print("Last-Modified 头:", header)
print("客户端缓存与当前一致 ->", not_modified_since(last_modified, header))
print("资源在客户端缓存之后更新过 ->", not_modified_since(last_modified, "Sat, 01 Oct 2026 00:00:00 GMT"))
print("缺头 ->", not_modified_since(last_modified, None))
