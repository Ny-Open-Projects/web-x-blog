---
title: "[Q7193] pytest-forked 测试进程隔离事故复盘"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7193 · pytest-forked 测试进程隔离事故复盘

难度：P6 ｜ 标签：事故复盘、pytest、测试隔离、全局状态

基线：Python 3.12；pytest 7+ / pytest-forked；os.fork 标准库演示。

**问**：测试套件里有几个包装 C 扩展的用例，单跑全过、一起跑就偶发失败：A 用例改了全局配置，B 用例读到被污染的值。已经用了 `pytest-xdist -n 4` 分片，为什么没用？怎么从机制上隔离这类"脏测试"？

**答**：
- **结论**：xdist 的分片单位是"worker 进程"，同一个 worker 里的多个测试仍共享进程内全局状态，所以污染照样发生。`pytest-forked` 的 `--forked` 把**每个测试**放进 fork 出的子进程执行，进程退出时所有全局状态、C 层静态变量随之销毁，天然隔离。它可以和 xdist 叠加（worker 内再逐测试 fork），兼顾并行与隔离。
- **取舍**：fork 有进程创建开销，逐测试 fork 比纯 xdist 慢不少；它治标——真正干净的做法是把全局状态改成依赖注入、让测试自带 setup/teardown。fork 也有副作用：子进程继承父进程的文件描述符和随机数状态，可能出现 fork 后随机种子相同的"双胞胎"问题，需要重新播种。
- **实战**：先定位脏测试并单独隔离（`pytest --forked path/to/dirty_test.py`），不要全套件无脑加；配合 `pytest-randomly` 打乱顺序暴露隐藏依赖；把"单跑过、合跑挂"列为测试规范红线，要求提交前跑全量。

```python
import os
import sys

STATE = ["clean"]  # 模拟被脏测试污染的全局状态


def run_in_fork(name: str, mutate: bool) -> None:
    """每个测试在 fork 出的子进程运行，进程结束即释放全部全局状态。"""
    pid = os.fork()
    if pid == 0:
        if mutate:
            STATE.append("polluted")
        print(f"{name} in child {os.getpid()}: {STATE}")
        sys.stdout.flush()  # os._exit 不 flush，需手动刷出子进程输出
        os._exit(0)
    os.waitpid(pid, 0)


if __name__ == "__main__":
    run_in_fork("test_A", True)
    run_in_fork("test_B", False)
    print("parent 状态:", STATE)  # 仍是 clean，未被子进程污染
```

**追问一**：为什么 xdist 分片不能解决同一个 worker 内的全局状态污染？
→ 解析：xdist 只在 worker 之间隔离进程，一个 worker 会顺序执行分配给它的多个测试，这些测试共享该 worker 的地址空间，所以进程内污染仍会跨测试传播。

**追问二**：fork 隔离有什么隐藏坑？
→ 解析：子进程继承父进程已打开的文件描述符、随机数生成器状态、线程锁等。多线程进程里 fork 还可能因只复制调用线程而导致锁死锁；fork 后应重新播种随机数、避免依赖继承的锁。
