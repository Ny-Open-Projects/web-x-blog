import random

def fetch():
    return random.randint(0, 5)

if __name__ == "__main__":
    random.seed(7)

    # 旧写法:先算一次赋给变量,再在 while 条件里反复判断
    while (chunk := fetch()) != 0:
        print("got", chunk)
    print("loop ended on zero")

    values = [10, 25, 3, 40]
    big = [trimmed for v in values if (trimmed := v - 20) > 0]
    print(big)               # [5, 20],计算一次并复用

    if (n := len(values)) > 3:
        print(f"{n} items, more than three")
