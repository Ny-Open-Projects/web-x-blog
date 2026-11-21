class A:
    __slots__ = ("a",)

class B:
    __slots__ = ("b",)

class Empty:
    __slots__ = ()

if __name__ == "__main__":
    try:
        class C(A, B):                    # 两个非空 slots 布局冲突
            __slots__ = ("c",)
        print("unexpected success")
    except TypeError as e:
        print("layout conflict:", e)

    class D(A, Empty):                    # 空 slots 可混入
        __slots__ = ("d",)
    d = D()
    d.a, d.d = 1, 2
    print("D fields ok:", d.a, d.d)
    try:
        d.e = 3
    except AttributeError as e:
        print("no dict:", e)
