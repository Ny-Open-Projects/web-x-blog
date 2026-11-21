"""观察者与回调注册表:注册、退订、错误隔离与生命周期。"""
import gc
import weakref


class CallbackRegistry:
    def __init__(self):
        self._callbacks = {}

    def register(self, callback):
        token = object()
        self._callbacks[token] = callback
        return token

    def unregister(self, token):
        return self._callbacks.pop(token, None) is not None

    def emit(self, event):
        for token, cb in list(self._callbacks.items()):
            try:
                cb(event)
            except Exception as exc:      # 隔离:记录但继续派发
                print(f"    回调 {cb.__name__} 出错: {exc}")

    def __len__(self):
        return len(self._callbacks)


if __name__ == "__main__":
    reg = CallbackRegistry()
    t1 = reg.register(lambda e: print("    观察者A 收到", e))
    t2 = reg.register(lambda e: 1 / 0)
    t3 = reg.register(lambda e: print("    观察者C 收到", e))

    print("注册数量:", len(reg))
    reg.emit("ping")
    print("退订 A:", reg.unregister(t1), "| 重复退订:", reg.unregister(t1))
    reg.emit("pong")

    class Listener:
        def __call__(self, e):
            print("    弱观察者收到", e)

    listener = Listener()
    ref = weakref.ref(listener)
    reg.register(listener)
    del listener
    gc.collect()
    print("注册表强引用让已弃对象仍存活:", ref() is not None)
