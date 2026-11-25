---
title: "[Q5707] Manager.dict 的嵌套陷阱：子项修改不回传"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5707 · Manager.dict 的嵌套陷阱：子项修改不回传

难度：P6 ｜ 标签：multiprocessing.Manager、代理对象、嵌套容器、序列化边界、进程间共享

**问**：用 `Manager().dict()` 跨进程共享状态，主进程里 `d["inner"]["x"] = 2` 改得好好的，子进程读到的却永远是旧值；反过来子进程改嵌套字段，主进程也看不见。顶层赋值没问题，为什么嵌套修改会"静默失效"？代理对象的边界在哪里？正确姿势是什么？

**答**：
结论：`Manager().dict()` 返回的是**代理对象**，只有对代理本身的方法调用（`__setitem__`、`get`、`pop` 等）才会序列化成 RPC 发给 manager 进程执行。`d["inner"]` 返回的不是代理，而是**从远端同步下来的普通本地 dict 副本**；对副本的 `["x"] = 2` 是纯本地内存操作，永远不会有第二次 RPC，修改随副本一起消散。这就是"顶层赋值生效、嵌套修改失效"的根源：代理边界止步于第一层。list/set 同理，嵌套一层的容器全部是本地副本。

取舍：a) 正确姿势一：**整体替换**——先 `inner = dict(d["inner"])` 取回、修改、再 `d["inner"] = inner` 整体赋值走代理，数据量不大时最简单；b) 正确姿势二：**保持扁平**——用复合 key（`f"{user}:{field}"`）把嵌套结构压平成一维，所有修改都走代理；c) 正确姿势三：嵌套结构也用 Manager 容器（`d["inner"] = mgr.dict({...})`），让嵌套对象本身也是代理，但每层访问都是 RPC，成本陡增；d) 数据大或更新频繁时，Manager 每次操作一个往返（pickle + socket）不划算，应改用 `multiprocessing.shared_memory`/`Value` 或消息队列，Manager 只适合低频、结构化的元数据；e) Manager 还有可见性时序问题：读到的永远是"最近一次同步"的快照，别拿它做自旋等待的同步原语。

实战：事故形态是"多进程爬虫用 Manager.dict 存 per-domain 统计 `stats[d]['ok'] += 1`，跑了一整天对账发现计数全是 1（每进程第一层赋值后全是本地副本自嗨）；把计数改成扁平 key `stats[f'{d}:ok']`，所有 += 走代理后账目恢复"。下面复现失效与两种修复。

```python
import multiprocessing as mp


def reader(d, tag):
    print(f"[{tag}] 子进程读到的 inner:", dict(d.get("inner", {})))


if __name__ == "__main__":
    with mp.Manager() as mgr:
        d = mgr.dict()
        d["inner"] = {"x": 1}          # 赋值：整体序列化到 manager，OK
        d["inner"]["x"] = 2            # 修改的是同步下来的本地副本！
        print("[父进程] 本地视角 inner:", d["inner"])
        p = mp.Process(target=reader, args=(d, "坏姿势"))
        p.start()
        p.join()

        inner = dict(d["inner"])       # 正确姿势：先取回整体
        inner["x"] = 3
        d["inner"] = inner             # 再整体赋值，走代理序列化
        p2 = mp.Process(target=reader, args=(d, "好姿势"))
        p2.start()
        p2.join()
```

**追问一**：`d["inner"] = mgr.dict({...})` 让嵌套层也变代理，为什么不推荐？—— 代理是逐次 RPC：读 `d["inner"]["x"]` 是"先从 manager 取 inner 代理引用，再对它发一次 get RPC"，两次网络往返加两次 pickle。嵌套三层时一次业务读取可能六次往返，写操作还有锁竞争；且嵌套代理的引用传递（把代理作为参数传给另一个进程）容易让代码陷入"看似本地操作实则远程调用"的迷宫。Manager 的定位是低频元数据共享，高频数值走 `Value`/`shared_memory`，高频消息走队列。

**追问二**：这个坑和 pickle 序列化的"部分复制"有什么共同本质？—— 都发生在**边界处做了浅拷贝**：代理边界只覆盖顶层方法调用，pickle 只序列化对象图快照。共同教训是：跨边界（进程/序列化/网络）传递复杂对象时，边界内看到的永远是副本或快照，对副本的修改没有回到原点的通道。工程规则是"跨边界结构尽量扁平、不可变，或显式声明同步协议"，凡是"改了嵌套字段以为共享生效"的代码，都要在 review 时按边界审计。

## 背诵要点
- 代理边界止步顶层：`d["inner"]` 返回本地副本，嵌套修改是纯本地操作，静默不回传。
- 三种修复：整体取回-改-赋回、扁平复合 key、嵌套层也用 Manager 容器（代价是逐层 RPC）。
- Manager 是低频元数据方案（每次操作一次往返）；高频计数/大块数据走 Value/shared_memory/队列。

## 复盘追问
- 为什么顶层赋值生效而 `d["inner"]["x"] += 1` 不生效？（前者走代理 RPC，后者改的是本地副本）
- per-domain 计数跑一天全是 1，怎么改最省事？（扁平 key：stats[f"{d}:ok"]，每次自增走代理）
