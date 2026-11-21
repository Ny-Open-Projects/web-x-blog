---
title: [Q273] Agent 与外部系统的重试与超时策略
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q273 · Agent 与外部系统的重试与超时策略

> 难度:★★★★ | 标签:Agent, 可靠性

**问**:LLM API 和下游工具都会超时,重试策略怎么设计?

**答**:分层策略:1) LLM API——429/5xx 幂等可重试,用指数退避+抖动(exponential backoff with jitter),设置总重试预算;400 类参数错误不重试直接报;2) 工具调用——读操作自动重试,写操作必须幂等键保护后再重试;3) 全链路——设置 deadline 预算,剩余时间不足时提前降级而不是无限等待;4) 熔断——连续失败率超阈值暂时停止调用,防止雪崩。关键区分"可重试错误"(暂时性)与"不可重试错误"(确定性),盲目重试只会放大故障。

```python
# file: code/06_Agent与LLM及系统设计/q273_retry_backoff.py
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
```

**追问**:
- 为什么 4xx 不重试?——参数/权限类错误是确定性的,重试只会重复失败;只有 429/5xx/超时这类暂时性错误才值得退避重试。
- deadline 预算怎么传递?——请求入口起算,逐层减去已耗时下传;剩余不足直接降级,不做「等了 9 秒又调一个 10 秒依赖」。
- 熔断的恢复怎么做?——半开状态放少量探测流量,成功率达标逐步恢复;直接全量恢复会再次雪崩。
