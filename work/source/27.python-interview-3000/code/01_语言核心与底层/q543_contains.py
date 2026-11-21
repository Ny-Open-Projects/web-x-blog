import time

class SlowRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return iter(range(self.n))        # 没有 __contains__:in 走全量迭代

class FastRange(SlowRange):
    def __contains__(self, x):
        return 0 <= x < self.n            # 结构化判定:O(1)

if __name__ == "__main__":
    sr, fr = SlowRange(10_000_000), FastRange(10_000_000)

    start = time.perf_counter()
    _ = 9_999_999 in sr
    print("iter-based:", round(time.perf_counter() - start, 4), "s")

    start = time.perf_counter()
    _ = 9_999_999 in fr
    print("structured:", round(time.perf_counter() - start, 6), "s")
