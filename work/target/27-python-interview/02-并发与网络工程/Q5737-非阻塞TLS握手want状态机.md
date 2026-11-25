---
title: "[Q5737] 非阻塞 TLS 握手：want_read/want_write 状态机与事件循环集成"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5737 · 非阻塞 TLS 握手：want_read/want_write 状态机与事件循环集成

难度：P7 ｜ 标签：非阻塞 TLS、SSLWantReadError、SSLWantWriteError、do_handshake、状态机、selector、事件循环集成

**问**：非阻塞 socket 上 `do_handshake()` 抛 `SSLWantReadError` 是错误还是信号？TLS 握手为什么会有"需要写"的状态（want_write）？把非阻塞握手集成进 selector 事件循环的正确姿势是什么？为什么说"抛 SSLWantReadError 就只注册 EVENT_READ"在某些场景下会卡死？

**答**：
结论：在非阻塞（或超时模式）socket 上调用 `SSLSocket.do_handshake()`（构造时传 `do_handshake_on_connect=False`），握手没完成时**不是失败而是分步信号**：`ssl.SSLWantReadError` = OpenSSL 需要读更多字节（等对端数据）、`ssl.SSLWantWriteError` = OpenSSL 需要**发送**数据但发送缓冲满了——这两个异常是 OpenSSL 的 `WANT_READ/WANT_WRITE` 状态的 Python 化，语义是"请把我放回事件循环，条件就绪再调一次"。集成的正确姿势是**按信号重新注册事件**：抛 SSLWantReadError → 关注 EVENT_READ、SSLWantWriteError → 关注 EVENT_WRITE，循环直至成功——这就是"状态机驱动"的握手。关键细节：**want_read 时不代表不需要写**——OpenSSL 内部状态可能在"读完这批后要回写"，权威做法是按异常类型精确注册（想省事也可以同时注册 READ|WRITE 直到握手完成，代价是多几轮空转）；绝不能想当然"want_read 就永远只等读"——TLS 握手是读写交替的多轮协议（ClientHello→ServerHello...Certificate...Finished），每一轮都可能落在读或写。与阻塞模式的对照：阻塞 socket 上 `do_handshake_on_connect=True` 自动完成，但那会把事件循环卡死在握手阶段（Q5572 事故）——异步服务里握手必须非阻塞化或丢进线程池。

取舍：a) asyncio 用户的答案是"别手写"：`loop.start_tls()` / asyncio 内置完成这套状态机，手写仅用于自研 loop 或教学；b) 自研 selector 事件循环：按异常类型精确注册事件，握手完成后再切换到数据阶段的事件策略（改注册才生效，selectors 的 register/modify）；c) 握手超时必须显式：状态机循环要带 deadline，恶意/慢客户端可以让握手"永远差一个字节"——每轮 SSLWant* 都重置 deadline 就是 DoS 面（Q5534 握手容量账）；d) 手握 TLSSession 复用（session resumption，Q5534）：非阻塞路径下复用信息在 context 层，与事件注册正交；e) 阻塞降级路径：线程池里做阻塞握手省事，但连接数大时线程池成为瓶颈——量级判断后二选一，不混用。

实战：事故形态是"自研网关把握手放在 connect 后直接 do_handshake()，遇到 SSLWantWriteError 未捕获当普通错误断连——大证书链（跨几个 TCP 段）场景下偶发握手失败率 2%；修复为信号驱动的状态机循环 + 每轮 deadline，失败率归零"。下面实测非阻塞握手状态机的完整驱动。

