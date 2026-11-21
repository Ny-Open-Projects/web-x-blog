"""渠道归因:首触、末触、线性、时间衰减四种模型的对照实现"""

TOUCHES = {
    # 订单 -> 有序触点序列 渠道, 次序
    "order_1": [("ad", 1), ("search", 2), ("social", 3), ("email", 4)],
    "order_2": [("search", 1), ("ad", 2)],
}


def first_touch(path):
    return {path[0][0]: 1.0}


def last_touch(path):
    return {path[-1][0]: 1.0}


def linear(path):
    credit = 1.0 / len(path)
    return {ch: credit for ch, _ in path}


def time_decay(path, half_life=1):
    """按触点距转化的步数做指数衰减,步数越近权重越大"""
    weights = [0.5 ** (len(path) - i - 1) for i in range(len(path))]
    total = sum(weights)
    return {ch: w / total for (ch, _), w in zip(path, weights)}


def aggregate(orders, model):
    totals = {}
    for path in orders.values():
        for ch, credit in model(path).items():
            totals[ch] = totals.get(ch, 0.0) + credit
    return totals


if __name__ == "__main__":
    models = [("first_touch", first_touch), ("last_touch", last_touch),
              ("linear", linear), ("time_decay", time_decay)]
    for name, fn in models:
        totals = aggregate(TOUCHES, fn)
        line = ", ".join(f"{ch}={v:.2f}" for ch, v in sorted(totals.items(),
                                                            key=lambda x: -x[1]))
        print(f"{name:<12} {line}")
    print("模型只决定'功劳怎么分',选型要跟投放决策挂钩,建议多模型并列展示")
