import sys

if __name__ == "__main__":
    a = 100
    b = 100
    print(a is b)        # True,小整数缓存

    c = 257
    d = 257
    print(c is d)        # 交互模式下可能 False,脚本里同一次编译可能 True

    s1 = sys.intern("hello" + "!")
    s2 = sys.intern("hello!")
    print(s1 is s2)      # True,显式驻留

    big = "".join(["x"] * 1000)
    print(sys.getsizeof(big) > 0)  # str 有独立存储
