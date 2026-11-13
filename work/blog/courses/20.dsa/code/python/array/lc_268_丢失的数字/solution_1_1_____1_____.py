# 来源（blog）：丢失的数字 — 高斯求和 - 总和差值
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def missing_number(nums):  # 定义函数 missing_number（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    return n * (n + 1) // 2 - sum(nums)  # 返回 元素个数 乘 (元素个数 加 1) 除以 除以 2 减 累计和(数组)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ]
    for nums, want in cases:  # for 数组, want in cases:
        got = missing_number(nums)  # 把 missing_number(数组) 存入 got
        assert got == want, f"missingNumber({nums})={got} want {want}"  # 断言校验
    print("PASS")  # 全部用例通过，输出 PASS
