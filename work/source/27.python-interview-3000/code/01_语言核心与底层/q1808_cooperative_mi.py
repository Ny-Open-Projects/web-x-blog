"""协作式多继承:super 链上的 kwargs 传递与耗尽。"""


class Base:
    def __init__(self, **kw):
        self.leftover = kw          # 链尾:接住没人认领的 kwargs,不再上传
        print("Base 收尾,剩余:", set(kw))


class TimedMixin:
    def __init__(self, timeout=None, **kw):
        self.timeout = timeout
        print("TimedMixin 认领 timeout")
        super().__init__(**kw)


class TaggedMixin:
    def __init__(self, tags=(), **kw):
        self.tags = tags
        print("TaggedMixin 认领 tags")
        super().__init__(**kw)


class Task(TimedMixin, TaggedMixin, Base):
    pass


class Broken(Task):
    def __init__(self, **kw):
        Base.__init__(self)         # 反例:绕过 super 链,其他 mixin 全饿死


if __name__ == "__main__":
    print("MRO:", [c.__name__ for c in Task.__mro__])
    t = Task(timeout=5, tags=("a",), name="job1")
    print("timeout:", t.timeout, "| tags:", t.tags, "| 没人认领:", t.leftover)
    print("--- 反例 ---")
    b = Broken(timeout=9)
    print("Broken.timeout:", getattr(b, "timeout", "没拿到"))
