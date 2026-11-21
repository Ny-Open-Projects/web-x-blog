---
title: [Q1603] SIGHUP 热加载:信号安全与原子替换
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1603 · SIGHUP 热加载:信号安全与原子替换

> 难度:★★★★ | 标签:SIGHUP, 热加载, 信号

**问**:kill -HUP 触发配置热加载,信号处理器里能直接读文件吗?怎么保证读者不看到半截配置?

**答**:信号处理器只做一件事:置位一个标志(Event.set)。处理器运行在主线程的字节码间隙,里面做 IO、加锁、解析都是给未来埋雷;真正的重载在主循环里做。半截配置的防线分两侧:写侧用临时文件加 os.replace 原子上线,读者永远看到完整文件——旧版或新版,没有中间态;读侧把配置对象整体替换,不可变快照一次赋值,工作线程读一次引用就够,无锁无撕裂。还有个冷知识:标准信号不排队,连发两个 SIGHUP 可能合并成一次,Event 语义天然防抖,重载幂等。

```python
# file: code/02_并发与网络工程/q1603_sighup_reload.py
"""SIGHUP 热加载: 信号安全与原子替换。

- 信号处理器只做一件事: 置位标志。重活(读文件、解析)留给主循环,
  处理器里做 IO 是给未来埋雷;
- 配置文件用 tmp + os.replace 原子上线, 读者永远看到完整文件;
- 配置对象整体替换(不可变快照), 工作线程读一次引用就够, 无锁;
- 信号不排队: 连发两个 SIGHUP 可能合并成一次, Event 语义天然防抖。
"""
import json
import os
import signal
import tempfile
import threading
import time

CONFIG_PATH = os.path.join(tempfile.gettempdir(), "q1603_config.json")


def write_config(data):
    tmp = CONFIG_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f)
    os.replace(tmp, CONFIG_PATH)             # 原子替换: 不存在半截文件


class HotReloader:
    def __init__(self):
        write_config({"rate": 10})
        with open(CONFIG_PATH) as f:
            self.current = json.load(f)      # 整体替换的不可变快照
        self.reload_requested = threading.Event()
        self.versions = 0

    def on_sighup(self, signum, frame):
        self.reload_requested.set()          # 信号处理器只置位

    def reload_if_requested(self):
        if self.reload_requested.is_set():
            self.reload_requested.clear()
            with open(CONFIG_PATH) as f:
                self.current = json.load(f)  # 原子引用替换
            self.versions += 1
            return True
        return False


def main():
    reloader = HotReloader()
    signal.signal(signal.SIGHUP, reloader.on_sighup)   # 只能在主线程装

    seen = set()
    stop = threading.Event()

    def worker():
        while not stop.is_set():
            rate = reloader.current["rate"]  # 读一次快照引用, 无锁无撕裂
            seen.add(rate)
            time.sleep(0.02)

    threads = [threading.Thread(target=worker, daemon=True) for _ in range(2)]
    for t in threads:
        t.start()
    time.sleep(0.1)                          # 稳定期: 保证初版配置被采样到
    deadline = time.monotonic() + 2.0
    while time.monotonic() < deadline and 10 not in seen:
        time.sleep(0.02)                     # 确定性同步: 初值确认已被读

    print("初版配置 rate =", reloader.current["rate"])
    for new_rate in (20, 30):
        write_config({"rate": new_rate})
        os.kill(os.getpid(), signal.SIGHUP)  # 自我投递: 模拟运维 kill -HUP
        deadline = time.monotonic() + 2.0
        while time.monotonic() < deadline and not reloader.reload_if_requested():
            time.sleep(0.01)
        # 等工作线程确认采样到这一版, 再进入下一版(否则窗口太窄会被跳过)
        deadline = time.monotonic() + 2.0
        while time.monotonic() < deadline and new_rate not in seen:
            time.sleep(0.02)
        print("热加载后 rate =", reloader.current["rate"])

    stop.set()
    for t in threads:
        t.join(timeout=1)

    print("工作线程见过的 rate 集合:", sorted(seen))
    assert seen == {10, 20, 30}, "三轮配置都应被工作线程看到, 且无中间态"
    assert reloader.versions == 2, "两次 SIGHUP 各完成一次重载"
    print("结论: 信号只当门铃, 重载走主循环; 原子替换让读者永远只见完整配置")


if __name__ == "__main__":
    main()
```

**追问**:1) asyncio 服务里 SIGHUP 怎么处理?——用 loop.add_signal_handler 把信号转成回调,它跑在循环线程里,可以直接 await 重载协程,不用跨线程标志。2) 信号处理器里为什么不能做 IO/加锁?——处理器在主线程字节码间隙异步执行,可能打断「正持有锁/正在 malloc」的代码;IO 在处理器里会与主线程状态交错(重入);唯一安全动作是原子置位——这是 POSIX 信号安全(cfreak: async-signal-safe)在 Python 的投影。3) 「tmp+os.replace」为什么是原子性的关键?——os.replace 是同一文件系统内的 rename,内核保证原子:读者任何时刻 open 只见到旧版或新版;先写后改再 replace 的写法避免了「读半截文件」——与配置热更新(Q707)的快照替换构成两道防线。4) 生产陷阱?——处理器里 print/log(IO);连发信号合并被误当「丢了信号」(Event 置位语义天然幂等,重载逻辑要幂等);asyncio 服务用 signal.signal(阻塞循环,应 add_signal_handler,Q1603 原问);replace 后工作线程仍持旧快照(热更新到生效有延迟,要接受最终一致)。

---