```python
# 非阻塞 TLS 握手: want_read/want_write 状态机驱动
import selectors
import socket
import ssl
import threading
import time

# 线程侧: 阻塞式 TLS 服务端 (服务端简单化, 重点在客户端非阻塞状态机)
import tempfile, os, subprocess
d = tempfile.mkdtemp()
key, crt = os.path.join(d, "k.pem"), os.path.join(d, "c.pem")
subprocess.run(["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
                "-keyout", key, "-out", crt, "-days", "1", "-subj", "/CN=localhost"],
               check=True, capture_output=True)
ctx_srv = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx_srv.load_cert_chain(crt, key)
ctx_cli = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctx_cli.load_verify_locations(crt)

ready = threading.Event()
tmp_srv = socket.socket()
tmp_srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tmp_srv.bind(("127.0.0.1", 0))
probe_port = tmp_srv.getsockname()[1]
tmp_srv.close()

def serve(port: int) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", port))
    srv.listen(1)
    ready.set()
    srv.settimeout(5)
    conn, _ = srv.accept()
    tls = ctx_srv.wrap_socket(conn, server_side=True)
    tls.send(b"ok")
    tls.close(); srv.close()

threading.Thread(target=serve, args=(probe_port,), daemon=True).start()
ready.wait()

print("[1] 客户端: 非阻塞 socket + do_handshake_on_connect=False")
raw = socket.create_connection(("127.0.0.1", probe_port), timeout=5)
raw.setblocking(False)
tls = ctx_cli.wrap_socket(raw, server_hostname="localhost", do_handshake_on_connect=False)

print("[2] 状态机循环: 按异常类型重新注册事件, 直到握手完成")
sel = selectors.DefaultSelector()
events_log = []
deadline = time.monotonic() + 5.0
while True:
    if time.monotonic() > deadline:
        raise SystemExit("handshake deadline exceeded")
    try:
        tls.do_handshake()                       # 每次调用推进一小步
        break
    except ssl.SSLWantReadError:
        events_log.append("want_read")
        sel.register(tls, selectors.EVENT_READ)
        sel.select(timeout=1.0)
        sel.unregister(tls)
    except ssl.SSLWantWriteError:
        events_log.append("want_write")
        sel.register(tls, selectors.EVENT_WRITE)
        sel.select(timeout=1.0)
        sel.unregister(tls)
print("    握手期间信号序列:", events_log, "<- 读写交替, 按信号精确注册")
print("    握手版本:", tls.version(), "| 密码套件:", tls.cipher()[0])

print("[3] 数据阶段: 收服务端回包")
sel.register(tls, selectors.EVENT_READ)
for key, _ in sel.select(timeout=2.0):
    print("    收到:", tls.recv(16))
sel.unregister(tls); sel.close()
tls.close()
print("[4] 纪律: 状态机循环带 deadline (防恶意慢握手); asyncio 用户直接用 loop.start_tls() 不手写")
```

**追问一**：为什么 OpenSSL 会"握手时需要写"？want_write 出现的具体场景是什么？—— TLS 握手是**双方各自发送多条消息的协议**（ClientHello / ServerHello+Certificate+ServerKeyExchange / ClientKeyExchange+ChangeCipherSpec+Finished 等），每条消息写入 TCP 发送缓冲。want_write 的典型触发：①**发送缓冲满**——ServerHello+证书链（几 KB）一次性序列化时，对端接收慢或链路 RTT 高，缓冲塞不下，OpenSSL 暂停等你腾空间；②**重协商/双向认证**中客户端侧的 ClientKeyExchange 在缓冲满时同样触发；③MTU 交互：大证书链跨多个 TCP 段，写路径分段（Q5688 非阻塞部分写家族）。所以"TLS 握手只读"的直觉来自小证书单段场景——证书链越大、链路越差，want_write 概率越高，这正是"测试环境没事、生产偶发"的典型来源。理解这个就能把"按信号精确注册"从教条变成必然。

**追问二**：握手状态机与"每轮重置 deadline"的 DoS 面是什么关系？怎么设计握手预算？—— 攻击面：握手状态机的每轮 SSLWant* 都在等待"条件就绪"，若客户端刻意每 0.9s 发一个字节让状态机持续 want_read，服务端为这条半死连接消耗一个事件注册与缓冲——海量这种连接就是 slowloris 的 TLS 变体（Q5534 握手容量账、Q2914 最大连接保护家族）。预算设计三件套：①**总预算**：整个握手（从建立到 Finished）一个硬 deadline（如 10s），状态机循环以总时长判断，而不是每轮重置——每轮重置等于预算无效；②**步数预算**：限制 do_handshake 的调用轮次（正常握手 < 10 轮），超步直接断——防"字节滴漏"式推进；③**连接级额度**：同一来源同时处于握手期的连接数上限（信号量），超限快速拒绝。与阻塞降级路径对比：线程池阻塞握手天然被池大小约束，但也把 DoS 转移成池耗尽——没有免费的形态，只有显式的预算。这也是"协议状态机必须带预算"的通用规律：TCP 半开（SYN Flood）、HTTP 慢速头、TLS 慢握手是同一族攻击。

## 背诵要点
- 非阻塞 do_handshake 抛 SSLWantReadError/SSLWantWriteError 是分步信号不是失败；按异常类型重新注册 EVENT_READ/WRITE 循环到完成。
- TLS 握手读写交替多轮，证书链大/缓冲满时触发 want_write——"want_read 就只等读"会卡死；asyncio 用 loop.start_tls() 不手写。
- 握手状态机必须带总预算（deadline + 轮次上限 + 并发握手额度），防 slowloris TLS 变体；每轮重置 deadline 等于无预算。

## 复盘追问
- 非阻塞握手偶发 SSLWantWriteError 未捕获断连，根因？（大证书链跨段、发送缓冲满；按信号驱动状态机注册事件）
- 慢客户端让握手永远差一个字节怎么办？（握手总预算+轮次预算+并发额度，防每轮重置 deadline 的伪预算）
