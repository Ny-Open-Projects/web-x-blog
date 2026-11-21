from collections import Counter

STOCK = Counter({"apple": 10, "banana": 6, "cherry": 0})
ORDER_A = Counter({"apple": 3, "banana": 1, "durian": 2})
ORDER_B = Counter({"apple": 1, "banana": 4})


def ship(stock, order):
    """扣减库存:multiset 差,扣到非正的品项从结果消失。"""
    return stock - order


if __name__ == "__main__":
    print("stock:", dict(STOCK))
    left = ship(STOCK, ORDER_A)
    print("after order A:", dict(left))         # durian 扣成 -2 直接消失

    print("A & B:", dict(ORDER_A & ORDER_B))    # 各取最小计数
    print("A | B:", dict(ORDER_A | ORDER_B))    # 各取最大计数
    print("+A   :", dict(+ORDER_A), "-A:", dict(-ORDER_A))

    total = ORDER_A + ORDER_B
    print("A + B:", dict(total))                # 汇总订单

    # 相等比较的版本差异:3.10 起缺失视作零,3.9 是严格 dict 相等
    zeroish = Counter({"apple": 0})
    print("zero-count equality:", zeroish == Counter(),
          " 3.10+ 为 True,3.9 为 False")

    # 元素展开:按计数重复
    print("elements:", sorted(total.elements()))
    print("most_common:", ORDER_A.most_common(2))
