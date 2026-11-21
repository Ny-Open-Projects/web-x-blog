if __name__ == "__main__":
    for i in range(3):
        pass
    print("i survives loop:", i)          # 2:for 不产生作用域

    funcs = []
    for j in range(3):
        funcs.append(lambda: j)           # 闭包共享同一个 j
    print("late binding:", [f() for f in funcs])   # [2, 2, 2]

    comp = [k for k in range(3)]          # 推导式有独立作用域
    try:
        print(k)
    except NameError as e:
        print("comprehension leaked nothing:", e)
