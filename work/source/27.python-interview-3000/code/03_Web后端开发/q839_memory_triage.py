import tracemalloc

def gen_batch() -> list:
    return [[i] * 10 for i in range(1000)]

tracemalloc.start()
keep1 = gen_batch()
snap1 = tracemalloc.take_snapshot()
keep2 = gen_batch()
snap2 = tracemalloc.take_snapshot()
diff = snap2.compare_to(snap1, "lineno")
print("当前追踪内存字节:", tracemalloc.get_traced_memory()[0])
print("增长最快的分配点:")
for stat in diff[:2]:
    print(" ", stat.traceback.format()[-1], stat.size_diff)
tracemalloc.stop()
