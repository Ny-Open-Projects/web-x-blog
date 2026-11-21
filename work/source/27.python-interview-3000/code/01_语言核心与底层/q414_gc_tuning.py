import gc
import time

events = []

def on_gc(phase, info):
    if phase == "start":
        events.append((info["generation"], time.perf_counter()))
    else:
        gen, t0 = events[-1]
        events[-1] = (gen, time.perf_counter() - t0)

gc.callbacks.append(on_gc)

# 制造 0 代压力:大量短命容器
for _ in range(3000):
    {"k": [1, 2, 3]}

gc.callbacks.remove(on_gc)
print("collections triggered:", len(events), "sample:", events[:3])
print("stats per gen:", [(s["collections"], s["collected"]) for s in gc.get_stats()])

# 调优示例:拉低 2 代频率,把全量回收留给低峰期
old = gc.get_threshold()
gc.set_threshold(700, 10, 10000)
print("new thresholds:", gc.get_threshold(), "old:", old)
gc.set_threshold(*old)
