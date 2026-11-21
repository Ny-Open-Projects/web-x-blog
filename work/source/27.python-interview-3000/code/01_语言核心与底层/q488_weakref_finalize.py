import weakref

class TempFile:
    pass

def cleanup(name):
    print(f"[finalize] cleaning {name}")

if __name__ == "__main__":
    f = TempFile()
    ref = weakref.finalize(f, cleanup, "tmp123")
    print("alive:", ref.alive)
    del f                          # 对象回收,回调被调用
    print("alive after del:", ref.alive)
    ref()                          # 再次调用:已死,安全 no-op
    print("calling a dead finalizer is safe")

    g = TempFile()
    ref2 = weakref.finalize(g, cleanup, "tmp456")
    ref2()                         # 也可以主动触发并解除注册
    print("alive after manual call:", ref2.alive)
