import dis

def mystery():
    funcs = []
    for n in [1, 2, 3]:
        funcs.append(lambda: n * 10)
    return funcs

if __name__ == "__main__":
    results = [f() for f in mystery()]
    print("surprising:", results)                 # [30, 30, 30]

    # 第一步后:验证机制——闭包 cell 里存的是什么
    f = mystery()[0]
    cell = f.__closure__[0]
    print("cell content:", cell.cell_contents)

    # 反汇编验证:LOAD_DEREF 说明运行时才读 cell
    for ins in dis.get_instructions(f):
        if ins.opname.startswith("LOAD"):
            print(" ", ins.opname, ins.argrepr)

    # 定义处修复:默认参数在创建时绑定值
    def fixed():
        funcs = []
        for n in [1, 2, 3]:
            funcs.append(lambda n=n: n * 10)
        return funcs

    print("fixed:", [g() for g in fixed()])
    print("methodology: repro -> hypothesis -> verify with dis/id -> fix at definition -> regression")
