"""集合的子集与超集:<=、< 运算符与 issubset 家族。"""

if __name__ == "__main__":
    small, big = {1, 2}, {1, 2, 3}
    print("small <= big:", small <= big)
    print("small < big 真子集:", small < big)
    print("big >= small:", big >= small)
    print("small <= small:", small <= small, "| small < small:", small < small)

    print("issubset 接受迭代:", {1}.issubset([1, 2, 3]))
    try:
        {1} <= [1, 2, 3]
    except TypeError as exc:
        print("运算符拒绝 list:", exc)

    print("空集:", set() <= big, set() < big)
    print("不相交:", small.isdisjoint({7, 8}), small.isdisjoint({2, 7}))
