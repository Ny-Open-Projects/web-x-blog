from collections import defaultdict
from typing import Callable


class EventBus:
    def __init__(self):
        self._subs: dict[str, list[Callable]] = defaultdict(list)

    def subscribe(self, event: str, fn: Callable) -> None:
        self._subs[event].append(fn)

    def unsubscribe(self, event: str, fn: Callable) -> None:
        self._subs[event].remove(fn)

    def publish(self, event: str, *args, **kwargs) -> None:
        for fn in list(self._subs[event]):
            try:
                fn(*args, **kwargs)
            except Exception as exc:  # 隔离订阅者异常
                print(f"[warn] subscriber {fn} failed: {exc}")


bus = EventBus()
bus.subscribe("order.paid", lambda oid: print(f"send email for {oid}"))
bus.subscribe("order.paid", lambda oid: print(f"add points for {oid}"))

if __name__ == "__main__":
    bus.publish("order.paid", 1001)
