---
title: [Q2113] daemon 线程与 atexit:实测存活窗口里的钩子
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2113 · daemon 线程与 atexit:实测存活窗口里的钩子

> 难度:★★★ | 标签:atexit, daemon, 关闭序列

**问**:daemon 线程注册的 atexit 钩子到底会不会执行?这道题的答案为什么必须实测?

**答**:在 CPython 3.9 上实测,答案是"会":关闭序列先 join 非 daemon 线程,再跑 atexit 钩子,daemon 要到最终化阶段才被杀,所以它注册的钩子仍会执行。

- 退出序列记录显示 main-atexit-ran 与 daemon-atexit-ran 都出现;

- 但 daemon 自身的循环没跑完,daemon-finished 缺席——工作被腰斩;

- 真正的陷阱是时序:钩子执行时 daemon 还在写共享状态,钩子可能观察到中间态;

- 若钩子里去 join daemon 则直接挂死:钩子在等 daemon,daemon 在等钩子跑完;

- 这个存活窗口是实现细节,3.12 用 threading.atexit 把它显式化了。

```python
# file: code/02_并发与网络工程/q2113_daemon_atexit.py
# -*- coding: utf-8 -*-
"""daemon 线程与 atexit: 实测守护线程的存活窗口。

- 3.9 实测: atexit 钩子执行时 daemon 仍存活, 它注册的钩子竟然会执行;
- 但 daemon 自身的工作在最终化阶段被腰斩, 循环半途而废;
- 陷阱在时序: 钩子运行时 daemon 还在写共享状态; 若钩子去 join daemon 则挂死。
"""
import atexit
import os
import tempfile
import threading
import time

log_path = tempfile.mktemp(prefix="q2113_atexit_")


def record(tag):
    with open(log_path, "a") as f:
        f.write(tag + "\n")


def report_reader():
    with open(log_path) as f:
        lines = [ln.strip() for ln in f if ln.strip()]
    print("退出序列中的记录:", lines)
    print("main-atexit-ran 出现:", "main-atexit-ran" in lines,
          "(主线程注册的钩子照常执行)")
    print("daemon-atexit-ran 出现:", "daemon-atexit-ran" in lines,
          "(3.9 实测: atexit 阶段 daemon 仍存活, 钩子被执行)")
    print("daemon-finished 出现:", "daemon-finished" in lines,
          "(daemon 的工作被腰斩, 半途而废)")
    os.remove(log_path)


def main_hook():
    record("main-atexit-ran")


def daemon_hook():
    record("daemon-atexit-ran")   # daemon 注册的钩子


def daemon_body():
    atexit.register(daemon_hook)
    record("daemon-started")
    deadline = time.monotonic() + 2.0
    while time.monotonic() < deadline:    # 长活 daemon, 模拟后台服务
        time.sleep(0.05)
    record("daemon-finished")             # 期望永不出现


def main():
    atexit.register(main_hook)
    t = threading.Thread(target=daemon_body, name="d", daemon=True)
    t.start()
    time.sleep(0.15)   # daemon 已完成注册并写下 started
    # main 返回 -> join 非 daemon -> atexit(LIFO) -> 最终化腰斩 daemon


if __name__ == "__main__":
    atexit.register(report_reader)   # 先注册后执行, 保证最后读取结果
    main()
```

**追问**:1) 为什么"daemon 钩子不执行"的旧说法流传很广?——早期实现与其他运行时行为不同,且关闭序列在版本间调整过,这类问题必须以实测为准。2) atexit 钩子和 finally 块谁先跑?——finally 属于正常的栈展开,先于解释器关闭;atexit 在关闭序列里,进程被信号杀死时两者都可能不执行。3) atexit 钩子执行时的并发风险怎么防?——钩子运行时 daemon 还在跑(Q2113 原问的存活窗口),共享状态可能处于中间态;钩子里只做「读取+落盘」不做「修改+依赖」,或先 set 停止标志再等一小段;钩子里 join daemon 是确定性挂死(钩子等 daemon,daemon 的退出在钩子之后)。4) 「以实测为准」的版本敏感性怎么工程化?——关闭序列在不同 CPython 版本间调整过(3.9 实测钩子会跑、3.12 threading.atexit 显式化);这类行为进 CI 的「行为锁定测试」,升级解释器时先跑;文档不背书「永远如此」。5) 生产陷阱?——在钩子里依赖 daemon 的产物(时序赌注);信号杀死(SIGKILL)时钩子与 finally 都不跑(审计逻辑别指望 atexit);多钩子间的顺序依赖(atexit 按 LIFO 执行,注册顺序即依赖);钩子里再抛异常(被吞,收尾静默失败)。

---
