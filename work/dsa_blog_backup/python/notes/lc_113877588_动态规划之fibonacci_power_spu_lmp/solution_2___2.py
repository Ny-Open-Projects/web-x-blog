# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588
# 快速幂 (Fast Power) - O(log n)
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def power(base, exp):  # 定义函数 power（参数：base, exp）
    if exp == 0:  # 若 exp 等于 0
        return 1  # 返回 1
    half = power(base, exp >> 1)  # 把 power(base, exp 超过 超过 1) 存入 half
    if exp % 2 == 0:  # 若 exp 对…取模 2 等于 0
        return half * half  # 返回 half 乘 half
    return half * half * base  # 返回 half 乘 half 乘 base


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(power(2, 10))  # 1024
