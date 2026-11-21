# -*- coding: utf-8 -*-
"""子进程 stdout 流式读取: 逐行消费, 不撑爆管道。

- communicate() 一次性收全输出, 长任务会显得"没有进度"且占内存;
- for line in proc.stdout 逐行消费, 时间戳能证明是流式而非批收;
- 子进程必须 -u 或主动 flush, 否则它的库缓冲会让流式变假流式。
"""
import subprocess
import sys
import time

CHILD = r"""
import sys, time
for i in range(5):
    print("event-%d ts=%.2f" % (i, time.monotonic() % 100), flush=True)
    time.sleep(0.15)
print("child-done", flush=True)
"""


def main():
    t0 = time.monotonic()
    proc = subprocess.Popen(
        [sys.executable, "-u", "-c", CHILD],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    for line in proc.stdout:          # 逐行迭代: 一行到了就处理一行
        line = line.rstrip()
        print("%5.2fs  收到: %s" % (time.monotonic() - t0, line))
    proc.stdout.close()
    rc = proc.wait()
    print("退出码:", rc, "| 总耗时: %.2fs" % (time.monotonic() - t0))
    print("相邻两行的到达间隔约 0.15s, 证明流式读取而非最后一次性收全")


if __name__ == "__main__":
    main()
