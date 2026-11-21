---
title: [Q2427] 304 Not Modified 的条件组合裁决
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2427 · 304 Not Modified 的条件组合裁决

> 难度:★★★☆ | 标签:HTTP, 条件请求, 缓存

**问**:If-None-Match、If-Modified-Since、If-Match 同时出现时,304 与 412 到底怎么裁决?

**答**:RFC 7232 给了固定顺序:If-Match 先行,不匹配则对非安全方法回 412;接着 If-Unmodified-Since,资源在其后修改过回 412;然后 If-None-Match,命中时 GET/HEAD 回 304、其他方法回 412;只有 If-None-Match 不存在时才轮到 If-Modified-Since。两个关键细节:If-None-Match 出现时 If-Modified-Since 整体失效,不存在"两个都看一下"的混合逻辑;ETag 的弱比较忽略 W/ 前缀,强比较(If-Match)必须逐字节一致。304 响应不能带响应体,但应该回填当前的 ETag、Cache-Control 与 Vary,让客户端缓存的元数据跟着更新。If-Modified-Since 的秒级精度是它不如 ETag 可靠的根本原因,同秒内两次修改会漏检。

```python
# file: code/03_Web后端开发/q2427_conditional_304.py
"""条件请求头的组合裁决: 304 与 412 的优先级(纯标准库)。"""
import email.utils


def parse_etag_list(value):
    """If-None-Match 的值可以是逗号分隔列表, 也可以是通配符 *。"""
    value = value.strip()
    if value == "*":
        return "*"
    return [item.strip() for item in value.split(",")]


def etag_match(candidate, current, weak_ok=True):
    """弱比较忽略 W/ 前缀, 用于 If-None-Match; 强比较要求逐字节一致。"""
    def strip(s):
        return s[2:] if s.startswith("W/") else s
    if weak_ok:
        return strip(candidate) == strip(current)
    return candidate == current


def evaluate(method, resource, headers):
    """按 RFC 7232 固定顺序裁决, 返回 (status, 理由)。"""
    if "If-Match" in headers:
        listed = parse_etag_list(headers["If-Match"])
        ok = listed == "*" or any(
            etag_match(c, resource["etag"], weak_ok=False) for c in listed)
        if not ok:
            return 412, "If-Match 不匹配, 资源已被他人修改"
    if "If-Unmodified-Since" in headers:
        since = email.utils.parsedate_to_datetime(headers["If-Unmodified-Since"]).timestamp()
        if resource["mtime"] > since:
            return 412, "资源在 If-Unmodified-Since 之后被修改"
    if "If-None-Match" in headers:
        listed = parse_etag_list(headers["If-None-Match"])
        hit = listed == "*" or any(
            etag_match(c, resource["etag"], weak_ok=True) for c in listed)
        if hit and method in ("GET", "HEAD"):
            return 304, "ETag 命中, 缓存副本仍然有效"
        if hit:
            return 412, "非安全方法不允许覆盖已存在的表示"
    elif "If-Modified-Since" in headers and method in ("GET", "HEAD"):
        since = email.utils.parsedate_to_datetime(headers["If-Modified-Since"]).timestamp()
        if resource["mtime"] <= since:
            return 304, "修改时间未变, 缓存副本仍然有效"
    return 200, "条件全部通过, 返回新表示"


res = {"etag": '"v3"', "mtime": 1735689600.0}
httpdate = email.utils.formatdate(res["mtime"], usegmt=True)
cases = [
    ("GET", {"If-None-Match": 'W/"v3"'}, 304),
    ("GET", {"If-None-Match": '"v2", "v3"'}, 304),
    ("GET", {"If-None-Match": '"v9"', "If-Modified-Since": httpdate}, 200),
    ("GET", {"If-Modified-Since": httpdate}, 304),
    ("PUT", {"If-Match": '"v2"'}, 412),
    ("PUT", {"If-Match": '"v3"'}, 200),
]
for method, headers, expect in cases:
    status, why = evaluate(method, res, headers)
    print("{} {:36s} -> {} {}".format(method, str(headers), status, why))
    assert status == expect, (method, headers, status, expect)
print("要点: 裁决顺序 If-Match -> If-Unmodified-Since -> If-None-Match -> If-Modified-Since, "
      "INM 出现时 IMS 整体失效, 304 永不带响应体")
```

**追问**:
- 为什么 If-None-Match 命中时 PUT 是 412 而不是 304?——304 语义是"你缓存的那份还能用",写请求的答案是"资源已被人改过,你的条件假设不成立"。
- If-Match 在并发编辑里扮演什么角色?——它是乐观锁的 HTTP 表达,提交时带上读到的 ETag,被别人改过就拒绝。
