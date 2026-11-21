"""进程健康自采样: 内存、线程与文件句柄的周期记录(纯标准库)。"""
import resource
import sys
import threading
import time
import os

# ru_maxrss 单位因平台而异: Linux 是 KB, macOS 是字节; 统一换算成 MB
RSS_FACTOR = 1024.0 * 1024.0 if sys.platform == "darwin" else 1024.0


def fd_count():
    """跨平台数打开的文件句柄: macOS 走 /dev/fd, Linux 走 /proc/self/fd。"""
    for candidate in ("/dev/fd", "/proc/self/fd"):
        try:
            return len(os.listdir(candidate))
        except OSError:
            continue
    return -1


def snapshot():
    return {
        "maxrss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / RSS_FACTOR,
        "threads": threading.active_count(),
        "fds": fd_count(),
        "cpu_user": resource.getrusage(resource.RUSAGE_SELF).ru_utime,
    }


samples = []
stop = threading.Event()


def sampler(interval=0.05):
    while not stop.is_set():
        samples.append(snapshot())
        time.sleep(interval)


t = threading.Thread(target=sampler, daemon=True)
t.start()

grower = []                          # 模拟一段会增长内存的工作负载
for round_no in range(4):
    grower.append([0] * 200000)
    time.sleep(0.12)
stop.set()
t.join(timeout=1.0)

print("采样数:", len(samples))
assert len(samples) >= 6
first, last = samples[0], samples[-1]
peak = max(samples, key=lambda s: s["maxrss_mb"])
print("首样本: rss={:.1f}MB threads={} fds={}".format(
    first["maxrss_mb"], first["threads"], first["fds"]))
print("末样本: rss={:.1f}MB threads={} fds={}".format(
    last["maxrss_mb"], last["threads"], last["fds"]))
print("峰值: rss={:.1f}MB".format(peak["maxrss_mb"]))
assert last["maxrss_mb"] >= first["maxrss_mb"]      # ru_maxrss 是峰值水位, 只升不降
assert last["fds"] == first["fds"] or last["fds"] > 0
print("要点: 自采样把 maxrss 只升不降、线程数、句柄数写成时间序列, 内存与句柄泄漏一眼可见")
