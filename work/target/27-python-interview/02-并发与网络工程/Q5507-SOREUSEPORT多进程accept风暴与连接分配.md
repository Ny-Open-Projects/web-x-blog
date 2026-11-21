---
title: [Q5507] SO_REUSEPORT 多进程 accept 风暴与连接分配
date: 2026-11-18
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5507 · SO_REUSEPORT 多进程 accept 风暴与连接分配

> 难度:★★★ | 标签:SO_REUSEPORT, 惊群, 多进程

**问**：多进程服务用 SO_REUSEPORT 让每个 worker 各自 bind 同一端口，和「父进程监听 + 子进程 accept」比，连接是怎么分配的？为什么会出现 accept 风暴/连接倾斜？内核哈希分配有什么坑，怎么在应用层补救？

**答**：结论：SO_REUSEPORT 模式下每个 worker **独立 socket 各自 listen**，内核对新建连接按**四元组哈希**选 worker——不是按负载，是按哈希！三个后果：1) **无惊群但也不负载均衡**：哈希保证一条连接只唤醒一个 worker（对比无 REUSEPORT 时 accept 惊群），但长连接时代 worker 间连接数可能严重倾斜（哈希分布 + 每连接生命周期不同），热点 worker 打满、其它闲置；2) **restart 缝隙**：滚动重启时新旧进程都要持有 REUSEPORT 才无缝（Q692 的接力场景），老进程退出瞬间它「名下」的连接哈希桶变化，正在 accept 的队列若无 takeover 会丢；3) **内核版本坑**：3.9 才引入；Linux 4.5+ 才有 `SO_REUSEPORT` + `SO_ATTACH_REUSEPORT_CBPF/EBPF` 支持**按 CPU/负载选桶**——不用 EBPF 修不了分配倾斜，只能应用层补救。应用层补救三板斧：a) 接受倾斜，靠 worker 无状态 + 全局均衡层（LB 层再哈希）；b) 改回「父监听 + fork 共享 fd」模式（天然队列共享、真负载均衡，代价是惊群由内核 mutex 化解、多一次 fd 共享复杂度）；c) EBPF `bpf_sk_reuseport` 按连接数选桶（Nginx/Envoy 的高阶玩法）。Python 侧注意：每个 worker 要**各自创建 socket 并 bind**（fd 不能跨进程复用同一 socket 再 REUSEPORT），`SO_REUSEADDR` 是另一回事，两个选项要同时配。

```python
# 基线:Linux 3.9+(SO_REUSEPORT)。macOS 支持 REUSEPORT 但语义略异(负载均衡版);
# Windows 缺库降级:用父进程监听+多进程共享 fd 或 WSL。
import os, socket, sys

def worker_listen(port: int) -> socket.socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # 解决 TIME_WAIT 重绑
    if hasattr(socket, "SO_REUSEPORT"):
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # 多进程各绑同端口
    s.bind(("0.0.0.0", port))
    s.listen(512)
    return s

if os.name != "nt" and hasattr(socket, "SO_REUSEPORT"):
    s = worker_listen(19007)
    print(f"pid={os.getpid()} listening, kernel hash 决定哪条连接到本进程")
    s.close()   # 演示即关;真实服务在 worker 主循环 accept
else:
    print("无 SO_REUSEPORT:改父进程 listen + fork/进程池共享 accept")

if sys.platform == "linux":
    print("倾斜治理:Linux 4.5+ 可用 SO_ATTACH_REUSEPORT_EBPF 按负载选桶")
```

**追问**：
1) 和 Nginx/uvicorn 的多 worker 是一种模式吗？——uvicorn/gunicorn 的 worker 若各自 bind（REUSEPORT 模式）就是本卡模型；若用 gunicorn 的「master bind + worker 继承 fd」则是共享 accept 队列模型。两者 uvicorn 都支持，`--reuse-port` 开关决定走哪条，倾斜排查先确认是哪种。
2) 哈希倾斜怎么量化？——每 worker 打点当前连接数与 QPS，看 max/min 比值：短连接服务哈希分布接近均匀（大数定律），长连接（WebSocket/SSE）倾斜随连接生命周期随机累积，比值 >2 就该治理；根治只有 EBPF 或换共享 fd 模式。
3) 为什么 REUSEPORT 下 worker 崩溃不丢已 accept 的连接但可能丢 backlog？——已建立连接在各自 socket 上，worker 死则该 socket 的连接被内核 RST（连接跟着 socket 走）；未 accept 的 backlog 也随 socket 消亡——所以「无缝重启」必须新旧并存窗口内老进程先停收新连、排空存量（见 Q692/Q2691）。
