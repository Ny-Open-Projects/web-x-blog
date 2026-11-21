import gc
import inspect
import threading
import weakref


class EventBus:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._topics = {}   # topic -> list[weakref]
        self.errors = []

    @staticmethod
    def _make_ref(callback):
        if inspect.ismethod(callback):
            return weakref.WeakMethod(callback)  # 绑定方法: 跟踪宿主对象
        return weakref.ref(callback)             # 普通函数: 直接弱引用

    def subscribe(self, topic: str, callback) -> None:
        with self._lock:
            self._topics.setdefault(topic, []).append(self._make_ref(callback))

    def _live_callbacks(self, topic: str) -> list:
        with self._lock:
            subs = self._topics.get(topic, [])
            alive, dead = [], []
            for ref in subs:
                cb = ref()          # 探活: 对象已被回收返回 None
                (alive if cb is not None else dead).append((ref, cb))
            if dead:
                self._topics[topic] = [r for r, _ in alive]  # 顺路清尸
            return [cb for _, cb in alive]

    def publish(self, topic: str, event) -> None:
        for cb in self._live_callbacks(topic):
            try:
                cb(event)
            except Exception as exc:            # 单订阅者故障被隔离
                self.errors.append(f"{cb.__name__}: {exc}")


class Subscriber:
    def __init__(self, name: str) -> None:
        self.name = name
        self.received = []

    def on_event(self, event: str) -> None:
        if self.name == "bad":
            raise ValueError("bad handler 炸了")
        self.received.append(event)


def main() -> None:
    bus = EventBus()
    good = Subscriber("good")
    bad = Subscriber("bad")
    bus.subscribe("order.created", good.on_event)
    bus.subscribe("order.created", bad.on_event)

    bus.publish("order.created", "e1")
    assert good.received == ["e1"], "坏订阅者不影响好订阅者"
    assert len(bus.errors) == 1
    print(f"异常隔离: good 收到 {good.received}, 错误 {bus.errors}")

    del bad
    gc.collect()
    bus.publish("order.created", "e2")
    assert good.received == ["e1", "e2"]
    print(f"弱引用注销: 死订阅者被剔除, good 继续 {good.received}")

    def plain(e):  # 普通函数也能订阅
        good.received.append("fn:" + e)
    bus.subscribe("order.created", plain)
    bus.publish("order.created", "e3")
    print(f"最终状态: {good.received}")


if __name__ == "__main__":
    main()
