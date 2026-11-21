---
title: [Q2704] If-Range 的裁决:强标签与整秒日期
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2704 · If-Range 的裁决:强标签与整秒日期

> 难度:★★★☆ | 标签:HTTP 协议, Range, 缓存

**问**:断点续传中途文件被更新过,客户端的 Range 请求怎么避免拼出混合版本?

**答**:If-Range 就是为此设计的:客户端续传时把上次响应的 ETag 或 Last-Modified 放进 If-Range,服务端先裁决再决定 206 还是退回 200 全量。规则三条:值是引号包裹的标签时按 ETag 强比较,弱标签 W/ 不允许出现在 If-Range,直接回 200;值是 HTTP 日期时与 Last-Modified 整秒相等才算命中——秒级精度意味着秒内两次变更无法区分,有秒内变更风险的资源必须用 ETag;解析不了的值一律回 200 全量,绝不猜。没有 If-Range 的裸 Range 在文件变更后会静默拼出前半旧后半新的混合文件,这种损坏往往要到文件被使用时才暴露。

```python
# file: code/03_Web后端开发/q2704_if_range.py
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
```

**追问**:
- If-Range 命中后还要不要看 If-None-Match?——两者语义独立:If-Range 只裁决区间是否仍匹配,缓存协商由 If-None-Match 单独处理,可以并存。
- If-Range 给了但请求没带 Range 头呢?——If-Range 被忽略,按普通 GET 处理,它只对 Range 请求有意义。
