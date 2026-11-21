---
title: [Q5543] 多进程 IPC 的 pickle 传输税成本账
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5543 · 多进程 IPC 的 pickle 传输税成本账

> 难度:★★★☆ | 标签:multiprocessing, pickle, 成本工程, IPC

**问**：多进程 worker 划分后吞吐不升反降。IPC 的"传输税"由哪几笔成本构成（序列化、拷贝、管道传输）？`multiprocessing.Pipe/Queue` 与 `shared_memory` 各自的适用边界怎么划？如何实测算清这笔账？

**答**：传输税三笔：1) **序列化**：跨进程传对象必须 pickle（Q428/Q5009），`pickle.dumps` 成本随对象图复杂度线性涨（大 list of dict 量级 ~百 MB/s），这是大头；2) **拷贝**：Queue 走 feeder 线程 + 操作系统管道，数据从发送进程用户态→内核→接收进程用户态至少两三次拷贝；3) **同步**：Queue 的锁、feeder 唤醒在消息很小时占主导——**小消息的每条固定税**可能比内容本身还贵。适用边界：进程间只需传"结果/任务"且消息中等大小（KB-MB）、频率 < 万条/秒 → Queue/Pipe 够用；传大块数值数据（图像、矩阵、batch）且要多次访问 → `shared_memory` 零拷贝共享（Q5509），只传元信息；传小而频繁的控制消息 → 优先重新划分进程边界（按批聚合）而不是优化通道。成本账实测法：分别测 `pickle.dumps/loads` 单价、Pipe 往返单价（含 pickle）与 shared_memory 写读单价，除以消息大小得到每 MB 总成本，再乘业务消息速率即 IPC 税占吞吐比。常见复盘结论：把"每条一传"改成"攒批再传"，税直接降一个量级。

```python
# file: code/02_并发与网络工程/q5543_ipc_pickle_tax.py
import multiprocessing as mp
import pickle
import time
import sys

def payload(n_items):
    return [{"id": i, "val": i * 1.5} for i in range(n_items)]

def bench(fn, n=20):
    fn()                                        # 预热
    t0 = time.perf_counter()
    for _ in range(n):
        fn()
    return (time.perf_counter() - t0) / n

def echo(conn):
    try:
        while True:
            conn.send(conn.recv())
    except (EOFError, OSError):
        pass

if __name__ == "__main__":                      # macOS spawn 必须守卫
    print("python:", sys.version_info[:3])

    # 1) 序列化单价: 不同规模的 pickle 成本
    for n in (100, 10_000):
        p = payload(n)
        size = len(pickle.dumps(p))
        t = bench(lambda: pickle.loads(pickle.dumps(p)))
        print(f"{n:>6} 条: {size/1024:.0f} KB/条批, pickle 往返 {t*1000:.1f} ms -> {size/1e6/t:.0f} MB/s")

    # 2) Pipe 往返单价(含传输税): 父子进程逐条互相回显
    parent, child = mp.Pipe()
    proc = mp.Process(target=echo, args=(child,), daemon=True)
    proc.start()
    p = payload(10_000)
    t = bench(lambda: (parent.send(p), parent.recv()))
    print(f"Pipe 往返 10K 条: {t*1000:.1f} ms/次 (序列化+拷贝+传输)")
    parent.close(); proc.join(timeout=1)

    # 3) 攒批收益: 同样 10K 条, 单对象批量序列化 vs 100 条小消息序列化
    def many_small():
        for _ in range(100):
            pickle.loads(pickle.dumps(payload(100)))
    def one_batch():
        pickle.loads(pickle.dumps(payload(10_000)))
    t_small = bench(many_small, n=5)
    t_batch = bench(one_batch, n=5)
    print(f"100 条小消息各自序列化: {t_small*1000:.0f} ms | 攒成 1 批: {t_batch*1000:.0f} ms "
          f"(每条固定税均摊后差距即批收益)")
```

**追问**：1) 为什么 `mp.Queue` 比 `Pipe` 慢还要走 feeder 线程？——Queue 需要在任意进程可安全并发投递（内部锁+buffer+feeder 线程异步 flush，Q5532 的退出挂死也源于此）；Pipe 是单/双工直连，低开销但并发写要自己加锁。2) `shared_memory` 传"引用"时元信息里必须带什么？——名字、shape、dtype（结构化约定）；跨机器不能用（这是与 redis/memcached 的边界），且生命周期要显式管理防孤儿块（Q5509）。3) 如何判断 IPC 税是否已经是瓶颈？——对比"CPU 忙在计算 vs 忙在 pickle"，py-spy 按 `pickle`/`send` 栈帧占比量化，超 20% 就该重划进程边界或攒批。

## 背诵要点
- IPC 税三笔：pickle 序列化（大头）+ 内核拷贝 + 每条消息固定同步开销（小消息最伤）。
- 大块数值数据用 shared_memory 零拷贝只传元信息；中等消息 Queue/Pipe；提频先攒批再传。
- 实测口径：dumps/loads 单价、Pipe 往返单价、每 MB 总成本 × 消息速率 = 税占吞吐比。

## 复盘追问
- 一个多进程图像处理服务吞吐不达标，如何量化 IPC 税并决定走 shared_memory 还是攒批？（提示：先测三类单价，再看消息大小分布与访问次数，>1 次读的批数据才值得共享内存）
- 攒批改造后延迟指标会怎么变？如何给批大小设上限？（提示：延迟 = 排队攒批时间 + 处理时间，批上限按延迟预算与内存水位双重约束）
