---
title: [Q5610] 非阻塞 connect 与 EINPROGRESS 原理
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5610 · 非阻塞 connect 与 EINPROGRESS 原理

> 难度:★★★★☆ | 标签:原理深挖, connect, 多路复用

**问**:`connect` 是阻塞调用，asyncio 凭什么能同时发起上千个连接？底层发生了什么？

**答**:结论：把 socket 置为非阻塞后，`connect()` 对未完成的三次握手返回 `EINPROGRESS`（"连接已在内核进行中"），fd 变成"可写即表示连接结果就绪"：握手成功变可写，失败（RST）变可写+可读且 `getsockopt(SO_ERROR)` 带出错误。事件循环就靠这个把 N 个并发 connect 登记进 epoll 的写集合，谁就绪处理谁——这就是 asyncio/所有多路复用框架做并发外呼的底层机制。坑点：① 成功判定不能只看"可写"，要显式 `getsockopt(SO_ERROR)` 排错；② `select` 对已完成连接的写就绪语义在部分平台上有误报历史（历史上 connect 失败不总是置可写，Windows/select 有差异），标准库封装已处理，自己手写要小心；③ 超时要自己用 `loop` 定时器挂 fd（对应 `sock.settimeout` 阻塞版的语义）。

```python
import errno, socket

def nonblock_connect_demo(host="127.0.0.1", port=1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(False)
    try:
        s.connect((host, port))            # 立即返回或抛 EINPROGRESS
        return "已连上（罕见，loopback 立即完成）"
    except BlockingIOError:
        # 3.x 里 EINPROGRESS 表现为 BlockingIOError，连接在内核进行中
        return f"EINPROGRESS：等待内核完成三次握手（fd 就绪性={s.fileno() > 0}）"
    except OSError as e:
        s.close()
        return f"立即失败：{e}"
    finally:
        try:
            s.close()
        except OSError:
            pass

print(nonblock_connect_demo())
print("连接结果判读顺序：可写 → getsockopt(SO_ERROR) → 0 成功 / 非 0 错误码")
print("errno 对照：EINPROGRESS =", errno.EINPROGRESS, "| EALREADY =", errno.EALREADY)
```

**追问一层**:为什么"可写"不能直接当"连接成功"？`SO_ERROR` 的取值时机有什么讲究？
**追二层**:asyncio 的 `open_connection` 里 connect 超时是怎么挂的？和阻塞版 `settimeout` 的实现（SO_SNDTIMEO vs 定时器）有何不同？

**背诵要点**
- 非阻塞 connect 立即返回 EINPROGRESS，握手由内核异步完成。
- 结果就绪=fd 可写；成功与否必须 getsockopt(SO_ERROR) 判定。
- 并发 connect 的本质：N 个 fd 登记进 epoll 写集合，就绪即处理。

**复盘追问**
- 批量外呼中"半完成连接堆积"如何观测与清理？提示：连接池状态机 + 超时回收（Q5603）。
- 手写 selector 版并发 connect 时，Windows 下还有什么平台差异要兼容？提示：proactor 与 select 的就绪语义差（Q5521）。
