"""If-Range 的裁决: 只认强 ETag 或精确到秒的日期(纯标准库)。"""
import calendar
from email.utils import parsedate_to_datetime

ETAG = '"abc123"'
MTIME = calendar.timegm((2026, 11, 3, 0, 0, 0))  # Last-Modified: 2026-11-03 整秒


def if_range_decision(if_range, current_etag, current_mtime):
    """返回 (status, note)。命中返回 206 可续传, 未命中返回 200 全量。

    规则三条: 值形如引号包裹的标签时按 ETag 比, 且必须是强标签;
    值是 HTTP 日期时与 Last-Modified 整秒相等才算命中;
    解析不了的非法值一律回 200 全量, 绝不猜。
    """
    if if_range is None:
        return 206, "无条件头, 直接按 Range 切"
    value = if_range.strip()
    if value.startswith('"') or value.startswith('W/"'):
        if value.startswith("W/"):
            return 200, "弱 ETag 不允许出现在 If-Range, 回全量"
        if value == current_etag:
            return 206, "强 ETag 命中, 继续续传"
        return 200, "版本已变, 旧区间作废"
    try:
        want = parsedate_to_datetime(value).timestamp()
        return (206, "日期命中") if int(want) == int(current_mtime) else (200, "日期不符")
    except (TypeError, ValueError):
        return 200, "无法解析, 回全量"


cases = [
    (None, 206),
    ('"abc123"', 206),
    ('"other"', 200),
    ('W/"abc123"', 200),
    ("Wed, 04 Nov 2026 00:00:00 GMT", 200),
    ("garbage-input", 200),
]
for value, want in cases:
    status, note = if_range_decision(value, ETAG, MTIME)
    assert status == want, (value, status, note)
    print("%-34s -> %s  %s" % (repr(value), status, note))

status, note = if_range_decision("Tue, 03 Nov 2026 00:00:00 GMT", ETAG, MTIME)
assert status == 206, note
print("日期精确命中 ->", status, note)
