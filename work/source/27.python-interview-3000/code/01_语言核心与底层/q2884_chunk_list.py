"""列表分块的三种实现对比:切片、islice 与步进生成器。"""
import timeit
from itertools import islice


def chunk_slice(seq, size):
    """切片法:简单直观,每次产生新列表,仅接受序列。"""
    return [seq[i:i + size] for i in range(0, len(seq), size)]


def chunk_islice(iterable, size):
    """islice 法:吃任意迭代器,惰性产出块,流式友好。"""
    it = iter(iterable)
    while True:
        block = list(islice(it, size))
        if not block:
            return
        yield block


def chunk_step(seq, size):
    """步进生成器:仅适合序列,切片语义与切片法一致但惰性。"""
    for i in range(0, len(seq), size):
        yield seq[i:i + size]


if __name__ == "__main__":
    data = list(range(10))
    print("切片法:", chunk_slice(data, 3))
    print("islice 法:", [b for b in chunk_islice(data, 3)])
    print("步进法:", list(chunk_step(data, 3)))

    print("islice 能吃生成器:", [b for b in chunk_islice((x * x for x in range(7)), 3)])
    print("尾部不足一块:", chunk_slice(data, 4))

    t1 = timeit.timeit(lambda: chunk_slice(list(range(10000)), 100), number=50)
    t2 = timeit.timeit(lambda: list(chunk_islice(list(range(10000)), 100)), number=50)
    print(f"1 万元素 50 次:切片 {t1:.3f}s,islice {t2:.3f}s")
