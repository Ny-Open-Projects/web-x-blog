---
title: "[Q7257] session 夹具被建了四次：pytest-xdist 下 session 作用域的重复实例化"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7257 · session 夹具被建了四次：pytest-xdist 下 session 作用域的重复实例化

难度：P6 ｜ 标签：pytest-xdist、session fixture、进程隔离、共享资源、端口冲突

基线：Python 3.12；用 threading 模拟 4 个 xdist worker 各自实例化 session 级资源，演示端口冲突与文件锁认主修复，全标准库实跑。

**问**：测试套件加 `-n 4` 后提速 3 倍，但"每个测试会话只启动一次"的 session 级夹具（起本地 mock 服务、建共享测试库、初始化全局缓存）开始报端口占用、数据库重复初始化。为什么 scope=session 的夹具在 xdist 下不止跑一次？worker 之间到底共享什么？怎么设计才能既并行又不打架？

**答**：
- **结论**：xdist 的模型是**主进程 + N 个独立 worker 进程**：worker 之间**没有共享内存**，每个 worker 独立加载测试套件、独立执行夹具链。`scope=session` 的"session"是**每个 worker 各自的会话**——4 个 worker 就是 4 次实例化，不存在跨 worker 的 session 单例。所以占固定端口的 mock 服务会被 4 个 worker 抢，写同一个共享文件/数据库会互相踩（Q7193 forked 隔离、Q7066 状态泄漏的同族问题在进程层的放大）。两条出路：① **每 worker 独立资源**：固定值改动态值（端口绑定 0 由 OS 分配、库名/路径带 worker 标识 `os.environ['PYTEST_XDIST_WORKER']`）——大多数场景的正确答案；② **跨 worker 单例**：文件锁认主，第一个 worker 创建资源并登记，其余 worker 等待后复用——只对"资源创建极贵且可复用"成立（如下载的大模型文件、启动一次的重量级容器）。默认按 ① 设计，② 是例外。
- **取舍**：① 独立资源的成本：4 份 mock 服务内存、4 次建库时间（Q7134 xdist 内存配比的账），换来的是零协调；② 共享单例的成本：文件锁的复杂度 + 等待超时的 flaky 风险 + worker 崩溃后的认主重建——只值回票价在"创建要 30s 以上"的资源上；③ 不是所有 session 夹具都该共享：含状态的（缓存预热、随机种子）共享反而引入 worker 间耦合；④ 与 `--forked` 的叠加：进程再加进程，隔离更彻底、重复更彻底，资源成本翻倍前先算账。
- **实战**：① 夹具审查清单加一条：scope=session 的夹具必须回答"在多 worker 下执行几次、每次的成本与副作用"，答不清就降级 scope；② worker 感知资源命名：端口 `socket.bind(('127.0.0.1', 0))` 拿分配值，文件路径拼 worker id；③ 需要跨 worker 传递结果时用文件（xdist 的 worker 间通信受限，文件是简单可靠通道）；④ CI 上把 `-n` 数量与 worker 资源配比一起定（Q7134），别只看总时长。

