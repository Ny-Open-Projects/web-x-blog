# -*- coding: utf-8 -*-
"""优雅停机的三层信号处理: 收敛、强杀、硬退出。

- 第一层 SIGTERM: 置停止位, 停止接活并排干在途任务, 干净退出 0;
- 第二层 SIGTERM: 放弃在途, 走快速放弃路径, 退出 1;
- 第三层 SIGTERM: os._exit(2) 立即走人, 防止任何收尾代码挂住进程。
"""
import os
import signal
import sys
import time


def child_main():
    stop = {"hits": 0, "graceful": False, "force": False}

    def on_term(sig, frame):
        stop["hits"] += 1
        n = stop["hits"]
        if n == 1:
            stop["graceful"] = True
            print("[child] 一层: 停止接活, 开始排干", flush=True)
        elif n == 2:
            stop["force"] = True
            print("[child] 二层: 放弃在途", flush=True)
        else:
            print("[child] 三层: 硬退出", flush=True)
            os._exit(2)                      # 不走任何清理路径

    signal.signal(signal.SIGTERM, on_term)
    signal.signal(signal.SIGINT, on_term)

    while stop["hits"] == 0:                 # 接活阶段
        time.sleep(0.1)

    drained = 0
    for i in range(5):                       # 排干阶段: 每步检查二层
        if stop["force"]:
            break
        time.sleep(0.3)
        drained += 1

    if stop["force"]:
        print("[child] 快速放弃完成, 退出 1", flush=True)
        sys.exit(1)
    print("[child] 排干 %d 步完成, 退出 0" % drained, flush=True)
    sys.exit(0)


def main():
    for layers, expect in ((1, 0), (2, 1), (3, 2)):
        pid = os.fork()
        if pid == 0:
            child_main()
        time.sleep(0.25)                     # 让子进程装好处理器
        for _ in range(layers):
            os.kill(pid, signal.SIGTERM)
            time.sleep(0.06)
        _, status = os.waitpid(pid, 0)
        code = os.waitstatus_to_exitcode(status)
        print("发送 %d 次信号 -> 退出码 %d (期望 %d) %s" %
              (layers, code, expect, "一致" if code == expect else "异常"))
    print("三层语义: 排干收场 / 放弃收场 / 立即硬退")


if __name__ == "__main__":
    main()
