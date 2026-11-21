"""cProfile 热点定位(纯标准库)。"""
import cProfile
import hashlib
import io
import pstats
import random


def slow_hash(n):
    return [hashlib.sha256(str(i).encode()).hexdigest()[:8] for i in range(n)]


def slow_sort(n):
    data = [random.random() for _ in range(n)]
    data.sort()
    return len(data)


profiler = cProfile.Profile()
profiler.enable()
slow_hash(20000)
slow_sort(20000)
profiler.disable()

buf = io.StringIO()
pstats.Stats(profiler, stream=buf).sort_stats("tottime").print_stats(4)
print("\n".join(buf.getvalue().splitlines()[:14]))
