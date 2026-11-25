---
title: [Q7133] multiprocessing spawn 模式下全局状态丢失的事故复盘
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7133 · multiprocessing spawn 模式下全局状态丢失的事故复盘

难度：P6 ｜ 标签：事故复盘 / 多进程 / 工程化

**问**：一个数据预处理脚本在 Linux 服务器上跑得好好的，同事拿到 Mac 上跑就出现：子进程里"配置是空的"、数据库连接对象报 `cannot pickle`、模块顶层的懒加载缓存每次都是 miss。这些现象的共同根因是什么？fork 与 spawn 的差别要怎么在代码里防御？

**答**：
- **结论**：根因是 **spawn 不继承父进程内存**：spawn 是全新启动一个解释器、重新 import 目标模块，再 pickle 传参——所以 ① 模块顶层"顺手"建好的全局配置/连接/懒加载缓存在子进程里全部不存在（fork 是 COW 复制整份内存，看起来"都在"）；② 传给子进程的参数必须可 pickle，数据库连接、锁、打开的文件句柄都会抛错；③ macOS 从 3.8 起 multiprocessing 默认 spawn（安全考虑），Linux 默认 fork——同一份代码跨平台行为不同，这就是"服务器好、本地炸"的典型。防御三板斧：① 顶层模块**零副作用**：连接/配置/缓存一律封装成函数内获取或显式初始化（initializer 参数传给 Pool），不靠 import 时序；② 子进程需要的"全局"通过 `Pool(initializer=setup, initargs=...)` 或函数参数显式传递，且只传可 pickle 的原始数据；③ 主入口必须加 `if __name__ == "__main__":` 守卫——没有守卫的 spawn 会无限递归重新 import 主模块。
- **取舍**：fork 快（无重新 import、共享 COW 内存）但不安全（继承锁状态、fd 状态、与线程组合有死锁风险，PEP 建议 fork+exec）；spawn 慢（每进程重新 import，NumPy/pandas 大模块冷启动可达秒级）但隔离干净。3.12 起官方文档明确：多线程程序中 fork 默认将触发 DeprecationWarning，跨平台库作者必须按 spawn 设计。
- **实战**：① 用 `multiprocessing.get_start_method()` 在 CI 里跑 spawn 矩阵（Q7024 的 nox 多矩阵），别只测 Linux fork；② initializer 里重建连接池而非传连接对象；③ 懒加载缓存要 per-process 一致：spawn 下每个子进程独立缓存（内存多份，容量账 Q7092），不要假设命中率跨进程共享；④ 大参数（如整个 DataFrame）别用 pickle 传，用文件/共享内存传递。

```python
# spawn 语义演示: 子进程修改全局变量对父进程不可见; 传参必须可 pickle
# 基线: Python 3.9+ 标准库; macOS 默认 spawn, Linux 默认 fork
import multiprocessing as mp

_counter = {"value": 0}          # 模块级全局: spawn 下每个进程独立一份


def worker_and_increment(x: int) -> int:
    _counter["value"] += x
    return _counter["value"]


def initializer(state: dict) -> None:
    """正确做法: 全局状态通过 initializer 显式注入, 不依赖 import 时序。"""
    _counter["value"] = state["seed"]


def main() -> None:
    # 证据 1: 全局修改不回传 (fork/spawn 都不可见, spawn 连初始状态都不共享)
    with mp.Pool(1) as pool:
        first = pool.apply(worker_and_increment, (5,))
        again = pool.apply(worker_and_increment, (0,))
    assert first == 5
    assert again == 5, "worker 重新初始化, 全局被重置"  # spawn 每任务新进程
    # 证据 2: initializer 注入的状态在 worker 里可见
    with mp.Pool(1, initializer=initializer, initargs=({"seed": 100},)) as p:
        assert p.apply(worker_and_increment, (5,)) == 105
    # 证据 3: 不可 pickle 对象传参报错 (lambda/连接/锁类)
    lock = mp.Lock()
    try:
        with mp.Pool(1) as p:
            p.apply(lambda: lock)   # lambda 不可 pickle
        raise AssertionError("应抛出")
    except Exception as e:          # pickle.PicklingError / TypeError
        assert "pickle" in type(e).__name__.lower() or \
            "pickle" in str(e).lower(), type(e).__name__
    print("OK: spawn 不继承父进程内存; 全局靠 initializer/参数显式传")


if __name__ == "__main__":   # spawn 无守卫会无限递归 import 主模块
    main()
```

**追问 1**：为什么 macOS 在 3.8 之后把默认启动方式从 fork 换成 spawn？
→ 一句话提示：macOS 系统库（CoreFoundation 等）在 fork 后调用会崩溃/未定义行为，且 fork 与线程组合继承锁状态有死锁风险——spawn 从干净解释器启动规避了整类问题。

**追问 2**：3.13 的 fork+exec 与自由线程对这段代码有什么影响？
→ 一句话提示：`multiprocessing.set_start_method("forkserver")` 或 3.14+ 的 fork+exec 让"fork 的快"与"spawn 的安全"折中；自由线程下 GIL 移除使 fork 继承多线程状态的死锁风险更突出，官方进一步不推荐裸 fork。

## 背诵要点
- spawn = 新解释器 + 重新 import + pickle 传参：全局配置/连接/缓存全部不继承，参数必须可 pickle。
- 防御：模块顶层零副作用、Pool(initializer=...) 显式注入、主入口 `__main__` 守卫（无守卫 spawn 无限递归）。
- macOS 3.8+ 默认 spawn、Linux 默认 fork → CI 用 spawn 矩阵；fork 在多线程下有锁继承死锁风险（3.12+ 文档不推荐）。

## 复盘追问
- 为什么"本地 Mac 好、服务器炸"和"服务器好、本地炸"都可能发生？提示：取决于默认启动方式差异方向——fork 崩在 spawn 没有的继承问题（fd/锁），spawn 崩在 fork 没有的状态缺失，两端行为都不等价于对方。
- initializer 重建连接池和"传连接给子进程"的差别？提示：前者每进程独立 TCP 连接（协议安全），后者是同一 socket 两进程共用 = 串包事故（Q6631 同源问题）。
