---
title: "[Q5646] sendfile 零拷贝与文件下发吞吐成本账"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5646 · sendfile 零拷贝与文件下发吞吐成本账

难度：P6 ｜ 标签：sendfile、零拷贝、socket、成本工程

**问**：静态文件下发服务用 `shutil.copyfileobj(f, socket.makefile('wb'))` 只能跑到 300MB/s，换 `os.sendfile` 后翻倍。用户态-内核态之间发生了几次拷贝？sendfile 的零拷贝省在哪、边界条件（TLS、小文件、需要改内容）有哪些？

**答**：
结论：传统路径一次文件下发要 4 次拷贝 + 4 次上下文切换：磁盘→内核页缓存（DMA）、页缓存→用户缓冲（`read`）、用户缓冲→socket 缓冲（`write`）、socket 缓冲→网卡（DMA）。`os.sendfile(out_fd, in_fd, offset, count)` 把中间两步合并进内核：数据从页缓存直达 socket 缓冲，用户态全程不碰数据，省 2 次拷贝与一半上下文切换；配合网卡 scatter-gather（零拷贝真形态）连 socket 缓冲都只传元数据。

取舍与边界：① sendfile **不能加工数据**——要压缩、加密（TLS）、动态注入头部内容就不能走纯 sendfile，TLS 加密必须在用户态完成，所以 HTTPS 场景收益减半或归零（除非内核 TLS kTLS）；② 小文件收益被 setup 成本吃掉，阈值以下直接 `write` 更快；③ macOS 与 Linux 的 sendfile 语义有差异（macOS 版本仅支持 socket 输出、参数不同），跨平台要做降级封装；④ offset 语义 Linux 会自动推进、macOS 需自己维护。

实战：下发服务分层——HEAD/Range 协商后，明文 HTTP 大文件走 sendfile（uvicorn/nginx 都内置），Python 层做"探测 sendfile 可用 → 不支持降级到 64KB 缓冲 copyfileobj"的两级策略；压测对比 P95 与 CPU%，把零拷贝收益折算成单机并发容量。

```python
import os
import socket
import socketserver
import tempfile
import threading
import time

PAYLOAD = os.urandom(1 * 1024 * 1024)        # 1MB 演示文件

def serve_once(port_holder):
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    port_holder.append(srv.getsockname()[1])
    srv.listen(1)
    conn, _ = srv.accept()
    path = tempfile.mktemp()
    with open(path, "wb") as f:
        f.write(PAYLOAD)
    fd = os.open(path, os.O_RDONLY)
    try:
        # macOS: sendfile(fd, sock, offset, count, flags)；Linux: sendfile(out, in, offset, count)
        if sys_platform_darwin():
            # macOS 的 os.sendfile 参数顺序为 (file, socket, offset, count)
            sent = os.sendfile(fd, conn.fileno(), 0, len(PAYLOAD))
        else:
            sent = os.sendfile(conn.fileno(), fd, 0, len(PAYLOAD))
        print("sendfile bytes:", sent)
    except (AttributeError, OSError) as e:
        print("sendfile unavailable, fallback copy:", e)
        conn.sendall(PAYLOAD)
    finally:
        os.close(fd)
        os.unlink(path)
        conn.close()
        srv.close()

def sys_platform_darwin():
    import sys
    return sys.platform == "darwin"

port_holder: list[int] = []
t = threading.Thread(target=serve_once, args=(port_holder,), daemon=True)
t.start()
while not port_holder:
    time.sleep(0.01)

cli = socket.create_connection(("127.0.0.1", port_holder[0]))
cli.settimeout(3)
chunks = []
total = 0
while total < len(PAYLOAD):
    buf = cli.recv(65536)
    if not buf:
        break
    chunks.append(buf)
    total += len(buf)
print("received:", total, "match:", b"".join(chunks) == PAYLOAD)
cli.close()
t.join(timeout=2)
```

**追问一**：为什么 TLS 终结让 sendfile 收益归零？——TLS 加密在用户态，必须把页缓存数据读回用户空间加密再写入 socket；nginx 的折衷是 `ssl_buffer_size` 调优与 kTLS（内核 TLS 卸载，Linux 4.13+/nginx 1.21），启用 kTLS 后 sendfile 收益恢复。

**追问二**：Range 请求怎么与 sendfile 配合？——直接把 offset 设为 range 起点、count 设为 range 长度，天然支持断点续传，这也是 Q6109 Range 协议的服务端最优实现路径；对比 read+write 方案省一次用户态拷贝。

**追问三**：如何测量"拷贝次数差"的贡献而不是猜？——`perf stat` 的上下文切换/系统调用数对比 + `strace -c` 统计 read/write 次数消失；CPU% 与吞吐双指标压测（相同 QPS 下 CPU 降即零拷贝生效）。

## 背诵要点
- 传统下发 4 拷贝 4 切换；sendfile 把页缓存→socket 合并进内核，省 2 拷贝与一半切换。
- 三个边界：TLS/kTLS、小文件 setup 成本、macOS/Linux 参数语义差异（offset 自推进与否）。
- 生产姿势：探测可用性 + 降级到缓冲 copyfileobj；Range 直接映射 offset/count。

## 复盘追问
- 网关层已做 TLS 终结，后端 Python 服务的 sendfile 还有意义吗？（网关到后端是内网明文可用，端到端 TLS 时归零，讨论架构分层与收益归属）
- 小图床场景（平均 8KB）该不该上 sendfile？（阈值以下 setup 成本主导，改为批量合并/CDN 卸载，讨论与 Q6056 的衔接）
