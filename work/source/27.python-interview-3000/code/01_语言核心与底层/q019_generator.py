def countdown(n):
    while n > 0:
        yield n
        n -= 1
    return "done"

if __name__ == "__main__":
    gen = countdown(3)
    print(next(gen))  # 3
    print(next(gen))  # 2
    for rest in gen:  # for 自动处理 StopIteration
        print(rest)   # 1

    try:
        next(gen)
    except StopIteration as e:
        print("return value:", e.value)  # done

    big = (x * x for x in range(10**8))  # 立即返回,不占内存
    print(next(big))
