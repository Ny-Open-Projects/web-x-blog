"""比较链的字节码视角:中间值只求值一次。"""
import dis


def probe():
    calls = []

    def middle():
        calls.append("middle")
        return 5

    ok = 1 < middle() < 10
    return ok, calls


def mixed_operators():
    # 每一段允许不同比较符:1 <= 2 < 2 即 1<=2 and 2<2
    return 1 <= 2 < 2, 1 <= 2 <= 2


def tail_opcodes(func, n=8):
    return [(i.opname, i.argrepr) for i in dis.get_instructions(func)][-n:]


if __name__ == "__main__":
    ok, calls = probe()
    print("1 < middle() < 10:", ok, "| middle 调用次数:", len(calls))
    print("混合运算符链:", mixed_operators())
    print("probe 尾部字节码(可见中间值的复制与跳转处理):")
    for op, arg in tail_opcodes(probe):
        print("   ", op, arg)
