

def span(*args, **kwargs):
    return args, kwargs


if __name__ == "__main__":
    a = [1, 2]
    b = (3, 4)
    gen = (x * x for x in range(3))

    print("call      :", span(*a, *b, tag="end"))
    print("list      :", [*a, *b, 5])
    print("tuple     :", (*a, *b))
    print("set       :", {*a, *b, 4})          # 解包进集合顺带去重
    first, second = [*gen], [*gen]
    print("generator :", first, "then", second)   # 第二次解包已耗尽

    d1 = {"retries": 3, "timeout": 1.0}
    d2 = {"timeout": 2.0, "debug": True}
    merged = {**d1, **d2, "extra": 1}          # 后写的键赢,重复不报错
    print("dict merge:", merged)

    # 调用处多星号与关键字字典混用;定义处仍只能有一个 *args
    defaults = {"tag": "auto"}
    print("mixed     :", span(*a, **defaults))

    # dict 字面量只接受 **mapping:**[1, 2] 是 SyntaxError,只作说明不执行
    print("keys view :", {*d1})                 # 可迭代解包进集合只剩键
