import sys

if __name__ == "__main__":
    a, b = int("1000"), int("1000")
    print("dynamic 1000, a is b:", a is b)          # False:超缓存范围
    s1, s2 = int("256"), int("256")
    print("dynamic  256, is:", s1 is s2)            # True:小整数缓存 -5..256
    print("None/True/False 单例:", None is None, True is True, False is False)
    sentinel = object()
    print("哨兵用 is:", sentinel is sentinel, "| 不同哨兵:",
          object() is object())
    p1 = sys.intern("hello_world_case")
    p2 = sys.intern("hello_world_case")
    print("intern 后 is:", p1 is p2)
    print("结论: 值比较一律 ==, is 只用于单例与哨兵")
