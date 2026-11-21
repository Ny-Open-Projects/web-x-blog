import tracemalloc

def allocate_big():
    return [bytes(1024) for _ in range(50)]      # 约 50 KB

if __name__ == "__main__":
    tracemalloc.start()
    before = tracemalloc.take_snapshot()

    keep = allocate_big()                         # 持有引用,模拟泄漏

    after = tracemalloc.take_snapshot()
    for stat in after.compare_to(before, "lineno")[:3]:
        print(stat)
    current, peak = tracemalloc.get_traced_memory()
    print("current KB:", current // 1024, "peak KB:", peak // 1024)
    tracemalloc.stop()
