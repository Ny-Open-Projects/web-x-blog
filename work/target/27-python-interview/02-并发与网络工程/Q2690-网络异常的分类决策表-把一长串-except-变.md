---
title: [Q2690] 网络异常的分类决策表:把一长串 except 变成一张可维护的表
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2690 · 网络异常的分类决策表:把一长串 except 变成一张可维护的表

> 难度:★★★ | 标签:异常分类, 决策表, 重试

**问**:网络调用要处理 timeout、refused、reset、gaierror 一堆异常,except 越叠越长怎么办?

**答**:把处置策略收进数据:决策表按"具体类在前、基类兜底"排序,isinstance 沿表匹配即得动作。实测:读超时与拒连判退避重试,重置判幂等重试一次,DNS 错误与权限不足判快速失败;真实连一个没人听的端口抛 ConnectionRefusedError,同样正确落表。新异常类型加一行表项,不再加一层 elif。

- 表序即语义:gaierror 与 PermissionError 都是 OSError 子类,基类兜底必须垫底;

- 动作是策略不是实现:退避重试、幂等重试、快速失败,落库后可全局调参;

- 真实异常与构造异常走同一张表,分类逻辑被端到端验证;

- 未知异常兜底 FAIL_FAST,宁可少重试不可重试风暴。

```python
# file: code/02_并发与网络工程/q2690_error_decision.py
# -*- coding: utf-8 -*-
"""网络异常的分类决策表: 把一长串 except 变成一张可维护的表。

- 每类异常对应一种处置: 退避重试 / 幂等重试一次 / 快速失败;
- 表按"具体类在前、基类兜底"排序, isinstance 沿表匹配即决策;
- 处置策略收进数据, 新异常类型加一行表项, 不再加一层 elif。
"""
import socket
from enum import Enum


class Action(Enum):
    RETRY_BACKOFF = "退避重试"
    RETRY_ONCE = "幂等重试一次"
    FAIL_FAST = "快速失败"


# 决策表: 具体异常在前, 基类兜底在后, 顺序错了整张表就废了
DECISION_TABLE = (
    (socket.timeout, Action.RETRY_BACKOFF),          # 读超时: 对端慢, 可退避
    (ConnectionRefusedError, Action.RETRY_BACKOFF),  # 拒连: 对端没起, 退避等它
    (ConnectionResetError, Action.RETRY_ONCE),       # 重置: 链路抽风, 幂等试一次
    (socket.gaierror, Action.FAIL_FAST),             # DNS: 配置错, 重试无意义
    (OSError, Action.FAIL_FAST),                     # 兜底: 未知网络错误
)


def classify(exc):
    for typ, action in DECISION_TABLE:
        if isinstance(exc, typ):
            return action
    return Action.FAIL_FAST


def simulated_ops():
    yield "读超时", socket.timeout("timed out")
    yield "对端拒绝", ConnectionRefusedError(61, "Connection refused")
    yield "对端重置", ConnectionResetError(54, "Connection reset by peer")
    yield "DNS 失败", socket.gaierror(8, "nodename nor servname provided")
    yield "权限不足", PermissionError(13, "Permission denied")


if __name__ == "__main__":
    print("%-10s %-24s %s" % ("故障", "异常", "处置"))
    for name, exc in simulated_ops():
        print("%-10s %-24s %s" % (name, type(exc).__name__, classify(exc).value))

    print("== 真实故障注入: 连一个没人听的端口 ==")
    try:
        socket.create_connection(("127.0.0.1", 1), timeout=2)
    except OSError as e:
        print("真实异常 %s -> 处置: %s" % (type(e).__name__, classify(e).value))

    print("要点: gaierror 与 PermissionError 都是 OSError 子类, 表序即语义")
```

**追问**:1) 为什么 DNS 错误不重试?——gaierror 多为域名配置错误,重试同样的错误输入只会更快烧掉预算。2) 决策表和熔断怎么配合?——决策表管单次调用的动作,熔断看决策表的统计结果,连续 FAIL_FAST 类就打开熔断。3) 底层机制:为什么表序错一点整张表就废?——isinstance 沿表取首个命中项,gaierror 与 PermissionError 都是 OSError 子类,基类垫在前面就把所有细分异常吞掉,细分动作永远轮不到;决策表是数据化的 elif 链,顺序即语义。4) 生产陷阱?——新异常类型漏登记落到兜底,可重试故障被快速放弃(要监控兜底命中率);重抛时裸 raise 丢 traceback;把 timeout 归为快速失败,对端慢一点就熔断。

---
