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
