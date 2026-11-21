import gc
import weakref

events = []


class Phoenix:
    def __del__(self):
        events.append("del")
        globals()["keep"] = self        # 复活


if __name__ == "__main__":
    p = Phoenix()
    ref = weakref.ref(p, lambda r: events.append(
        "cb, obj %s" % ("dead" if r() is None else "alive")))
    del p                               # 第一次死亡:__del__ 复活对象
    print("after 1st drop:", events, "| wr alive:", ref() is not None)
    events.clear()
    del keep                            # 第二次真正死亡
    print("after 2nd drop:", events, "| __del__ 不再执行, 回调此刻触发")
    events.clear()
    gc.collect()
    print("PEP 442: 终结器对同一对象最多一次, 复活不可依赖")
