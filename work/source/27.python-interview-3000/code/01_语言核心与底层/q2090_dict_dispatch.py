"""字典分派:把 if-elif 链重构为函数表。"""


def _approve(amount):
    return f"通过 {amount}"


def _review(amount):
    return f"转人工 {amount}"


def _reject(amount):
    return f"拒绝 {amount}"


def decide_if_chain(action, amount):
    """重构前:分支链每加一个动作就长一节。"""
    if action == "approve":
        return _approve(amount)
    elif action == "review":
        return _review(amount)
    elif action == "reject":
        return _reject(amount)
    return "未知动作"


HANDLERS = {"approve": _approve, "review": _review, "reject": _reject}


def decide_table(action, amount):
    """重构后:查表分派,新增动作只注册函数。"""
    handler = HANDLERS.get(action)
    return handler(amount) if handler else "未知动作"


if __name__ == "__main__":
    for action in ("approve", "review", "reject", "hack"):
        a, b = decide_if_chain(action, 100), decide_table(action, 100)
        assert a == b, action
        print(f"{action:8} -> {b}")
