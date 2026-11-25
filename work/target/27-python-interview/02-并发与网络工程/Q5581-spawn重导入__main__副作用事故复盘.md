---
title: "[Q5581] spawn 重导入 __main__ 副作用的事故复盘"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5581 · spawn 重导入 __main__ 副作用的事故复盘

难度：★★★★☆ ｜ 标签：multiprocessing / spawn / 事故复盘 / __main__ 守卫

**问**：一段脚本在 Linux 开发机上正常，部署到 macOS 容器后每次启动：监听 socket 被创建两次、DB 连接数翻倍、日志打两份。为什么 spawn 启动方式会导致模块级代码"再跑一遍"？正确的工程护栏是什么？

**答**：
- **结论**：macOS 从 3.8 起默认 start method 是 **spawn**（Linux 默认 fork）。spawn 启动子进程 = 新开解释器 + **重新 import 主模块**（`__main__` 会以 `__mp_main__` 名字重新执行一遍）来还原目标函数的代码上下文。模块级的副作用代码——建 socket、建连接池、写日志、读配置——全部会在每个子进程里再执行一次。护栏是所有进程启动入口必须包在 `if __name__ == "__main__":` 守卫里：spawn 的 re-import 时 `__name__` 是 `__mp_main__`，守卫块被跳过。
- **取舍**：fork 继承内存镜像没有重导入问题，但有线程锁继承、fd 状态污染等另一类风险（3.14 起默认策略也在向 forkserver 演进，另见 Q5535）；spawn 更安全但代价是"主模块必须可安全导入"。所以不能靠"换回 fork"回避问题，而要保证模块导入无副作用——这也是"业务逻辑放函数/类、进程入口放守卫"这条分层纪律的由来。
- **实战**：复盘清单：1）把模块级初始化移进 `main()` 或延迟初始化；2）子进程入口目标函数放**可导入模块**而不是脚本顶层（spawn 要 pickle 目标函数的引用）；3）临时文件/全局注册类对象在 re-import 下会重复创建，跨进程共享的用 initializer 传参而不是模块级全局；4）CI 加一条"模块导入幂等"冒烟测试（`python -c "import module; import module"` 观察 stdout 副作用）。

```python
"""spawn 会重执行模块级代码：__main__ 守卫是唯一护栏（macOS 默认 spawn）"""
import multiprocessing as mp

# 模块级副作用演示：spawn 子进程会再执行一次这行（以 __mp_main__ 身份）
print(f"[module-level] name={__name__} （fork 下子进程不打印；spawn 下子进程会打印）")

def worker(q):
    q.put(f"child sees name={__name__}")

if __name__ == "__main__":                       # 守卫：spawn re-import 时 __name__ != __main__
    ctx = mp.get_context("spawn")                # 显式声明，跨平台行为一致
    q = ctx.Queue()
    p = ctx.Process(target=worker, args=(q,))
    p.start()
    print("parent got:", q.get())
    p.join()

    # 反面确认：无守卫的目标写在脚本顶层时，spawn 无法 pickle（报错或重复执行）
    # 正确姿势：target 必须是可导入模块里的函数，而不是交互式/脚本顶层闭包
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=2, mp_context=ctx) as ex:
        results = list(ex.map(abs, [-1, -2, -3]))
        print("pool ok:", results)
```

**追问链**
1. spawn 重导入时 `__main__` 变成了什么？`if __name__ == "__main__"` 为什么恰好能挡住？
   1. 子进程把主模块源码以 `__mp_main__` 名字执行一遍并把它注册进 sys.modules；守卫判断的正是 `__name__`，re-import 时为 `__mp_main__`，初始化块被跳过；而 target 函数通过 pickle 的引用规则从 `__mp_main__` 里取回定义。
   2. 追问：为什么 `lambda` 和嵌套函数不能做 spawn 的 target？——pickle 序列化的是"模块路径 + 限定名"，lambda/闭包没有限定名，spawn 模式直接 PicklingError。
2. forkserver 模式怎么同时规避 fork 与 spawn 的两个坑？
   1. forkserver 预先启动一个"干净的服务器进程"（只导入需要的模块），每次 fork 都从这个无线程、无副作用状态的进程分叉——既避开"fork 继承脏状态"，也没有"重执行主模块副作用"；代价是多一层进程与首启延迟。
   2. 追问：什么情况下 forkserver 反而慢？——任务极短、进程创建占比高时，forkserver 的每次 fork 仍要走 IPC 与页表复制，远不如线程池；短任务应整体换并发模型而不是调 start method。

## 背诵要点
- macOS/Windows 默认 spawn：子进程重导入主模块（__main__ → __mp_main__），模块级副作用全部重复执行。
- 唯一护栏：入口包 `if __name__ == "__main__":`；target 必须是可导入模块的具名函数，lambda/闭包不可 spawn。
- forkserver = 从干净进程 fork，兼顾安全与无重导入；3.14 起 macOS 默认向 forkserver 演进。

## 复盘追问
- 如何系统性排查代码库里"模块级副作用"？AST 扫描哪些调用模式？
- 双倍日志/双倍连接的事故里，监控上最早可发现的信号是什么？
