import dis


def calc(a, b, c):
    return a * b + c


if __name__ == "__main__":
    for ins in dis.get_instructions(calc):
        print("%4d %-16s %s" % (ins.offset, ins.opname, ins.argrepr))
    print("栈视角: 两次 LOAD_FAST 压栈 -> BINARY_OP 弹二压一 -> LOAD_FAST c -> BINARY_OP -> RETURN_VALUE 弹出")
