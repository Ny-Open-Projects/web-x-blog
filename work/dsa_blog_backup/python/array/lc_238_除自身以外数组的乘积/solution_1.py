# 来源（blog）：LeetCode 238 除自身以外数组的乘积 — 前缀积 × 后缀积
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def product_except_self(nums):  # 定义函数 product_except_self（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    out = [1] * n  # 把 [1] 乘 元素个数 存入 out
    p = 1  # 把 1 存入 节点
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        out[i] = p  # 把 节点 写入 out[i]
        p *= nums[i]  # 把 数组[下标 i] 写入 p *
    p = 1  # 把 1 存入 节点
    for i in range(n - 1, -1, -1):  # 让 下标 i 从 元素个数 减 1 倒数回去（每步减 1）
        out[i] *= p  # 把 节点 写入 out[i] *
        p *= nums[i]  # 把 数组[下标 i] 写入 p *
    return out  # 返回 out


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([0, 0], [0, 0]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ]
    for inp, want in cases:  # for inp, want in cases:
        got = product_except_self(inp)  # 把 product_except_self(inp) 存入 got
        assert got == want, f"in={inp} want={want} got={got}"  # 断言校验
    print("PASS")  # 全部用例通过，输出 PASS
