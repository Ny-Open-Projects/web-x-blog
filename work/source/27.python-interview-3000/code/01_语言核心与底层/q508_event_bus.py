from collections import defaultdict

class EventBus:
    def __init__(self):
        self._subscribers = defaultdict(list)

    def subscribe(self, event, handler):
        self._subscribers[event].append(handler)
        return lambda: self._subscribers[event].remove(handler)   # 退订闭包

    def publish(self, event, payload):
        for handler in list(self._subscribers[event]):            # 遍历副本
            try:
                handler(payload)
            except Exception as e:
                print(f"[bus] handler {handler.__name__} failed: {e}")

USER_CREATED = "user.created"          # 事件名常量化

if __name__ == "__main__":
    bus = EventBus()
    seen = []
    unsub = bus.subscribe(USER_CREATED, lambda p: seen.append(("audit", p["name"])))
    bus.subscribe(USER_CREATED, lambda p: seen.append(("mail", p["name"])))
    bus.publish(USER_CREATED, {"name": "Alice"})
    unsub()
    bus.publish(USER_CREATED, {"name": "Bob"})   # audit 已退订
    print(seen)
