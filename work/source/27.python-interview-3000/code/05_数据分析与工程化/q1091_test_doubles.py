
class Mailer:
    def send(self, to, body):
        raise RuntimeError("真实 IO")

class StubMailer(Mailer):
    def send(self, to, body):
        return True                      # stub:固定返回,让流程走通

class SpyMailer(Mailer):
    def __init__(self):
        self.sent = []

    def send(self, to, body):
        self.sent.append((to, body))     # spy:记录交互供事后断言
        return True

def notify(mailer, user, message):
    return mailer.send(user["email"], message)

if __name__ == "__main__":
    user = {"email": "a@b.c"}
    assert notify(StubMailer(), user, "hi") is True          # 状态验证
    spy = SpyMailer()
    notify(spy, user, "hi")
    assert spy.sent == [("a@b.c", "hi")]                     # 交互验证
    print("stub 验证状态,spy 验证交互,mock 事前期望,dummy 纯占位")
