"""== 的递归相等与循环引用:身份短路何时救场,何时失效。"""

if __name__ == "__main__":
    a = [1, [2, 3]]
    b = [1, [2, 3]]
    print("深嵌套逐元素比较:", a == b)

    a.append(a)
    print("自引用对象与自身比较:", a == a)     # 身份短路

    x = [1]
    x.append(x)
    y = [1]
    y.append(y)
    try:
        print(x == y)
    except RecursionError:
        print("两个独立循环结构: RecursionError,递归不收敛")

    other = [1, [1]]
    print("循环 vs 手工展开:", x == other)
