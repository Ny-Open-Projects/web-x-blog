# -*- coding: utf-8 -*-
"""daemon 线程的退出时机实测: 没人等它, 终被腰斩。

- 主线程返回并不会立刻杀 daemon: 解释器先 join 全部非 daemon 线程;
- 这段等待期里 daemon 还在跑, 但已经没人对它负责;
- 到最终化阶段 daemon 被直接掐断, 停在哪一行算哪一行, final-line 永远缺席。
"""
import atexit
import os
import tempfile
import threading
import time


def writer(path, rounds, interval):
    with open(path, "w") as f:
        for i in range(rounds):
            f.write("line-%d\n" % i)
            f.flush()
            time.sleep(interval)
        f.write("final-line\n")   # 收尾行: 完整跑完才会出现
        f.flush()


def count_lines(path):
    with open(path) as f:
        return len([ln for ln in f if ln.strip()])


def report(daemon_file, normal_file, rounds):
    d = count_lines(daemon_file)
    print("daemon 文件行数: %d / %d, final-line 缺失 -> 被腰斩" %
          (d, rounds + 1))
    print("normal 文件行数: %d / %d, 含 final-line -> 被解释器等完" %
          (count_lines(normal_file), rounds + 1))
    for p in (daemon_file, normal_file):
        try:
            os.remove(p)
        except OSError:
            pass


def main():
    rounds = 30
    daemon_file = tempfile.mktemp(prefix="q2112_daemon_")
    t = threading.Thread(target=writer, args=(daemon_file, rounds, 0.06),
                         name="daemonic-writer", daemon=True)
    t.start()
    time.sleep(0.25)   # daemon 先写上若干行, 主线程提前退场
    print("main 返回时刻 daemon alive:", t.is_alive())
    print("此后解释器还要先等非 daemon 线程, daemon 无人负责但仍可运行")

    normal_file = tempfile.mktemp(prefix="q2112_normal_")
    t2 = threading.Thread(target=writer, args=(normal_file, rounds, 0.005),
                          name="normal-writer")
    t2.start()
    atexit.register(report, daemon_file, normal_file, rounds)


if __name__ == "__main__":
    main()
