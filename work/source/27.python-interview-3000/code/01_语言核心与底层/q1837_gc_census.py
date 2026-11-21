"""gc.get_objects 普查:按类型统计定位堆积。"""
import gc
from collections import Counter


def census():
    return Counter(type(o).__name__ for o in gc.get_objects())


def growth(before, after, top=5):
    diff = Counter(after)
    diff.subtract(before)
    return diff.most_common(top)


if __name__ == "__main__":
    gc.collect()
    before = census()
    leak = []
    for i in range(500):
        leak.append({"i": i, "tags": [str(i)]})   # 制造 dict 与 list 堆积
    after = census()
    print("当前对象数 Top5:", before.most_common(5))
    top = growth(before, after)
    print("增量最大的类型:", top)
    dict_growth = dict(top).get("dict", 0)
    print("dict 增量 >= 500:", dict_growth >= 500)
    del leak
    gc.collect()
    print("清理后 dict 普查回落:", census()["dict"] <= after["dict"])
