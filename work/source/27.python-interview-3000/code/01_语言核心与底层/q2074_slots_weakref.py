"""__slots__ 类默认不能被弱引用:__weakref__ 槽要显式声明。"""
import weakref


class NoWeak:
    __slots__ = ("x",)             # 没有 __weakref__ 槽

    def __init__(self, x):
        self.x = x


class WithWeak:
    __slots__ = ("x", "__weakref__")   # 显式声明弱引用槽

    def __init__(self, x):
        self.x = x


if __name__ == "__main__":
    a = NoWeak(1)
    try:
        weakref.ref(a)
    except TypeError as e:
        print("无 __weakref__ 槽:", e)

    b = WithWeak(1)
    r = weakref.ref(b)
    print("声明槽后可弱引用:", r() is b)
    del b
    print("对象销毁后弱引用失效:", r() is None)
    print("普通类不受影响:实例天生带着隐式的 __weakref__ 结构")
