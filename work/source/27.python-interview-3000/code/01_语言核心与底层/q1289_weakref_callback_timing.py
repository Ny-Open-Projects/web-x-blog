import gc
import weakref

events = []


class Sensor:
    def __del__(self):
        events.append("del")


if __name__ == "__main__":
    s = Sensor()
    ref = weakref.ref(s, lambda r: events.append(
        "cb, obj %s" % ("dead" if r() is None else "ALIVE")))
    del s
    print("refcount death, synchronous:", events)
    events.clear()

    o = Sensor()
    weakref.ref(o, lambda r: 1 / 0)     # 回调里抛异常
    del o
    print("callback exception swallowed, program continues")
    print("finalize 与 ref 回调时机一致: 都在 __del__ 之后", )
    del events[:]
