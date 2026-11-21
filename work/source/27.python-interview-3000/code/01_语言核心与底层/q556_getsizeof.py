import sys

class Plain:
    pass

class Slotted:
    __slots__ = ("a",)

if __name__ == "__main__":
    print("empty list:", sys.getsizeof([]))
    print("1000-int list:", sys.getsizeof(list(range(1000))))
    print("1000-int tuple:", sys.getsizeof(tuple(range(1000))))

    print("small int:", sys.getsizeof(1), "| big int:", sys.getsizeof(2 ** 100))
    print("plain instance:", sys.getsizeof(Plain()), "| slotted:", sys.getsizeof(Slotted()))

    nested = [list(range(1000))]          # 外层列表只算自己的指针
    print("shallow outer only:", sys.getsizeof(nested))
    print("content is not counted — walk references for deep size")
