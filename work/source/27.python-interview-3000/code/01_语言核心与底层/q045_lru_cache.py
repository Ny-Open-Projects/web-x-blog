import functools

@functools.lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

calls = 0

@functools.lru_cache(maxsize=2)     # 容量小,观察淘汰
def slow_square(x):
    global calls
    calls += 1
    return x * x

if __name__ == "__main__":
    print(fib(60), "computed fast thanks to cache")
    print(fib.cache_info())         # hits / misses / maxsize

    for v in (2, 3, 4, 2, 3):
        slow_square(v)
    print("real calls:", calls)     # 2 和 3 被淘汰后重算
    print(slow_square.cache_parameters())

    slow_square.cache_clear()       # 手动清空
    print(slow_square.cache_info())
