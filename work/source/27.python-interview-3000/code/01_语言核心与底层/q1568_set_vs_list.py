import timeit


def bench(size, reps=2000):
    data = list(range(size))
    needle_in, needle_out = size - 1, -1
    frozen = frozenset(data)
    per_miss = timeit.timeit(lambda: needle_out in data, number=reps) / reps
    per_build = timeit.timeit(lambda: needle_out in set(data), number=reps) / reps
    per_frozen = timeit.timeit(lambda: needle_out in frozen, number=reps) / reps
    per_hit = timeit.timeit(lambda: needle_in in data, number=reps) / reps
    return per_miss, per_build, per_frozen, per_hit


if __name__ == "__main__":
    for size in (8, 100, 5000):
        per_miss, per_build, per_frozen, per_hit = bench(size)
        print("n=%5d: list miss %8.2fus | set built per call %7.2fus | "
              "frozenset ready %6.3fus | list hit %7.2fus"
              % (size, per_miss * 1e6, per_build * 1e6,
                 per_frozen * 1e6, per_hit * 1e6))

    print("结论: 小 n 用 list, 大 n 建一次 set/frozenset 再查")
    print("dict.keys 视图成员检测也是 O(1):", "b" in {"a": 1, "b": 2}.keys())
