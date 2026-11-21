"""读多写多本地缓存的刷新策略: 后台定时刷新让读者永远不等"""
import threading
import time

# 模拟一个慢配置源: 读取要 15 ms
SOURCE = {"rate": 1.0, "version": 1}

def load_from_source():
    time.sleep(0.015)
    return dict(SOURCE)

INTERVAL = 0.05
READS = 30

def run_blocking_mode():
    cache = load_from_source()
    loaded_at = time.monotonic()
    max_lat = 0.0
    for i in range(READS):
        if time.monotonic() - loaded_at > INTERVAL:      # 读者自己发现过期, 自己扛刷新
            cache = load_from_source()
            loaded_at = time.monotonic()
        t0 = time.monotonic()
        _ = cache["rate"]                                 # 读操作本体
        max_lat = max(max_lat, time.monotonic() - t0)
    return max_lat

def run_background_mode():
    box = {"cache": load_from_source()}
    stop = threading.Event()

    def refresher():                                      # 后台线程独扛刷新
        while not stop.is_set():
            time.sleep(INTERVAL)
            box["cache"] = load_from_source()             # 原子替换引用, 读者无感知
    th = threading.Thread(target=refresher)
    th.start()
    max_lat = 0.0
    for i in range(READS):
        t0 = time.monotonic()
        _ = box["cache"]["rate"]                          # 永远只碰现成的快照
        max_lat = max(max_lat, time.monotonic() - t0)
    stop.set()
    th.join()
    return max_lat

lat_sync = run_blocking_mode()
lat_bg = run_background_mode()
print("读多写多配置: 读者自刷新模式最大读延迟 %.1f ms" % (lat_sync * 1000))
print("读多写多配置: 后台定时刷新模式最大读延迟 %.3f ms" % (lat_bg * 1000))
print("结论: 读多写少的数据值得养一个后台刷新线程, 用'秒级旧值'换'读者零阻塞';")
print("      刷新用整体替换引用而不是原地改字典, 读者拿到的永远是完整快照")
