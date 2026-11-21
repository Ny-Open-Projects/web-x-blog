from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    type: str
    payload: dict


def fold(events: list[Event]) -> dict:
    """从事件流折叠出当前状态,处理函数是唯一真相来源。"""
    state = {"balance": 0}
    for e in events:
        if e.type == "deposit":
            state["balance"] += e.payload["amount"]
        elif e.type == "withdraw":
            state["balance"] -= e.payload["amount"]
    return state


# 有 bug 的版本:withdraw 少扣了手续费
def fold_buggy(events: list[Event]) -> dict:
    state = {"balance": 0}
    for e in events:
        if e.type == "deposit":
            state["balance"] += e.payload["amount"]
        elif e.type == "withdraw":
            state["balance"] -= e.payload["amount"] - 5  # bug
    return state


if __name__ == "__main__":
    events = [
        Event("deposit", {"amount": 100}),
        Event("withdraw", {"amount": 30}),
        Event("deposit", {"amount": 20}),
    ]
    print("buggy:", fold_buggy(events))   # 修复前线上错误状态
    print("fixed:", fold(events))         # 修复后重放得到正确状态
