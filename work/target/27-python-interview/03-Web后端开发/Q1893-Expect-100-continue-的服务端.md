---
title: [Q1893] Expect 100-continue 的服务端决策
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1893 · Expect 100-continue 的服务端决策

> 难度:★★★☆ | 标签:HTTP, 上传

**问**:客户端带了 Expect: 100-continue,服务端应该怎么处理?

**答**:该头的含义是"我有一个大请求体,你先确认能不能收"。服务端决策三步:先按 Content-Length 或分块长度判断是否超限,超限直接回 413 并不读体,客户端省掉整个上传,这是该机制最大的价值;再看期望本身能否满足,不认识的期望回 417 Expectation Failed;可以收才发 HTTP/1.1 100 Continue 这一空响应,然后正常读体处理。实现要尊重客户端的等待窗口:客户端发 Expect 后通常只等几百毫秒,超时就认为服务端不支持而直接发体,所以响应慢等于没有决策,决策逻辑必须放在读体之前、轻量可判断。HTTP/2 不需要该机制,流控天然先问后发;框架层(http.server、Nginx)都有对应开关。

```python
# file: code/03_Web后端开发/q1893_expect_continue.py
"""Expect 100-continue 的服务端决策: 先答应再收体(纯标准库模拟, 无真实网络)。"""
import json


class FakeConn:
    """用列表模拟半双工连接, send 写入帧, 供断言与观察。"""

    def __init__(self):
        self.sent = []
        self.body_requested = False

    def send(self, frame):
        self.sent.append(frame)

    def ask_body(self):
        self.body_requested = True


MAX_BODY = 1 << 20     # 服务端上限 1MB


def handle_request(conn, head):
    """服务端对带 Expect: 100-continue 的请求做出决策。

    决策序: 超限先拒(413 且不收体) -> 无法满足的期望(417) -> 发 100 再收体。
    """
    lines = head.split("\r\n")
    headers = {}
    for line in lines[1:]:
        if ":" in line:
            k, v = line.split(":", 1)
            headers[k.strip().lower()] = v.strip()
    expectations = [e.strip().lower()
                    for e in headers.get("expect", "").split(",") if e.strip()]
    if "100-continue" in expectations:
        length = int(headers.get("content-length", "0"))
        if length > MAX_BODY:
            conn.send("HTTP/1.1 413 Payload Too Large\r\n\r\n")   # 不发 100, 不收体
            return 413
        if len(expectations) > 1:
            conn.send("HTTP/1.1 417 Expectation Failed\r\n\r\n")  # 不认识的期望
            return 417
        conn.send("HTTP/1.1 100 Continue\r\n\r\n")                # 答应后再收体
        conn.ask_body()
        conn.send("HTTP/1.1 201 Created\r\n\r\n")
        return 201
    conn.send("HTTP/1.1 400 Bad Request\r\n\r\n")
    return 400


# 场景一: 正常 100-continue, 客户端先问再发
c1 = FakeConn()
s1 = handle_request(c1, "POST /upload HTTP/1.1\r\nHost: a\r\n"
                        "Expect: 100-continue\r\nContent-Length: 800\r\n\r\n")
print("场景一 -> 状态", s1, "帧序列:", [f.split()[1] for f in c1.sent],
      "收体:", c1.body_requested)
assert s1 == 201 and c1.body_requested

# 场景二: 体超限, 服务端不答应直接 413, 客户端省去整个上传
c2 = FakeConn()
s2 = handle_request(c2, "POST /upload HTTP/1.1\r\nExpect: 100-continue\r\n"
                        "Content-Length: {}\r\n\r\n".format(MAX_BODY + 1))
print("场景二 -> 状态", s2, "帧序列:", [f.split()[1] for f in c2.sent],
      "收体:", c2.body_requested)
assert s2 == 413 and not c2.body_requested

# 场景三: 携带服务端不支持的期望 -> 417
c3 = FakeConn()
s3 = handle_request(c3, "POST /upload HTTP/1.1\r\nExpect: 100-continue, 200-please\r\n"
                        "Content-Length: 10\r\n\r\n")
print("场景三 -> 状态", s3)
assert s3 == 417

print("要点: 100-continue 的价值在服务端敢于先拒绝, 把昂贵请求体挡在传输之前")
```

**追问**:
- 客户端不等 100 直接发体会怎样?——协议允许,服务端把 100 与最终响应都正常回即可,只是省流量的优化失效。
- 超限与不支持期望同时发生回哪个?——按决策序先判长度,413 优先;417 只在期望本身无法满足时出现。
