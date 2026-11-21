---
title: [Q5572] ssl 握手阻塞事件循环的事故复盘
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5572 · ssl 握手阻塞事件循环的事故复盘

> 难度:★★★★ | 标签:事故复盘, ssl, asyncio, 阻塞

**问**：把同步 HTTPS 客户端代码"顺手"搬进协程里，上线后整个 asyncio 服务的 P99 从 5ms 飙到 2s+，其他协程全部排队。TLS 握手在 asyncio 里为什么会阻塞？`ssl.wrap_socket` 的 `do_handshake_on_connect`、非阻塞模式下的 `SSLWantReadError/SSLWantWriteError`、以及 `loop.start_tls` 各自的角色是什么？

**答**：结论：根因是**同步 ssl 模块的握手是阻塞系统调用集**——`SSLObject.do_handshake()` 内部要多次网络往返（TLS 1.3 一次 RTT、1.2 两次，还要读证书、可能做 OCSP），这些 recv/send 在协程里直接阻塞线程，事件循环被独占，所有其他连接跟着超时。机制拆解：a) 同步 `ssl.SSLContext.wrap_socket` 默认 `do_handshake_on_connect=True`，在阻塞 socket 上"连上即握手"；对已设为非阻塞的 socket 它会抛 `SSLWantReadError/SSLWantWriteError`（握手没完成，等相应方向就绪），需要调用方自己驱动状态机——**asyncio 内部正是这么实现的**（`sslproto` 状态机挂 read/write 回调），所以正确路径不是自己搓，而是用 asyncio 原语；b) 升级路径：`loop.start_tls(transport, ctx, server_side=...)` 把"裸 TCP transport"升级成 TLS transport，服务端在 asyncio.start_server 后按需 STARTTLS 用它，客户端等价物是 `asyncio.open_connection(ssl=ctx)`（内部即 start_tls）；c) 事故的第二形态是**握手成本被低估**：每请求新建连接 → 每请求完整握手（Q5534 的 session 复用没开），CPU 被 RSA/ECDHE 运算吃满，即便不阻塞 loop 也会拖垮 P99；d) 取舍：握手期间该连接本身不该有别的协程任务，但绝不能阻塞 loop——判据就是"slow callback 超过 100ms 告警"（Q5565 debug 工具）。实战：同步迁移到异步的清单第一项就是 grep `ssl.wrap_socket/requests/http.client`，全部替换为 asyncio 原生客户端或丢线程池。

```python
# file: code/02_并发与网络工程/q5572_tls_handshake.py
import asyncio, ssl, time, tempfile, subprocess, os, sys

# 1) 自签证书(演示环境): openssl 生成
d = tempfile.mkdtemp()
key, cert = os.path.join(d, "k.pem"), os.path.join(d, "c.pem")
subprocess.run(["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
                "-keyout", key, "-out", cert, "-days", "1", "-subj", "/CN=localhost"],
               check=True, capture_output=True)

# 2) 同步阻塞握手(事故形态): do_handshake 直接吃掉线程时间
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain(cert, key)

async def blocking_handshake_demo():
    # 模拟事故: 在协程里做同步阻塞握手等价物(这里用 sleep 代指其网络往返)
    await asyncio.sleep(0)          # 占位: 真实场景是 ssl.SSLContext.wrap_socket(阻塞)
    return "同步握手独占线程 ~1-2 RTT, 期间 loop 停摆"

async def main():
    # 3) 正确形态: asyncio 原生 TLS, 握手由 sslproto 状态机异步驱动
    sctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    sctx.load_cert_chain(cert, key)
    cctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    cctx.check_hostname = False; cctx.verify_mode = ssl.CERT_NONE  # 仅演示

    async def server(reader, writer):
        data = await reader.read(100)
        writer.write(b"ok-" + data); await writer.drain(); writer.close()

    srv = await asyncio.start_server(server, "127.0.0.1", 0, ssl=sctx)
    port = srv.sockets[0].getsockname()[1]
    t0 = time.perf_counter()
    r, w = await asyncio.open_connection("127.0.0.1", port, ssl=cctx)
    w.write(b"ping"); await w.drain()
    print("异步 TLS 响应:", await r.read(100), f"耗时 {time.perf_counter()-t0:.3f}s")
    w.close(); await w.wait_closed(); srv.close(); await srv.wait_closed()

    # 4) 事故对照: 同步握手期间, 其他协程全部排队
    async def victim(tag):
        return tag
    async def blocker():
        await asyncio.sleep(0.3)    # 代表阻塞握手的时长
    t0 = time.perf_counter()
    await asyncio.gather(blocker(), victim("v1"), victim("v2"))
    print("若 blocker 是真阻塞调用, v1/v2 的 P99 = 阻塞时长: %.2fs" % (time.perf_counter() - t0))

asyncio.run(main())
print("TLS1.3 握手 1-RTT vs 1.2 双 RTT: 客户端建连成本减半(详见 Q5534 session 复用)")
print("python:", sys.version.split()[0])
```

**追问**：1) `SSLWantReadError` 状态机怎么驱动才对？——非阻塞 socket 上捕获 Want* 后把 fd 交给 selector（读方向挂 EVENT_READ），就绪后再调一次 `do_handshake()`，直到成功；自己搓这套要处理**读/写交替**（WantWrite 可能发生在读会话里），这就是为什么强烈建议直接用 asyncio/loop.start_tls，手写状态机是 bug 高发区。2) STARTTLS 协议（smtp/redis）在 asyncio 里怎么实现？——先裸连接收服务端 banner，客户端发 STARTTLS 命令，然后 `loop.start_tls(existing_transport, ctx, server_side=False)` 原地升级；关键点是升级前必须保证旧 transport 上的缓冲数据清空，否则明文/密文边界错乱。3) 为什么说"握手放线程池"只是兜底？——`run_in_executor` 能救 loop 但引入线程切换成本与连接生命周期管理复杂度，且 CPU 密集的私钥运算在线程池里受 GIL 约束（OpenSSL 会释放 GIL，尚可），长期方案仍是原生异步客户端 + 会话复用。

## 背诵要点
- 同步 ssl 握手是阻塞调用集，放协程里独占 loop、全服务排队；正确路径是 asyncio.open_connection / loop.start_tls，底层 sslproto 状态机处理 Want* 异常。
- 非阻塞握手要自驱状态机：SSLWantRead/WriteError 表示等对应方向就绪再调，读会话里也可能要写，手写易错。
- 握手成本账：TLS1.3 一次 RTT、每请求新连接不开 session 复用会被私钥运算拖垮 P99；监控靠 slow callback >100ms 告警。

## 复盘追问
- 你们异步服务里还有哪些"同步库残留"？当时怎么发现的？（提示：py-spy 看 loop 线程栈里是否出现 ssl/requests 帧配合 slow callback 日志，见 Q5565/Q6010）
- 对必须用同步客户端的存量依赖，你们的兜底是线程池还是进程池？边界怎么划？（提示：释放 GIL 的 C 库用线程池、纯 Python 重逻辑用进程池，配 Q5506 背压）
