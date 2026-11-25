---
title: [Q6109] HTTP Range 请求与断点续传原理
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6109 · HTTP Range 请求与断点续传原理

> 难度:★★★★☆ | 标签:原理深挖, Range, 下载

**问**:大文件下载断点续传是怎么实现的？Range 服务端的实现要点与边界是什么？

**答**:结论：客户端在请求里带 `Range: bytes=offset-`（或闭区间 `bytes=100-199`），服务端若支持则回 **206 Partial Content** + `Content-Range: bytes 100-199/TOTAL`；不支持则必须回 200 + 全量，让客户端知道续传不被支持。实现要点：① 可靠性前提是资源未变——用 `ETag`/`Last-Modified` 配合 `If-Range`：资源变了就让服务端回 200 全量，避免把新文件拼到旧文件上；② 多区间请求（`bytes=0-99,200-299`）语义存在但工程上常拒绝（multipart 开销），静态下载场景单区间足够；③ 服务端必须做合法性裁剪——offset 越界返回 `416 Range Not Satisfiable`，`suffix`（`bytes=-500` 尾部 500 字节）要正确解析；④ 与 gzip/压缩中间件的互斥：压缩会改变字节长度，Range 必须对"原始实体"计算。Python 侧 3.12 之前可自己实现 Range 读取（`file.seek` + 定长 read），静态文件交给 nginx/对象存储（Q2923/Q2730）时是配置项。

```python
import re

RANGE_RE = re.compile(r"bytes=(\d*)-(\d*)")

def parse_range(header: str | None, total: int) -> tuple[int, int] | None:
    """返回 (start, end) 闭区间；None 表示无法满足（应回 416）或无 Range。"""
    if not header:
        return None
    m = RANGE_RE.fullmatch(header.strip())
    if not m:
        return None
    a, b = m.group(1), m.group(2)
    if a == "" and b == "":                     # "bytes=-" 非法
        return None
    if a == "":                                 # 后缀式 bytes=-500：尾部 500 字节
        n = min(int(b), total)
        return (total - n, total - 1)
    start = int(a)
    end = min(int(b), total - 1) if b else total - 1
    return (start, end) if start <= end and start < total else None

TOTAL = 10_000
print(parse_range("bytes=100-199", TOTAL))      # (100,199)
print(parse_range("bytes=-500", TOTAL))         # (9500,9999)
print(parse_range("bytes=99999-", TOTAL))       # None → 416
print(parse_range(None, TOTAL))                 # None → 200 全量

def response_plan(header, total, etag_match=True):
    r = parse_range(header, total)
    if r and etag_match:
        return 206, f"bytes {r[0]}-{r[1]}/{total}"
    if r and not etag_match:
        return 200, f"full/{total}"             # If-Range 失败 → 全量兜底
    return 416 if header else 200, "full" if not header else ""

print(response_plan("bytes=0-99", TOTAL), "|", response_plan("bytes=0-99", TOTAL, False))
```

**追问一层**:`If-Range` 用 ETag 和用 Last-Modified 的差异？为什么强校验器更适合？
**追二层**:Range 与 304/ETag 缓存链（Q6070）如何叠加？CDN 对 Range 的缓存键怎么变？

**背诵要点**
- Range 续传=请求头 Range + 206 + Content-Range；不支持就回 200 全量。
- 一致性靠 If-Range：资源变更自动退回 200，杜绝拼接错乱。
- 服务端要处理越界 416、后缀式区间、与压缩中间件互斥。

**复盘追问**
- 并发分片下载时多区间请求要不要支持？提示：客户端拆成多请求单区间更可控。
- 网关限流与 Range 组合的坑？提示：按响应字节数计费限流，而非按请求数。
