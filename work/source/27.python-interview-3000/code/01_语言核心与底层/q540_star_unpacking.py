def concat(*parts, sep="-"):
    return sep.join(parts)

if __name__ == "__main__":
    first, *middle, last = [1, 2, 3, 4, 5]
    print(first, middle, last)            # 1 [2, 3, 4] 5

    head, *tail = range(3)
    print(head, tail)                     # 0 [1, 2]

    single, *rest = [42]
    print(single, rest)                   # rest 是空 list,不是 42

    print(concat(*["a", "b", "c"]))

    base, extra = {"a": 1}, {"b": 2}
    print({**base, **extra})

    x, y = 10, 20
    x, y = y, x                           # tuple 打包再解包:无临时变量
    print(x, y)
