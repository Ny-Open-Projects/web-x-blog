import timeit

setup = "parts = ['chunk-%d' % i for i in range(2000)]"

plus = timeit.timeit(
    "s = ''\nfor p in parts:\n    s += p", setup, number=100)
join = timeit.timeit(
    "s = ''.join(parts)", setup, number=100)
print(f"+= loop : {plus*10:.1f} ms per 1000 iters")
print(f"join    : {join*10:.1f} ms per 1000 iters")

# 破坏唯一引用条件,+= 优化失效:先留一个别名
bad = timeit.timeit(
    "s = ''\nalias = s\nfor p in parts:\n    s += p", setup, number=100)
print(f"+= with alias: {bad*10:.1f} ms per 1000 iters  <- 优化失效,退化为 O(n^2)")