```python
"""xdist session 夹具重复实例化模拟：端口冲突与两种修复。"""
import socket
import threading
import time
import os


def start_mock_on_fixed_port(port: int, results: list) -> None:
    """反例: 每个 worker 抢同一个固定端口。"""
    try:
        s = socket.socket()
        s.bind(("127.0.0.1", port))
        results.append((threading.current_thread().name, "ok"))
        s.close()
    except OSError as e:
        results.append((threading.current_thread().name, f"端口被占: {e.errno}"))


def start_mock_on_ephemeral(results: list, worker_id: str) -> int:
    """修复1: 绑定端口 0, OS 分配 -> 每 worker 独立端口。"""
    s = socket.socket()
    s.bind(("127.0.0.1", 0))            # 0 = 由 OS 分配空闲端口
    port = s.getsockname()[1]
    s.close()
    results.append((worker_id, f"独立端口 {port}"))
    return port


def shared_resource_with_lock(worker_id: str, lock_path: str,
                              owner: list, ready: threading.Event) -> str:
    """修复2: 文件锁认主 -> 单例资源, 其余 worker 等待复用。"""
    fd = os.open(lock_path, os.O_CREAT | os.O_RDWR)
    try:
        import fcntl
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            if not owner:               # 抢到锁且资源未建 -> 我是 owner
                time.sleep(0.05)        # 模拟创建耗时
                owner.append(worker_id)
                ready.set()
                return f"{worker_id} 创建了资源"
            return f"{worker_id} 抢到锁但资源已存在(异常路径)"
        except BlockingIOError:
            ready.wait(timeout=2)       # 等 owner 建完
            return f"{worker_id} 等待后复用 {owner[0]} 创建的资源"
    finally:
        os.close(fd)


if __name__ == "__main__":
    print("反例: 4 个 worker 抢固定端口 8087")
    res: list = []
    ts = [threading.Thread(target=start_mock_on_fixed_port, args=(8087, res),
                           name=f"worker{i}") for i in range(4)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    for name, r in res:
        print(f"  {name}: {r}")

    print("\n修复1: 每 worker 动态端口")
    res2: list = []
    for i in range(4):
        start_mock_on_ephemeral(res2, f"worker{i}")
    for name, r in res2:
        print(f"  {name}: {r}")

    print("\n修复2: 文件锁认主的共享单例")
    owner: list = []
    ready = threading.Event()
    lock_path = "/tmp/_q7257_lock"
    if os.path.exists(lock_path):
        os.unlink(lock_path)
    outs = []
    ts2 = [threading.Thread(target=lambda i=i: outs.append(
        shared_resource_with_lock(f"worker{i}", lock_path, owner, ready)))
        for i in range(4)]
    for t in ts2:
        t.start()
    for t in ts2:
        t.join()
    for o in outs:
        print(f"  {o}")
    ok = len(owner) == 1
    print(f"校验: 资源只创建一次 -> {'通过' if ok else '异常'}")
    print("\n结论：xdist 的 session = 每 worker 一个; 默认走'每 worker 独立资源',")
    print("      文件锁单例只留给创建昂贵且可复用的资源")
```

**追问一**：worker 之间需要共享测试数据怎么办？

→ 解析：先问真的需要吗——多数"共享数据"需求用**每 worker 相同输入**即可满足：fixture 从共享只读源（git 里的 fixture 文件、对象存储）各自加载一份，worker 间不需要通信，天然安全（fixture 只读原则，Q1085 确定性数据）。真需要"一份可变共享数据"（如全局计数器、同一份数据库）时，用文件作为中介：SQLite 文件库 + 文件锁串行写，或预生成的数据文件每 worker 只读。xdist 官方没有 worker 间直连通道是有意设计：**迫使测试解耦**。如果发现测试套件强依赖跨 worker 通信，先怀疑测试设计——通常说明有隐藏的全局状态（Q7066），该修的是测试本身。

**追问二**：哪些 session 夹具适合降级、哪些必须保住 session 级？

→ 解析：保住 session 级的判据是"创建贵 + 无状态 + 每 worker 一份可接受"：如纯计算型缓存表（每 worker 各算一份，内存换时间）、只读连接池。降级到 function 级的是"有状态的"：临时缓存目录（用例间残留会让并行用例互相污染，Q7066）、可变配置对象。还有一类该**跨 worker 单例化**的：外部重量级依赖（共享测试容器、大模型权重），用文件锁认主或 xdist 的 `--dist loadfile` 分组——把需要同一资源的测试分到同一 worker，资源自然单例化，这是比锁更优雅的调度层解法。审查口诀：session 夹具看三问——多跑几次贵不贵？有状态吗？能按 worker 隔离吗？
