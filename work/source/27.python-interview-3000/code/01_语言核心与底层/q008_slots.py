import sys

class Plain:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Slotted:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == "__main__":
    p = Plain(1, 2)
    s = Slotted(1, 2)
    print(hasattr(p, "__dict__"))  # True
    print(hasattr(s, "__dict__"))  # False
    print(sys.getsizeof(p) > sys.getsizeof(s))  # True

    try:
        s.z = 3
    except AttributeError as e:
        print("cannot add:", e)
