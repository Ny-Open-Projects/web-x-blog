"""深嵌套的卫语句重构:先排除异常路径,主路径保持最浅。"""
import inspect


def before(order, user):
    """箭头反模式:主逻辑埋在深层缩进里。"""
    if order is not None:
        if user is not None:
            if user.get("active"):
                if order.get("total", 0) > 0:
                    return "下单成功"
                else:
                    return "金额必须为正"
            else:
                return "用户未激活"
        else:
            return "缺少用户"
    else:
        return "缺少订单"


def after(order, user):
    """卫语句版本:异常路径提前返回,主路径零嵌套。"""
    if order is None:
        return "缺少订单"
    if user is None:
        return "缺少用户"
    if not user.get("active"):
        return "用户未激活"
    if order.get("total", 0) <= 0:
        return "金额必须为正"
    return "下单成功"


def max_indent(func):
    """粗略度量:函数体最大缩进层级。"""
    depth = 0
    for line in inspect.getsource(func).splitlines():
        depth = max(depth, (len(line) - len(line.lstrip(" "))) // 4)
    return depth


if __name__ == "__main__":
    cases = [
        (None, None),
        ({"total": 0}, {"active": True}),
        ({"total": 5}, {"active": False}),
        ({"total": 5}, {"active": True}),
    ]
    assert all(before(o, u) == after(o, u) for o, u in cases)
    print("四种入参两版结果一致:", [after(o, u) for o, u in cases])
    print("最大缩进:重构前", max_indent(before), "层 -> 重构后", max_indent(after), "层")
