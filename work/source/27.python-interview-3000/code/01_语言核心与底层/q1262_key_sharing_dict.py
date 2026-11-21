import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    p1, p2 = Point(1, 2), Point(3, 4)
    plain = {"x": 1, "y": 2}
    print("instance __dict__ sizeof:", sys.getsizeof(p1.__dict__))
    print("literal dict     sizeof:", sys.getsizeof(plain))
    print("same keys object layout:", p1.__dict__.keys() == p2.__dict__.keys())
    p1.z = 9                       # 分叉:仅 p1 脱离共享键
    print("after divergence keys still align:", p1.__dict__.keys() == p2.__dict__.keys())
    print("p2 untouched:", p2.x, p2.y)
