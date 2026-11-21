import cProfile
import io
import pstats
import timeit

def slow_parts():
    total = 0
    for i in range(200_000):
        total += len(str(i))     # 字符串转换是热点
    data = [x for x in range(100_000)]
    return total, len(data)

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    slow_parts()
    profiler.disable()

    buf = io.StringIO()
    stats = pstats.Stats(profiler, stream=buf).sort_stats("tottime")
    stats.print_stats(3)
    print(buf.getvalue()[:600])

    cost = timeit.timeit("'-'.join(str(n) for n in range(1000))", number=100)
    print(f"join version: {cost:.4f}s for 100 runs")
