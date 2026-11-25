---
title: "[Q5718] ResourceWarning：依赖 GC 关闭资源的隐患与确定性关闭"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5718 · ResourceWarning：依赖 GC 关闭资源的隐患与确定性关闭

难度：P6 ｜ 标签：ResourceWarning、GC 关闭、socket 泄漏、with、显式 close、fd 确定性

**问**：忘记 `close()` 的 socket 最后也会被释放，那为什么算 bug？ResourceWarning 什么时候会触发、为什么默认看不见？在 CPython 里"引用计数归零即关闭"和"GC 周期回收关闭"的时机差别会导致什么真实故障？如何把"不确定的关闭"变成确定的？

**答**：
结论：`ResourceWarning` 在**带外部资源的对象被 GC 回收时未显式关闭**触发（socket、文件、subprocess 管道等在 `__del__` 里检查并告警），默认被 warning 过滤器压掉（默认 filter 忽略 ResourceWarning），开启方式：`python -W resource`、`PYTHONWARNINGS=resource` 或 `warnings.simplefilter("always", ResourceWarning)`。它揭示的本质问题是**关闭时机不确定**：CPython 引用计数让"无引用即立即关闭"看似确定，但只要存在**引用环**（self 循环、异常对象持有 traceback 持有帧、缓存表持有），关闭就被推迟到分代 GC 周期——高峰期的分配压力让周期长短不可控，fd 数量在"创建速率 × 回收延迟"窗口内堆积，最终 `Too many open files`（Q5553/Q648）。修复纪律：资源的生命周期绑定到语法块——`with socket`/`with open`/`contextlib.closing`/`ExitStack`（Q1816），让关闭在块退出时同步发生，GC 只负责兜底而不是主路径。

取舍：a) 库作者：资源类实现上下文管理器协议，`__del__` 里对未关闭状态发 ResourceWarning（自证用法）；b) 应用层：CI 里把 ResourceWarning 升级为 error（`-W error::ResourceWarning`）跑一遍用例，泄漏当场爆雷；c) 长生命周期对象持有短生命周期资源（缓存持 socket、单例持文件句柄）：显式管理（借还/池化，Q1284），不要指望 GC；d) 异步资源（asyncio 的 transport/writer）：必须 `await close()`/`wait_closed()`，GC 兜底在 loop 关闭时才跑（Q5210 的 aclosing 同理）；e) fd 泄漏的在线排查：`lsof -p`/`/proc/self/fd` 计数随时间单增即泄漏，结合 objgraph/`gc.get_objects()` 定位持有者（Q5021）。

实战：事故形态是"告警轮询服务每 30 秒对 200 个节点建 socket 探测，异常分支里没有 close（连接失败路径），fd 以每小时几百个的速度累积，两天后 worker 全体 Too many open files；开启 -W resource 后单测复现，统一改为 with 块 + finally close，并加了 fd 计数探针"。下面验证 GC 关闭的警告与确定性关闭。

```python
import gc
import socket
import warnings


def leaky():
    s = socket.socket()          # 无引用后等待 GC 关闭
    s.bind(("127.0.0.1", 0))
    return s


with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always", ResourceWarning)
    s = leaky()
    del s                        # CPython: 引用计数归零, 立即回收并告警
    gc.collect()                 # 环引用兜底: 把周期对象也清掉
    msgs = [str(w.message) for w in caught if issubclass(w.category, ResourceWarning)]
print("[1] 未显式关闭的 ResourceWarning:", msgs)


def closed():
    with socket.socket() as s:   # 确定性关闭: 块退出即 close
        s.bind(("127.0.0.1", 0))
    return "closed"


with warnings.catch_warnings(record=True) as caught2:
    warnings.simplefilter("always", ResourceWarning)
    print("[2] with 块结果:", closed())
    gc.collect()
    print("[3] 显式关闭后 ResourceWarning 数:",
          len([w for w in caught2 if issubclass(w.category, ResourceWarning)]))
```

**追问一**：为什么"CPython 引用计数会立即关闭"这句话在实践里不可靠？—— 引用计数立即回收只在**无环**时成立，而真实代码里环无处不在：对象自引用、容器互相持有、异常的 `__traceback__` 持有全部帧（帧里又引用本地变量持有的资源）、日志 handler/回调注册表引用连接对象。一旦进环，关闭时机交给分代 GC（分配/释放触发的代阈值，Q402），高峰期可能积压数万对象才跑一次 collection——fd 在这窗口里持续增长。另一个反直觉点：引用计数回收发生在**任意时刻**（包括持锁的代码中间），`__del__` 里做复杂清理本身就是坑（Q5051/Q546）。所以工程结论是：GC 是内存的安全网，但**永远不是资源关闭的调度器**。

**追问二**：asyncio 的 socket 为什么连"GC 兜底"都更晚？—— 异步栈里 `transport.close()` 是异步动作：要 flush 写缓冲、发 FIN、等回调，真正的 fd 关闭发生在事件循环的后续迭代。asyncio 的 StreamReader/Writer/transport 若被 GC 回收，`__del__` 只能安排"在 loop 线程里调度关闭"（还要看 loop 是否还活着），连接可能已经堆积而日志只出现 `Task was destroyed but it is pending!` 之类的间接症状。所以异步代码的关闭纪律更严：`writer.close()` + `await writer.wait_closed()` 必须写在 finally 里，task 生命周期结束前完成；探测 fd 计数（`/proc/self/fd` 或 `resource.getrlimit` 对比）作为回归指标进 CI。

## 背诵要点
- ResourceWarning = 资源对象被 GC 回收时未显式关闭；默认被压掉，-W resource / simplefilter 打开，CI 可升级为 error。
- 引用计数的"立即关闭"对环引用失效：环（异常 traceback、回调注册表）让关闭推迟到 GC 周期，fd 堆积引发 Too many open files。
- 修复纪律：with/closing/ExitStack 绑定生命周期；异步资源 close()+wait_closed() 进 finally；fd 计数进监控。

## 复盘追问
- 探测服务两天后 fd 耗尽，怎么定位与修复？（-W resource 复现泄漏分支；with 化 + fd 计数探针）
- 为什么引用计数不等于确定性关闭？（环引用推迟到分代 GC；资源关闭要语法块绑定）
