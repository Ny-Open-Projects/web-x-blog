---
title: [Q2913] 并发下载的分段合并:Range 分片与 md5 对账
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2913 · 并发下载的分段合并:Range 分片与 md5 对账

> 难度:★★★ | 标签:并发下载, Range, 分片合并

**问**:大文件下载慢,用多线程分段下载怎么落地?拼回去怎么保证一个字节都不少?

**答**:三步:探测总长、分段并发、按偏移拼装。先请求 size 端点拿到文件大小,均分为 4 段算好各自的字节区间;每个 worker 带 Range 头并发抓取,服务端回 206 和对应切片;各段数据按 offset 写进预分配缓冲的各自区域——区域互不重叠,天然免锁。拼完必须对账:md5 与原始文件一致才算下载成功,这最后一道校验是分段下载的收口,任何一段被截断或错位都能当场抓获。实测 300KB 文件,服务端按字节量制造传输延迟:单流 0.63 秒,4 段并发 0.22 秒,加速约 2.9 倍,md5 一致。

- 分段数不是越多越好:每段都有连接与延迟开销,通常 4 到 8 段封顶;

- Range 头要处理服务端不支持的情况:对方回了 200 全量,就得退化为单流;

- 预分配 bytearray 加区域写入,比"先收集再拼接"省一次大拷贝。

```python
# file: code/02_并发与网络工程/q2913_segment_download.py
# -*- coding: utf-8 -*-
"""并发下载的分段合并: Range 分片 + 多线程抓取 + 拼装校验。

- 先取 /size 知道总长, 均分为 N 段, 每段一个 worker 带 Range 头抓取;
- 各段写进预分配缓冲的各自区域, 互不重叠, 无需加锁;
- 合并后 md5 对账; 对照单流下载, 服务端按字节量制造延迟, 加速比可见。
"""
import hashlib
import json
import re
import socket
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# 确定性文件内容: 300KB
FILE = bytes((i * 31 + 17) % 256 for i in range(300000))
FILE_MD5 = hashlib.md5(FILE).hexdigest()
OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))
RANGE_RE = re.compile(r"bytes=(\d+)-(\d+)$")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/size":
            body = json.dumps({"size": len(FILE)}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if self.path != "/file":
            self.send_error(404)
            return
        m = RANGE_RE.match(self.headers.get("Range") or "")
        if m:
            start, end = int(m.group(1)), int(m.group(2))
        else:
            start, end = 0, len(FILE) - 1
        chunk = FILE[start:end + 1]
        time.sleep(0.02 + len(chunk) * 2e-6)   # 传输延迟与字节数挂钩
        self.send_response(206 if m else 200)
        self.send_header("Content-Type", "application/octet-stream")
        self.send_header("Content-Range",
                         "bytes %d-%d/%d" % (start, end, len(FILE)))
        self.send_header("Content-Length", str(len(chunk)))
        self.end_headers()
        self.wfile.write(chunk)

    def log_message(self, *args):
        pass


def wait_port(port, timeout=5.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return True
        except OSError:
            time.sleep(0.05)
    return False


def fetch_range(base, start, end):
    """抓一个字节区间, 返回 (offset, 数据)。"""
    req = urllib.request.Request(base + "/file",
                                 headers={"Range": "bytes=%d-%d" % (start, end)})
    with OPENER.open(req, timeout=10) as resp:
        if resp.status != 206:
            raise IOError("expect 206, got %d" % resp.status)
        return start, resp.read()


def segmented_download(base, size, segments):
    """分 4 段并发抓取, 按偏移拼装。"""
    step = (size + segments - 1) // segments
    jobs = [(o, min(o + step, size) - 1) for o in range(0, size, step)]
    out = bytearray(size)
    with ThreadPoolExecutor(max_workers=segments) as pool:
        for offset, data in pool.map(lambda j: fetch_range(base, j[0], j[1]),
                                     jobs):
            out[offset:offset + len(data)] = data   # 各段区域互不重叠
    return bytes(out)


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    srv.daemon_threads = True
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    assert wait_port(port)
    base = "http://127.0.0.1:%d" % port

    with OPENER.open(base + "/size", timeout=5) as resp:
        size = json.loads(resp.read())["size"]

    t1 = time.perf_counter()
    with OPENER.open(base + "/file", timeout=30) as resp:   # 单流对照
        single = resp.read()
    t_single = time.perf_counter() - t1

    t1 = time.perf_counter()
    merged = segmented_download(base, size, 4)
    t_multi = time.perf_counter() - t1

    print("文件 %d 字节: 单流 %.2fs, 4 段并发 %.2fs, 加速 %.1fx"
          % (size, t_single, t_multi, t_single / t_multi))
    print("md5 对账: %s" % ("一致" if hashlib.md5(merged).hexdigest()
                            == FILE_MD5 else "不一致"))
    assert single == FILE and merged == FILE
    assert t_multi < t_single, "并发分段应更快"
    srv.shutdown()
    print("要点: Range 定分段边界, 各段各写各的区域免锁, 合并后 md5 收口")
```

**追问**:1) 某一段中途失败了怎么办?——只重试那一段,这正是分段下载的副产品:断点续传的粒度就是段。2) 怎么知道该分几段?——看文件大小和单流吞吐,小文件不分段,大文件用"想要的并行度"来定段数,再实测校准。3) 底层机制:为什么"区域互不重叠"就免锁?——各段写进预分配 bytearray 的不同下标区间,区间不重叠的切片赋值彼此独立,无共享可变竞态;顺带省掉"先收集再拼接"的一次全量大拷贝。4) 生产陷阱?——服务端不支持 Range 回了 200 全量,代码不校验 status 把全量当切片写入,文件错位翻倍(必须校验 206);段边界 off-by-one(end 含端),少一字节 md5 不过;不分段大小下限,小文件分段开销倒亏。

---
