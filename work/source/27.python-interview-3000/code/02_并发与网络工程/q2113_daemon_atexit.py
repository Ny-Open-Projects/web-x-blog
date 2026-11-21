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
