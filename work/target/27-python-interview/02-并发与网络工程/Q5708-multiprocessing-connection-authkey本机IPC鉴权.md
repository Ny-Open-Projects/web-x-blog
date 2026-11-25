---
title: "[Q5708] multiprocessing.connection：authkey 握手与本机 IPC 鉴权"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5708 · multiprocessing.connection：authkey 握手与本机 IPC 鉴权

难度：P6 ｜ 标签：multiprocessing.connection、Listener、Client、authkey、HMAC、本机 IPC

**问**：本机两个 Python 进程要传命令和结构化数据，裸 socket 要自己定协议，`multiprocessing.Queue` 只能单向队列。`multiprocessing.connection` 的 `Listener/Client` 是什么？`authkey` 在握手里防什么攻击？本机 127.0.0.1 的连接为什么还要认证？消息默认怎么序列化？

**答**：
结论：`Listener` 是服务端监听器（可绑 TCP 地址或 Unix 域 socket），`Client` 是配套客户端；连接建立后两边拿到同一套 `send/recv` 接口，消息自动 pickle（可传任意可序列化对象），`recv` 可以带超时并支持多路复用（`wait()` 可同时等多个 connection）。`authkey` 是**双向 HMAC 挑战应答**：连接建立后服务端发随机 challenge，客户端用 authkey 计算 HMAC 回应，服务端验证；任何一边 key 不匹配都会抛 `AuthenticationError`。它防的是"本机其他用户/进程探测到端口后伪造客户端连进来发命令"——本机 IPC 的威胁模型不是网络窃听，而是同机越权访问，所以 127.0.0.1 也必须认证。

取舍：a) 管理面/控制面通信（主控进程发指令给 worker、守护进程间心跳）适合 Listener/Client：结构化消息 + 认证 + 可多路复用；b) 大流量数据管道不适合：pickle 逐条消息序列化、无背压，仍应走 `Queue`/`shared_memory`；c) `Listener(("127.0.0.1", 0))` 用随机端口方便测试，生产上 Unix 域 socket（`Listener("/tmp/app.sock")`）可加文件权限层防护；d) authkey 要按"对"来发——主控与每个 worker 用不同 key，避免一个 worker 被攻破后 key 可连所有节点；e) `recv()` 无超时会挂死，长连接循环里要 `poll(timeout)` 或 `wait([conn], timeout)`，别裸 recv。

实战：事故形态是"运维面板进程用无认证 TCP 本机端口给 worker 发 reload 指令，某同事的调试脚本扫到端口后照抄消息格式发了一条，worker 直接重载了错误配置；给 Listener/Client 配 authkey 后，伪造连接在握手就被 AuthenticationError 挡掉，协议格式知识不再等于控制权限"。下面演示正确握手与错误 key 被双向拒绝。

```python
import multiprocessing as mp
import multiprocessing.connection as mpc


def server(addr, q):
    with mpc.Listener((addr, 0), authkey=b"kx") as listener:
        q.put(listener.address)
        with listener.accept() as conn:      # 第一次：正确 key
            conn.send(conn.recv().upper())
        try:                                  # 第二次：错误 key
            with listener.accept():
                pass
            q.put("unexpected-ok")
        except mpc.AuthenticationError:
            q.put("server 拒绝错误 authkey")


if __name__ == "__main__":
    q = mp.Queue()
    p = mp.Process(target=server, args=("127.0.0.1", q))
    p.start()
    address = q.get()
    with mpc.Client(address, authkey=b"kx") as client:
        client.send("ping")
        print("[1] 正确 authkey 握手成功:", client.recv())
    try:
        mpc.Client(address, authkey=b"wrong-key")
    except mpc.AuthenticationError as e:
        print("[2] 客户端侧:", type(e).__name__)
    print("[3]", q.get())
    p.join()
```

**追问一**：authkey 握手防得住"同机恶意进程看到消息格式后重放指令"吗？—— 防得住首次伪造连接（没有 key 过不了 HMAC 挑战），但防不住 key 泄漏：恶意进程若拿到 authkey（比如父进程 spawn 子进程时默认继承 `mp.current_process().authkey`，而 key 从未轮换），握手就形同虚设。加固方向：按 worker 生命周期轮换 key、把认证升级为 TLS 双向证书（mTLS）、控制面消息加时间戳 + 序号 + 业务侧幂等，让重放即使过了握手也没有效果。鉴权解决"能不能连"，业务协议解决"连上之后说了算不算"。

**追问二**：`Listener/Client`、`mp.Queue`、`Pipe` 三者怎么选？—— `Pipe`（`Connection` 对象）是 Listener 握手后的产物，只适合两个进程间一条通道；`mp.Queue` 是多生产者多消费者的消息队列，feeder 线程异步投递，适合任务分发但消息无认证、无选择性接收；`Listener/Client` 是"一对多服务端 + 认证 + 双向请求应答 + 多路复用"，天然适合管理面。判据：要不要认证 → Listener/Client；是不是任务队列 → Queue；是不是单通道 → Pipe。管理面用 Listener/Client，数据面用 Queue/shared_memory，别用一个原语硬扛两类需求。

## 背诵要点
- Listener/Client：本机 IPC 的服务端/客户端，消息自动 pickle，`wait()` 支持多路复用，recv 要防挂死。
- authkey 是双向 HMAC 挑战应答，防同机越权连接；防不了 key 泄漏，key 要按对轮换。
- 选型：管理面 Listener/Client（认证+双向），任务分发 Queue，单通道 Pipe。

## 复盘追问
- 127.0.0.1 上的服务为什么也要认证？（威胁是同机越权进程，不是网络窃听；消息格式公开不等于控制权限）
- 调试脚本抄了消息格式就能发 reload，怎么系统性堵住？（authkey 握手 + key 轮换 + 业务层时间戳序号幂等）
