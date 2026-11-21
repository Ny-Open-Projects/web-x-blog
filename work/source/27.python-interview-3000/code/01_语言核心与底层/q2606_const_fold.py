"""常量折叠的边界:哪些表达式在编译期算完,哪些留到运行时。"""
import dis


def folded():
    x = 1 + 2                 # 算术折叠
    y = "ab" "cd"             # 字面量拼接折叠
    z = 2 ** 64               # 中等规模幂折叠
    w = (1, "a", True)        # 全常量元组折叠
    f = 0.1 + 0.2             # 连精度问题一起折叠
    return x, y, z, w, f


def not_folded(a):
    n = 2 ** 100000           # 超大幂:安全阀拒绝折叠
    v = a + 1                 # 有名字参与,不折叠
    s = "ab" + a              # 运行时才拼接
    return n, v, s


if __name__ == "__main__":
    print("folded 的 co_consts:")
    for c in folded.__code__.co_consts:
        print("   ", repr(c))

    print("not_folded 的 co_consts(注意 2 和 100000 原样保留):")
    for c in not_folded.__code__.co_consts:
        print("   ", repr(c))

    print("\ndis 验证:folded 的每个赋值只有一条 LOAD_CONST")
    dis.dis(folded)
