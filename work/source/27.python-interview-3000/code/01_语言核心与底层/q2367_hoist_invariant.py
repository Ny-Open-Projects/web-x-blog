"""循环不变量外提:把与循环变量无关的计算移出循环。"""
import timeit


def slow(rows, factor, offset):
    total = 0
    for value in rows:
        total += value * (factor + offset) / len(rows)   # 不变量每圈重算
    return total


def fast(rows, factor, offset):
    scale = (factor + offset) / len(rows)                # 一次算好
    total = 0
    for value in rows:
        total += value * scale
    return total


if __name__ == "__main__":
    rows = list(range(1000))
    print("结果一致:", slow(rows, 2, 1) == fast(rows, 2, 1))

    t_slow = timeit.timeit(lambda: slow(rows, 2, 1), number=2000)
    t_fast = timeit.timeit(lambda: fast(rows, 2, 1), number=2000)
    print(f"未外提: {t_slow:.3f}s | 外提后: {t_fast:.3f}s")

    def build(n):
        out = []
        push = out.append        # 方法查找也是不变量
        for i in range(n):
            push(i)
        return out

    print("绑定方法后:", len(build(100)))
