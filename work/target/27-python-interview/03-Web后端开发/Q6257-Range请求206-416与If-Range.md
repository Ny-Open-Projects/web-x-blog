---
title: "[Q6257] Range 请求的服务端取舍：206/416、If-Range 与多段 Range 该不该支持"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6257 · Range 请求的服务端取舍：206/416、If-Range 与多段 Range 该不该支持

难度：P6 ｜ 标签：HTTP Range、206、416、Content-Range、If-Range、断点续传、多段 Range、ETag

**问**：给静态文件服务加断点续传，`Range: bytes=0-99` 返回 206 正常，但 `Range: bytes=99999-`（超出文件大小）返回了 200 全量，播放器一直重下；另一条请求带 `If-Range`，文件其实已经变了，服务端仍然返回了旧文件的片段，客户端拼出一个损坏的文件。Range 的边界语义是什么？416 该怎么写？`If-Range` 什么时候必须忽略 Range？多段 Range 要不要支持？

**答**：

- **结论**：单段 Range 的处理是：解析 `bytes=start-end`（`end` 省略表示到文件尾，`start-end` 都缺省时按后缀处理 `bytes=-N`），把 `end` **截断到 `size-1`**；如果 `start >= size` 或 `start > end`（不可满足），返回 **416**，并带 `Content-Range: bytes */<size>` 告诉客户端真实大小；可满足时返回 **206**，必须带 `Content-Range: bytes start-end/size` 和正确的 `Content-Length`。`If-Range` 是"条件 Range"：只有它的值（强 ETag 或 HTTP-date）与当前资源**匹配**时才处理 Range，否则忽略 Range 返回 **200 全量**——这样客户端不会把"旧文件的片段"拼到"新文件"上。弱 ETag（`W/"..."`）不能用于 `If-Range`（规范要求强校验），遇到弱 ETag 应按不匹配处理。多段 Range（`bytes=0-0,2-2`）要返回 `multipart/byteranges`，实现复杂、收益低，多数服务端选择"只服务第一段"或"直接 200 全量"，但必须在文档里写清楚。

- **取舍**：a) 支持单段 Range：断点续传、视频拖动、大文件下载的核心，成本低，应该做；b) 多段 Range：客户端很少用（浏览器通常发单段），实现要生成 boundary、每段一个 part 头，容易出 bug；除非明确有客户端依赖，否则"只取第一段"是合理取舍；c) 416 的语义要精确：不是"文件不存在"，而是"范围不可满足"，必须带 `Content-Range: bytes */size`，否则客户端不知道该怎么重试；d) `If-Range` 必须用**强** ETag 或 Last-Modified：用弱 ETag 会让"内容变了但 ETag 前缀相同"的场景拼出坏文件；e) 206 响应不要被 CDN 当完整对象缓存，`Vary`/`Cache-Control` 要配好，避免"半个文件"污染缓存。

- **实战**：事故形态是"视频播放器无限重下"——服务端对 `bytes=99999-` 返回 200 全量，播放器认为"服务端不支持 Range"，每次 seek 都从头下；另一个事故是"更新安装包后用户装出坏包"——CDN 缓存了旧文件的 206 片段，客户端带旧 ETag 的 `If-Range` 请求新文件，服务端没校验 `If-Range` 直接返回新文件的同偏移片段，新旧字节拼在一起校验失败。修复：①严格实现 416 + `Content-Range: bytes */size`；②`If-Range` 与当前强 ETag 比较，不匹配就 200；③ETag 用内容哈希或"mtime-size-inode"，不要用弱 ETag；④CDN 对 206 单独设缓存策略，或让回源带 `Cache-Control: no-transform`。

