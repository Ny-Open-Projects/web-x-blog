---
title: [Q365] 重试与退避策略:为什么不推荐裸 for 循环重试
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q365 · 重试与退避策略:为什么不推荐裸 for 循环重试

> 难度:★★★ | 标签:可靠性, 指数退避

**问**:写一个通用的重试装饰器,要求支持指数退避、抖动和可重试异常白名单。

**答**:核心要点:①只重试指定异常,避免把逻辑 bug 也重试一遍;②指数退避 `2**n` 加随机抖动 jitter,防止服务恢复瞬间被重试风暴打死(惊群);③设最大重试次数与总时限;④每次重试记日志;⑤重试要求操作幂等,否则要配幂等键。生产中可直接用 `tenacity` 库,思路相同。

```python
# file: code/02_并发与网络工程/q365_retry.py
"""通用重试装饰器:指数退避 + 抖动 + 异常白名单。"""
import functools
import logging
import random
import time

log = logging.getLogger(__name__)


def retry(exceptions=(Exception,), attempts=3, base_delay=0.1, max_delay=2.0):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == attempts:
                        raise
                    delay = min(base_delay * 2 ** (attempt - 1), max_delay)
                    delay += random.uniform(0, delay * 0.3)  # jitter 防惊群
                    log.warning("%s 第 %s 次失败 %s,%.2fs 后重试",
                                func.__name__, attempt, e, delay)
                    time.sleep(delay)
        return wrapper
    return deco


class TransientError(Exception):
    pass


_calls = {"n": 0}


@retry(exceptions=(TransientError,), attempts=4, base_delay=0.05)
def flaky_api():
    """前两次失败,第三次成功,模拟抖动的下游。"""
    _calls["n"] += 1
    if _calls["n"] < 3:
        raise TransientError("upstream 503")
    return {"ok": True, "call": _calls["n"]}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print(flaky_api())
```

**追问**:
- 什么是重试风暴?下游抖动时所有调用方同时重试,流量放大数倍把下游彻底打死;用 jitter、熔断器、配额限制来缓解。
- 重试和熔断什么关系?重试解决偶发失败,熔断(`circuit breaker`)在持续失败时快速失败并停止重试,给下游恢复时间。
