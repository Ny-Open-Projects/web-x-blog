"""四类测试替身的手写最小实现与选用场景。"""


class Mailer:
    """被替换的依赖接口。"""

    def send(self, to, subject):
        raise NotImplementedError


class DummyMailer(Mailer):
    """dummy:占位,预期不会被调用。"""

    def send(self, to, subject):
        raise AssertionError("不应发信")


class StubMailer(Mailer):
    """stub:返回固定值,供被测代码走分支。"""

    def send(self, to, subject):
        return True


class SpyMailer(Mailer):
    """spy:转发并记录,断言交互。"""

    def __init__(self):
        self.calls = []

    def send(self, to, subject):
        self.calls.append((to, subject))
        return True


class FakeMailer(Mailer):
    """fake:内存实现,可多步查询。"""

    def __init__(self):
        self.outbox = []

    def send(self, to, subject):
        self.outbox.append((to, subject))
        return True


def notify_user(mailer, user):
    """被测函数:依赖 Mailer 接口。"""
    return mailer.send(user["email"], "welcome")


if __name__ == "__main__":
    user = {"email": "a@b.c"}

    print("stub 返回:", notify_user(StubMailer(), user))

    spy = SpyMailer()
    notify_user(spy, user)
    print("spy 记录:", spy.calls)

    fake = FakeMailer()
    notify_user(fake, user)
    notify_user(fake, user)
    print("fake 收件箱条数:", len(fake.outbox))

    print("dummy 正常情况下不应触发 send")
