

def minmax(seq):
    """一次遍历同时返回两个值:调用方一行解构。"""
    it = iter(seq)
    try:
        low = high = next(it)
    except StopIteration:
        raise ValueError("minmax empty seq") from None
    for x in it:
        if x < low:
            low = x
        elif x > high:
            high = x
    return low, high


if __name__ == "__main__":
    a, b = 1, 2
    a, b = b, a                     # 打包再解包,无临时变量
    print("swap:", a, b)

    x, y = 0, 1
    for _ in range(8):
        x, y = y, x + y             # 状态对同步推进
    print("fib :", x)

    first, *rest = [10, 20, 30, 40]
    *init, last = rest
    print("head/tail:", first, rest, init, last)

    (name, (lat, lon)) = ("pei", (39.9, 116.4))    # 嵌套模式
    print("nested:", name, lat, lon)

    scores = {"alice": 91, "bob": 85}
    for who, score in scores.items():              # items 直接解构
        print("item :", who, score)

    print("minmax:", minmax([5, 3, 9, 1, 7]))
    try:
        a, b = (1, 2, 3)
    except ValueError as err:
        print("mismatch:", err)
