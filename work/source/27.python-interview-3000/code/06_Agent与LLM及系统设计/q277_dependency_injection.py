from dataclasses import dataclass
from typing import Protocol


class Notifier(Protocol):
    def send(self, user: str, msg: str) -> None: ...


class EmailNotifier:
    def send(self, user: str, msg: str) -> None:
        print(f"[email] to={user} msg={msg}")


class FakeNotifier:
    """测试替身,不发真邮件。"""
    def __init__(self):
        self.sent = []

    def send(self, user: str, msg: str) -> None:
        self.sent.append((user, msg))


@dataclass
class UserService:
    notifier: Notifier  # 依赖通过构造注入

    def register(self, user: str) -> None:
        self.notifier.send(user, "welcome")


if __name__ == "__main__":
    svc = UserService(EmailNotifier())
    svc.register("alice")

    fake = FakeNotifier()
    UserService(fake).register("bob")
    print(fake.sent)  # 断言用
