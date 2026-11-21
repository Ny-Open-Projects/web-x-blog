"""常量治理:模块常量、Enum 与魔法数的边界。"""
import enum


class OrderState(enum.Enum):
    CREATED = "created"
    PAID = "paid"
    SHIPPED = "shipped"


MAX_RETRY = 3                     # 模块级常量:大写 + 下划线
TIMEOUT_SECONDS = 30

_ALLOWED_NEXT = {
    OrderState.CREATED: frozenset({OrderState.PAID}),
    OrderState.PAID: frozenset({OrderState.SHIPPED}),
    OrderState.SHIPPED: frozenset(),
}


def can_transition(src, dst):
    return dst in _ALLOWED_NEXT.get(src, frozenset())


def parse_state(raw):
    try:
        return OrderState(raw)
    except ValueError:
        raise ValueError(f"未知订单状态: {raw!r}") from None


if __name__ == "__main__":
    print("合法推进:", can_transition(OrderState.PAID, OrderState.SHIPPED))
    print("非法跳转:", can_transition(OrderState.CREATED, OrderState.SHIPPED))
    print("字符串解析:", parse_state("paid"))
    try:
        parse_state("cancelled")
    except ValueError as e:
        print("带上下文的报错:", e)
    print("魔法数消失后:含义集中在唯一的常量与枚举定义处")
