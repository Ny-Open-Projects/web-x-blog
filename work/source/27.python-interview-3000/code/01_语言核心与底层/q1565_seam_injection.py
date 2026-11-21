

def smtp_sender(recipient, text):
    """真实依赖:演示桩,不真发。"""
    return "smtp -> %s: %s" % (recipient, text)


def console_sender(recipient, text):
    return "console -> %s: %s" % (recipient, text)


class Notifier:
    """接缝设计:sender 是构造参数,默认真实实现。"""

    def __init__(self, sender=smtp_sender, max_len=140):
        self.sender = sender
        self.max_len = max_len

    def notify(self, recipient, text):
        if len(text) > self.max_len:
            raise ValueError("text 超过 %d 字符限制" % self.max_len)
        return self.sender(recipient, text)


def record_sink(recipient, text):
    """测试用 fake:记录而不发送。"""
    record_sink.calls.append((recipient, text))
    return "recorded"


record_sink.calls = []


def run_suite():
    results = []
    notifier = Notifier(sender=record_sink)          # 注入 fake
    results.append(notifier.notify("ops@x.io", "deploy done"))
    results.append(notifier.notify("ops@x.io", "deploy v2"))
    assert record_sink.calls == [("ops@x.io", "deploy done"),
                                 ("ops@x.io", "deploy v2")]
    return results


if __name__ == "__main__":
    print("default:", Notifier().notify("dev@x.io", "hello"))
    print("fake   :", run_suite())
    try:
        Notifier().notify("dev@x.io", "x" * 200)
    except ValueError as err:
        print("guard  :", err)
