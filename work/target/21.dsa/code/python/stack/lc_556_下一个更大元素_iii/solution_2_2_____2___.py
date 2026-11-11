# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397820
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def nextGreaterElement(n):  # 定义函数 nextGreaterElement（参数：元素个数）
    MAX = 2147483647  # 把 2147483647 存入 MAX
    x = n  # 把 元素个数 存入 x
    cnt = 1  # 把 1 存入 计数

    # Find first decreasing position from right (math approach)
    while (
        x >= 10 and (x // 10) % 10 >= x % 10
    ):  # 循环，直到不满足「x 不低于 10 and (x 除以 除以 10) 对…取模 10 不低于 x 对…取模 10」
        x = x // 10  # 把 x 除以 除以 10 存入 x
        cnt += 1  # 计数累加 1

    x = x // 10  # 把 x 除以 除以 10 存入 x
    if x == 0:  # 若 x 等于 0
        return -1  # 返回 减 1

    target_digit = x % 10  # 把 x 对…取模 10 存入 target_digit

    # Find first digit larger than target from right
    x2 = n  # 把 元素个数 存入 x2
    cnt2 = 0  # 把 0 存入 cnt2
    while x2 % 10 <= target_digit:  # 循环，直到不满足「x2 对…取模 10 不超过 target_digit」
        x2 = x2 // 10  # 把 x2 除以 除以 10 存入 x2
        cnt2 += 1  # cnt2累加 1

    d = x2 % 10  # 把 x2 对…取模 10 存入 d

    # Reconstruct number
    result = n // (10**cnt) * (10**cnt)  # 把 元素个数 除以 除以 (10 乘 乘 计数) 乘 (10 乘 乘 计数) 存入 结果
    result += d * (10 ** (cnt - 1))  # 结果累加 d 乘 (10 乘 乘 (计数 减 1))
    result += n % (10 ** (cnt2 - 1))  # 结果累加 (元素个数 对…取模 (10 乘 乘 (cnt2 减 1)))

    # Check overflow
    if result > MAX or result <= n:  # 若 结果 超过 MAX or 结果 不超过 元素个数
        return -1  # 返回 减 1
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(nextGreaterElement(1))  # 打印输出
