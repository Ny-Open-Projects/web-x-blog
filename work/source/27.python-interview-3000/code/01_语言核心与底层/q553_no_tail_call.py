import sys

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)                # 乘法在递归返回后:不是尾调用

def fact_iter(n):
    acc = 1
    while n > 1:                          # 迭代:O(1) 栈
        acc *= n
        n -= 1
    return acc

if __name__ == "__main__":
    print(fact(10), fact_iter(10))
    print("recursion limit:", sys.getrecursionlimit())
    try:
        fact(3000)
    except RecursionError as e:
        print("RecursionError:", str(e)[:40])
    print("iterative deep:", len(str(fact_iter(3000))), "digits, no problem")
