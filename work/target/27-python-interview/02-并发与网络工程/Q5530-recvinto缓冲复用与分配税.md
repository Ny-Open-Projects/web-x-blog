---
title: [Q5530] recv_into 与缓冲复用：读侧的分配税
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5530 · recv_into 与缓冲复用：读侧的分配税

> 难度:★★★★ | 标签:recv_into, memoryview, 性能

**问**：高吞吐读循环里 `recv(65536)` 每次都在干什么重复功？`recv_into` 怎么消掉它？`bytearray` + `memoryview` 的组合有什么必踩的坑（BufferError）？为什么 send 侧有 sendfile 零拷贝而读侧只能靠缓冲复用？

**答**：`recv(65536)` 每次分配一个新 bytes 对象：高频读循环下每秒百万级短命对象——分配锁竞争 + GC 压力（扫描/回收都是税）。`recv_into(buf)` 把字节直接写进**预分配的 bytearray**，只返回长度，分配次数归零；配合 `memoryview` 切片可零拷贝送进后续解析。两个必踩坑：1) **BufferError**——bytearray 有活跃 memoryview 导出时禁止 resize（`extend`/`append` 抛 `Existing exports of data: object cannot be re-sized`），先 `del mv` 释放再改长度；2) **切片也别长持**——`mv[i:j]` 本身是新的导出句柄，解析完立即释放。读侧与 send 侧的不对称：sendfile 只能"文件→socket"零拷贝（Q659/Q1873），**socket→用户内存**这半程数据终归要进应用（协议解析需要），所以读侧的最优解就是"一个缓冲反复用"，而不是幻想零拷贝。

```python
# file: code/02_并发与网络工程/q5530_recv_into.py
import socket, threading, time

TOTAL, CHUNK = 20_000_000, 65536

def pump(sock):
    block = CHUNK * b"x"
    sent = 0
    while sent < TOTAL:
        n = sock.send(block[:min(CHUNK, TOTAL - sent)])
        sent += n
    sock.close()

def read_by_recv(s):
    got = 0
    while True:
        d = s.recv(CHUNK)            # 每次新建 bytes
        if not d:
            break
        got += len(d)
    return got

def read_by_recv_into(s):
    buf = bytearray(CHUNK)
    got = 0
    while True:
        n = s.recv_into(buf)         # 复用同一缓冲
        if n == 0:
            break
        got += n
    return got

def bench(mode):
    a, b = socket.socketpair()
    b.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1 << 22)
    t = threading.Thread(target=pump, args=(a,))
    t.start()
    t0 = time.perf_counter()
    got = (read_by_recv if mode == "recv" else read_by_recv_into)(b)
    dt = time.perf_counter() - t0
    t.join()
    return got, dt

g1, t1 = bench("recv")
g2, t2 = bench("recv_into")
print(f"recv      : {g1} 字节 {t1*1000:.1f} ms")
print(f"recv_into : {g2} 字节 {t2*1000:.1f} ms (分配次数为 0)")

# BufferError 陷阱: 有 memoryview 导出时禁止 resize
buf = bytearray(CHUNK)
mv = memoryview(buf)
try:
    buf.extend(b"y")
except BufferError as e:
    print("导出期间 resize 被拒:", e)
del mv                              # 释放导出后恢复可变
buf.extend(b"y")
print("释放后可 resize: True")
```

**追问**：1) recv_into 后怎么"零拷贝"交给解析器？——`memoryview(buf)[:n]` 切片直接喂 `struct.unpack_from`/帧解析（Q1591），避免 bytes(n) 拷贝；解析完 `del` 切片再复用缓冲。2) 为什么不干脆维护一个环形缓冲？——变长帧场景环形缓冲 + 追踪读写游标确实更优（Q2680 滑动窗口思想），但要处理"跨环帧"的拷贝回卷；固定池 + recv_into 是成本最低的第一步。3) GC 压力怎么量化？——`gc.get_stats()` 看 gen0 collection 次数与耗时对比两模式，或 py-spy 火焰图里 alloc/seq 相关栈的占比。

## 背诵要点
1. recv(65536) 每次新建 bytes 对象 = 分配锁 + GC 税；recv_into 写入预分配 bytearray，分配归零。
2. bytearray 被内存视图导出时禁止 resize（BufferError），先 del 再改长度。
3. sendfile 只覆盖文件→socket 方向；socket→应用内存没有零拷贝，缓冲复用是读侧最优解。

## 复盘追问
1. 网关高并发下把 recv 换成 recv_into，收益怎么验证而不是拍脑袋？（提示：压测对比 RPS/p95 与 GC 停顿（gen0 次数），关注分配热点是否从 recv 移走，参考 Q1376 指标口径）
2. 缓冲复用引入"数据生命周期"新风险（解析慢导致缓冲被覆盖），怎么在工程上防？（提示：视图切片仅短持有 + 帧解析前显式拷贝长生命周期字段，评审规则禁"保存 mv 跨 await/跨函数"）
