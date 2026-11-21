import gc
import os
import resource
import sys

def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024   # macOS 单位 KB

big = [i for i in range(300_000)]     # 模拟父进程持有的共享数据
gc.collect()
gc.freeze()                            # 关键:fork 前冻结,减少 GC 触碰共享对象头
print("parent rss~", round(rss_mb(), 1), "MB")

pid = os.fork()
if pid == 0:
    # 子进程:如果在这里大量 touch 列表元素/增减引用,共享页被逐页私有化
    s = 0
    for x in big[:100_000]:
        s += x                          # 读 + 隐式 INCREF,逐步打破 COW
    print("child touched pages, sum", s)
    os._exit(0)
else:
    os.waitpid(pid, 0)
    print("parent rss after fork:", round(rss_mb(), 1), "MB")
    print("smaps (linux only):", os.path.exists("/proc/self/smaps"))
