"""重试退避:指数退避加全抖动,只有可重试错误才值得重试"""

import random

random.seed(42)

RETRYABLE = ("TimeoutError", "ConnectionError", "HTTP503")


def is_retryable(err):
    return any(token in err for token in RETRYABLE)


def full_jitter_delay(attempt, base=0.5, cap=8.0):
    """AWS 全抖动:delay = uniform(0, min(cap, base * 2**attempt))"""
    return random.uniform(0, min(cap, base * 2 ** attempt))


def call_with_retry(fn, max_attempts=5):
    for attempt in range(max_attempts):
        err = fn(attempt)
        if err is None:
            return f"第 {attempt + 1} 次成功"
        if not is_retryable(err):
            return f"第 {attempt + 1} 次致命错误 {err},直接失败不重试"
        if attempt == max_attempts - 1:
            return f"重试 {max_attempts} 次仍失败,进死信区"
        print(f"  第 {attempt + 1} 次失败 {err},退避 {full_jitter_delay(attempt):.2f}s 后重试")
    return "unreachable"


if __name__ == "__main__":
    print("场景 1:瞬时故障两次后恢复")
    fail_plan = ["TimeoutError", "ConnectionError", None]
    print(" ->", call_with_retry(lambda i: fail_plan[i] if i < len(fail_plan) else None))

    print("场景 2:参数错误,重试无意义")
    print(" ->", call_with_retry(lambda i: "ValueError: bad column"))

    print("场景 3:持续故障,耗尽次数")
    print(" ->", call_with_retry(lambda i: "HTTP503"))
    print("要点:重试要配预算与抖动,避免重试风暴把下游彻底打挂")