```python
# Range 服务端: 单段 206、不可满足 416、If-Range 强校验、多段取舍
ETAG = '"sha256-abc123"'          # 强 ETag

def serve(size, range_header=None, if_range=None, etag=ETAG):
    full = (200, {"content-length": str(size)}, size)
    if not range_header:
        return full

    # If-Range 不匹配(或弱 ETag) -> 忽略 Range, 返回全量
    if if_range is not None:
        if if_range.startswith("W/") or if_range != etag:
            return full

    unit, _, spec = range_header.partition("=")
    if unit.strip().lower() != "bytes" or not spec.strip():
        return full

    parts = [p.strip() for p in spec.split(",") if p.strip()]
    if len(parts) > 1:
        parts = parts[:1]          # 取舍: 只服务第一段, 不实现 multipart/byteranges

    start_s, _, end_s = parts[0].partition("-")
    if start_s == "":              # bytes=-N: 最后 N 字节
        n = int(end_s)
        if n <= 0:
            return (416, {"content-range": f"bytes */{size}"}, 0)
        start, end = max(0, size - n), size - 1
    else:
        start = int(start_s)
        end = int(end_s) if end_s else size - 1
        end = min(end, size - 1)   # 超出文件尾要截断, 不是报错

    if start >= size or start > end:
        return (416, {"content-range": f"bytes */{size}", "content-length": "0"}, 0)

    length = end - start + 1
    return (206, {"content-range": f"bytes {start}-{end}/{size}", "content-length": str(length)}, length)

SIZE = 1000

status, headers, n = serve(SIZE, "bytes=0-99")
print("→ 前 100 字节:", status, headers["content-range"], n)
assert status == 206 and headers["content-range"] == "bytes 0-99/1000" and n == 100

status, headers, n = serve(SIZE, "bytes=900-2000")
print("→ 尾部越界截断:", status, headers["content-range"], n)
assert status == 206 and headers["content-range"] == "bytes 900-999/1000" and n == 100

status, headers, n = serve(SIZE, "bytes=2000-")
print("→ 完全越界:", status, headers)
assert status == 416 and headers["content-range"] == "bytes */1000" and n == 0

status, headers, n = serve(SIZE, "bytes=-100")
print("→ 后缀 Range:", status, headers["content-range"], n)
assert status == 206 and headers["content-range"] == "bytes 900-999/1000" and n == 100

# 多段: 只取第一段(另一种策略是 200 全量)
status, headers, n = serve(SIZE, "bytes=0-0,2-2")
print("→ 多段只取第一段:", status, headers["content-range"], n)
assert status == 206 and headers["content-range"] == "bytes 0-0/1000" and n == 1

# If-Range: 强 ETag 匹配 -> 206; 不匹配 / 弱 ETag -> 200 全量
assert serve(SIZE, "bytes=0-99", if_range=ETAG)[0] == 206
status, headers, n = serve(SIZE, "bytes=0-99", if_range='"sha256-old"')
print("→ If-Range 不匹配:", status, n)
assert status == 200 and n == SIZE
status, _, n = serve(SIZE, "bytes=0-99", if_range='W/"sha256-abc123"')
print("→ 弱 ETag 不能用于 If-Range:", status, n)
assert status == 200 and n == SIZE

# 非法单位 -> 忽略 Range
assert serve(SIZE, "items=0-99")[0] == 200
```

**追问一**：为什么 `bytes=900-2000` 要截断成 `900-999`，而 `bytes=2000-` 是 416？—— 规范把"范围部分可满足"定义为可服务：`900-2000` 的起点在文件内，能提供 900 到文件尾的内容，所以截断末尾返回 206；`2000-` 的起点已经超过文件大小，一个字节都给不出，才是"不可满足"的 416。这个区分对断点续传很重要：客户端可能记了一个过大的 end（比如按旧文件大小算的），截断能让它拿到剩余部分；而起点越界通常意味着客户端状态错误，416 让它重新拉元数据。416 必须带 `Content-Range: bytes */size`，否则客户端不知道真实大小，可能无限重试。

**追问二**：多段 Range 为什么很少被支持？如果一定要支持，难点在哪？—— 多段响应要把多个片段拼成 `multipart/byteranges; boundary=...`，每个 part 带自己的 `Content-Range`，整体 `Content-Length` 要精确计算（包括 boundary、CRLF、part 头），任何一处算错都会让客户端解析失败；而且它破坏了"一个响应一个资源片段"的简单模型，CDN/代理缓存很难处理，收益却很小（浏览器下载通常只发单段，播放器也只发单段）。所以多数服务端（包括 nginx 的某些配置）选择"只服务第一段"或"返回 200 全量"。如果必须支持，建议用成熟库（如 `werkzeug` 的 Range 处理）而不是手写 boundary；并在测试里覆盖"空段、重叠段、逆序段、超多段"这些边界。

## 背诵要点

- 单段 Range：end 截断到 size-1；起点越界或 start>end → 416 + `Content-Range: bytes */size`；可满足 → 206 + `Content-Range: bytes s-e/size`。
- `If-Range` 只在强 ETag/日期匹配时处理 Range，否则 200 全量；弱 ETag 不能用于 If-Range。
- 多段 Range 需 multipart/byteranges，成本高收益低；常见取舍是只服务第一段或 200，并在文档/测试中写清。

## 复盘追问

- 播放器为什么对 `bytes=99999-` 返回 200 会"无限重下"？（它认为服务端不支持 Range，每次 seek 都从头下；应返回 416 + `bytes */size`）
- If-Range 用弱 ETag 会出什么问题？（弱校验允许内容等价但字节不同，客户端可能把旧片段拼到新文件上，校验失败）
