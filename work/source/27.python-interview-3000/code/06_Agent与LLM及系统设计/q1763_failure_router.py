"""失败处置路由器:按错误类别决定 重试 换路 放弃,重试预算与换路序列双护栏。"""


class QuotaError(Exception):
    pass


RETRYABLE, SWITCH, FATAL = "retryable", "switch", "fatal"


def classify(exc):
    """错误分类:瞬时错误可重试,配额与路由错误应换路,参数错误直接放弃。"""
    if isinstance(exc, TimeoutError):
        return RETRYABLE
    if isinstance(exc, QuotaError):
        return SWITCH
    if isinstance(exc, ValueError):
        return FATAL
    return SWITCH                                # 未知错误保守处理:先换路


class FailureRouter:
    def __init__(self, providers, max_retries=2):
        self.providers = providers                # 有序换路候选
        self.max_retries = max_retries
        self.attempts = []                        # (provider, outcome)
        self.abandon_reason = None

    def run(self, task, payload):
        for provider in self.providers:
            retries = 0
            while True:
                try:
                    result = task(provider, payload)
                    self.attempts.append((provider, "ok"))
                    return {"result": result, "via": provider}
                except Exception as exc:
                    action = classify(exc)
                    self.attempts.append((provider, action))
                    if action == FATAL:
                        self.abandon_reason = "fatal: " + str(exc)
                        return None
                    if action == RETRYABLE:
                        if retries < self.max_retries:
                            retries += 1
                            continue              # 原路重试,受预算约束
                        self.abandon_reason = "retry budget spent on " + provider
                        return None
                    break                         # 换路:跳出 while 到下一家
        self.abandon_reason = "all providers exhausted"
        return None


def task_for(script):
    def task(provider, payload):
        act = script[provider].pop(0)
        if act == "ok":
            return "done@" + provider
        raise act
    return task


if __name__ == "__main__":
    router1 = FailureRouter(["p1"])
    s1 = {"p1": [TimeoutError("t"), TimeoutError("t"), "ok"]}
    assert router1.run(task_for(s1), {}) == {"result": "done@p1", "via": "p1"}
    assert router1.attempts == [("p1", "retryable"), ("p1", "retryable"), ("p1", "ok")]

    router2 = FailureRouter(["p1", "p2"], max_retries=2)
    s2 = {"p1": [QuotaError("quota")],
          "p2": [TimeoutError("t"), TimeoutError("t"), TimeoutError("t")]}
    assert router2.run(task_for(s2), {}) is None
    assert router2.abandon_reason == "retry budget spent on p2"
    assert router2.attempts == [("p1", "switch"), ("p2", "retryable"),
                                ("p2", "retryable"), ("p2", "retryable")]

    router3 = FailureRouter(["p1", "p2"])
    s3 = {"p1": [ValueError("bad param")], "p2": ["ok"]}
    assert router3.run(task_for(s3), {}) is None
    assert router3.abandon_reason == "fatal: bad param", "致命错误不重试不换路"

    router4 = FailureRouter(["p1", "p2"])
    s4 = {"p1": [RuntimeError("weird")], "p2": ["ok"]}
    assert router4.run(task_for(s4), {}) == {"result": "done@p2", "via": "p2"}
    print("失败路由通过:瞬时重试受预算约束 配额换路 致命放弃,决策全程留痕")
