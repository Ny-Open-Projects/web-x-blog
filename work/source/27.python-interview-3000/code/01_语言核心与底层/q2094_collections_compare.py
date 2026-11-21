"""collections 容器的比较语义:namedtuple、deque 与 Counter。"""
import collections
import sys

Point = collections.namedtuple("Point", ["x", "y"])
Vec = collections.namedtuple("Vec", ["x", "y"])


if __name__ == "__main__":
    print("namedtuple 按元组比较,字段名不参与:", Point(1, 2) == Vec(1, 2) == (1, 2))
    print("位置参与比较:", Point(1, 2) == Point(2, 1))

    d1 = collections.deque([1, 2, 3])
    d2 = collections.deque([1, 2, 3])
    print("deque 与 deque:", d1 == d2, "| deque 与 list:", d1 == [1, 2, 3])

    c1 = collections.Counter(a=2, b=0)
    c2 = collections.Counter(a=2)
    print("3.9 的 Counter 沿用 dict 语义,零计数参与:", c1 == c2, "|", c1 == {"a": 2})

    if sys.version_info >= (3, 10):
        print("3.10+ 缺失视为零计数:", c1 == c2,
              "| 多重集合比较:", collections.Counter(a=1) <= collections.Counter(a=1, b=2))
    else:
        try:
            c1 < c2
        except TypeError:
            print("3.9 没有 Counter 的 < 比较:TypeError,3.10 才补齐")
