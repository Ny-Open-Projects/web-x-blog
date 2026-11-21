---
title: [Q5501] 3.13 子解释器与 PythonRunner：PEP 734 的并行模型
date: 2026-11-18
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5501 · 3.13 子解释器与 PythonRunner：PEP 734 的并行模型

> 难度:★★★ | 标签:PEP 734, 子解释器, 并行

**问**：3.13 把子解释器（PEP 734）带进标准库 `concurrent.interpreters`（3.14 落 `interpreters` 模块），它和 multiprocessing、threading 比，隔离与并行的账怎么算？什么场景值得上子解释器？跨解释器通信为什么只能走 pipes/queues 而不能共享对象？

**答**：结论：子解释器是「**同进程内的轻量隔离执行单元**」——每个解释器有独立的 GIL（3.12 起 per-interpreter GIL，PEP 684），CPU 密集任务可以真并行；但内存不共享，对象不能跨解释器传递，通信只能走显式 channel（`interpreters.Queue`/pipe，传的是 pickle 后的数据或不可变对象）。三方案对账：multiprocessing = 强隔离 + 进程开销 + 全新 GIL，适合重任务但要序列化一切、启动慢（fork 也只是缓解）；threading = 共享内存 + 一个 GIL，IO 并发好、CPU 无并行；子解释器 = 隔离中等（同一进程、同一 fd 表、崩溃仍会带崩整个进程）+ 启动毫秒级 + 独立 GIL，甜点区是「**插件/租户/脚本沙箱跑 CPU 密集且希望比进程轻**」的场景。边界要讲透：模块状态、全局变量、C 扩展的进程级状态（如全局锁的 C 库、signal handler）不隔离——C 扩展如果没按 PEP 684 声明 per-interpreter 支持，在子解释器里导入会失败或行为异常，这是比通信更常见的落地障碍。实战：先查依赖的扩展兼容性（`Py_mod_multiple_interpreters` 槽位），再测「解释器创建 + 导入依赖」的冷启动成本，最后才是业务迁移。

```python
# 基线:Python 3.13(PEP 734 _interpreters)。3.14 为 interpreters 公开模块;
# 3.12 及以下降级:用 multiprocessing.Process 或 threading 替代。
import sys

def cpu_task(n: int) -> int:
    return sum(i * i for i in range(n))

if sys.version_info >= (3, 13):
    import _interpreters  # 3.13 私有入口;3.14 起改为 import interpreters

    interp = _interpreters.create()
    out_q = _interpreters.Queue()
    _interpreters.run_string(interp, f"""
        import _interpreters
        _interpreters.Queue({_interpreters.Queue.send(out_q, {cpu_task(1_000_000)})})
    """.replace("{cpu_task(1_000_000)}", str(cpu_task(0)))) if False else None
    # 上面保持占位以免版本差异;3.14 公开 API 的等价写法:
    # import interpreters
    # interp = interpreters.create()
    # q = interpreters.create_queue()
    # interp.exec("from worker import main; main(q)")
    _interpreters.destroy(interp)
    print("3.13+: 子解释器可用;3.14 用 interpreters 公开 API")
else:
    # 降级路径:多进程拿到真并行,代价是启动与序列化开销
    import multiprocessing as mp
    if __name__ == "__main__":   # macOS/Windows spawn 模式必须加主模块守卫,否则子进程递归导入
        with mp.Pool(2) as pool:
            print(pool.map(cpu_task, [1_000_000, 1_000_000]))
```

**追问**：
1) 为什么子解释器不能直接共享对象？——per-interpreter GIL 的前提是解释器间没有共享的可变对象（否则一个解释器改数据、另一个的 GIL 管不到它，等于无锁竞争）；共享即打破隔离模型，所以官方通道只走 Queue/pipe 的序列化传递，这是设计选择不是实现限制。
2) 子解释器崩溃会怎样？——Python 层异常会被 `run_string` 捕获回主解释器；但 C 层段错误（坏扩展）依然是进程级灾难，隔离强度远低于多进程——选型时「崩溃容忍度」是和「启动成本」同级的一票否决项。
3) 和 free-threading 是什么竞争关系？——都是 CPU 并行方案：free-threading 共享内存但要自己管锁；子解释器隔离免费但要序列化通信。数据可分区、通信少（map-reduce 形态）→ 子解释器；共享状态密集 → free-threading + 锁改造；生态不兼容两者时 → multiprocessing。
