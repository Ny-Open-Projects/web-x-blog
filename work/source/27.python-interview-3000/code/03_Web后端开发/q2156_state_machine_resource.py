"""状态机化资源设计: 订单状态转换表与非法转换的 409 拒绝(纯标准库)。"""


class Conflict(Exception):
    """非法状态转换, 对应 HTTP 409 Conflict。"""


TRANSITIONS = {
    # 当前状态 -> {事件: 目标状态}
    "created": {"pay": "paid", "cancel": "cancelled"},
    "paid": {"ship": "shipped", "refund": "refunded"},
    "shipped": {"deliver": "delivered"},
    "delivered": {"refund": "refunded"},
    "cancelled": {},
    "refunded": {},
}


def apply_event(order, event):
    """按转换表驱动状态机; 未定义的转换直接拒绝而非静默忽略。"""
    cur = order["state"]
    target = TRANSITIONS.get(cur, {}).get(event)
    if target is None:
        raise Conflict("state {} 不允许事件 {}".format(cur, event))
    order["state"] = target
    order.setdefault("history", []).append("{} --{}--> {}".format(cur, event, target))
    return order


def http_apply(order, event):
    try:
        apply_event(order, event)
        return 204, None
    except Conflict as exc:
        return 409, {"error": "invalid_transition", "detail": str(exc),
                     "current": order["state"]}


order = {"id": "o1", "state": "created", "history": []}
for event in ["pay", "ship", "deliver"]:
    code, body = http_apply(order, event)
    print("事件 {:8s} -> HTTP {} {}".format(event, code, body or order["state"]))

code, body = http_apply(order, "pay")            # delivered 后再支付: 非法
print("事件 {:8s} -> HTTP {} {}".format("pay", code, body))
code, body = http_apply(order, "refund")         # 合法: delivered 可退款
print("事件 {:8s} -> HTTP {} {}".format("refund", code, body or order["state"]))
assert code == 204 and order["state"] == "refunded"
print("要点: 状态机把非法操作从业务报错升级为协议层的 409, 转换表即文档、即测试用例来源")
