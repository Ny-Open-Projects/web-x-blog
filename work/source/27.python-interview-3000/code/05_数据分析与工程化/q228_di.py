from typing import Protocol


class Notifier(Protocol):
    def send(self, to: str, msg: str) -> bool: ...


class EmailNotifier:
    def send(self, to: str, msg: str) -> bool:
        raise RuntimeError("生产实现")


class FakeNotifier:
    def __init__(self):
        self.sent: list[tuple[str, str]] = []

    def send(self, to: str, msg: str) -> bool:
        self.sent.append((to, msg))
        return True


def order_service(notifier: Notifier, user: str) -> bool:
    # 业务逻辑只依赖抽象,测试时注入 Fake
    return notifier.send(to=user, msg="order confirmed")


def test_with_fake():
    fake = FakeNotifier()
    assert order_service(fake, "alice")
    assert fake.sent == [("alice", "order confirmed")]
