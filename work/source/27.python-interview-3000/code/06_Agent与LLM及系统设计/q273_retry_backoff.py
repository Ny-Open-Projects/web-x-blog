"""指数退避重试:区分可重试与不可重试错误,带抖动与总预算控制。"""
import random
import time


class RetryableError(Exception):
    pass


class FatalError(Exception):
    pass


def call_with_retry(fn, max_attempts: int = 4, base_delay: float = 0.1,
                    deadline_s: float = 1.0):
    start = time.time()
    for attempt in range(1, max_attempts + 1):
        if time.time() - start > deadline_s:
            return "降级:超出 deadline 预算"
        try:
            return fn()
        except FatalError:
            return "失败:确定性错误,不重试"
        except RetryableError:
            if attempt == max_attempts:
                return "失败:重试耗尽"
            delay = base_delay * (2 ** (attempt - 1)) + random.uniform(0, 0.05)
            print(f"  第{attempt}次失败,退避 {delay:.2f}s 后重试")
            time.sleep(delay)
    return "失败"


def flaky_api(state: dict) -> str:
    state["n"] += 1
    if state["n"] < 3:
        raise RetryableError("429 too many requests")
    return "成功响应"


def bad_request() -> str:
    raise FatalError("400 invalid parameter")


if __name__ == "__main__":
    random.seed(1)
    state = {"n": 0}  # 状态须在重试间保持,否则每次调用都从头计数
    print(call_with_retry(lambda: flaky_api(state)))
    print(call_with_retry(bad_request, max_attempts=2))
    print(call_with_retry(lambda: (_ for _ in ()).throw(RetryableError()),
                          max_attempts=2, deadline_s=0.0001))
