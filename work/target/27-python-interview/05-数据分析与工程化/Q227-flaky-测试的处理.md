---
title: [Q227] flaky 测试的处理
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q227 · flaky 测试的处理

> 难度:★★★ | 标签:flaky, 测试稳定性

**问**:一个测试偶尔失败重跑就过,你会怎么处理?

**答**:flaky 测试的毒害是**消耗信任**——团队对红灯麻木后真 bug 也会被忽略。处理路径:一,先归类根因:时序竞争(sleep 代替等待,改成轮询条件)、外部依赖抖动(网络/第三方,改 stub 或隔离)、测试间状态泄漏(fixture 未清理、共享全局)、顺序依赖(测试独立化)、资源不足(超时太紧)。二,策略:用 `pytest-rerunfailures` 临时重跑止损,同时把 flaky 用例**打标记隔离**到单独 job,限期修复;而不是无限重跑掩盖问题。三,预防:CI 失败即查不积累、关键随机性注入固定 seed(Q229)、测试隔离每用例清场。

```python
# file: code/05_数据分析与工程化/q227_flaky_fix.py
import random


def flaky_network_stub(fail_rate=0.0):
    # 修法:把网络依赖替换为确定性 stub,而不是祈祷它别抖
    def call():
        if random.random() < fail_rate:
            raise ConnectionError
        return {"status": "ok"}
    return call


def poll_until(check, max_attempts=10):
    # 修法二:轮询条件代替 sleep 猜时间
    for _ in range(max_attempts):
        if check():
            return True
    return False


def test_deterministic():
    stub = flaky_network_stub(fail_rate=0.0)
    assert stub()["status"] == "ok"

def test_no_sleep_guessing():
    assert poll_until(lambda: True) is True
    assert poll_until(lambda: False, max_attempts=3) is False
```

**追问**:
- rerunfailures 的正确用法?——只对标记 flaky 的用例重试并设上限;全局无限重试会把红灯文化合法化。
- 怎么定位时序型 flaky?——把 sleep 换成轮询断言(eventual consistency 等条件),加详细超时日志;sleep 长度永远猜不准。
- 测试间状态泄漏的典型?——模块级缓存、环境变量未还原、临时文件同名;fixture 的 yield 清理 + monkeypatch 自动还原是防线。
