"""枚举设计:StrEnum 风格状态机。"""
from enum import Enum, auto


class Status(str, Enum):     # 继承 str,JSON 序列化直接得到字符串
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DONE = "done"


# 合法状态流转表:把状态机收进类型
TRANSITIONS = {
    Status.PENDING: {Status.PAID},
    Status.PAID: {Status.SHIPPED},
    Status.SHIPPED: {Status.DONE},
    Status.DONE: set(),
}


def can_transition(src: Status, dst: Status) -> bool:
    return dst in TRANSITIONS[src]


if __name__ == "__main__":
    import json
    order = {"id": 1, "status": Status.PAID}
    print("序列化:", json.dumps(order))          # 直接输出 "paid"

    print("字符串转枚举:", Status("paid") is Status.PAID)
    try:
        Status("unknown")
    except ValueError as e:
        print("非法值报错:", e)

    print("paid -> shipped:", can_transition(Status.PAID, Status.SHIPPED))
    print("done -> paid  :", can_transition(Status.DONE, Status.PAID))
    print("遍历成员:", [s.value for s in Status])
