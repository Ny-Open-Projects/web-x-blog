import cProfile
import io
import pstats

def hot_loop(n: int) -> int:
    total = 0
    for i in range(n):
        total += i * i
    return total

profiler = cProfile.Profile()
profiler.enable()
hot_loop(200000)
profiler.disable()
buf = io.StringIO()
pstats.Stats(profiler, stream=buf).sort_stats("cumulative").print_stats(3)
print("\n".join(buf.getvalue().splitlines()[:8]))
