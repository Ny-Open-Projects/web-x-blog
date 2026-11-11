# 来源（blog）：找到所有数组中消失的数字 — 用集合标记后按顺序收集 1..n 中缺失者
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def find_disappeared_numbers(nums):  # 定义函数 find_disappeared_numbers（参数：数组）
    s = set(nums)  # 把 set(数组) 存入 字符串
    return [i for i in range(1, len(nums) + 1) if i not in s]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cases = [
        ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
        ([1, 1], [2]),
    ]
    for nums, want in cases:  # for 数组, want in cases:
        got = find_disappeared_numbers(nums)  # 把 find_disappeared_numbers(数组) 存入 got
        assert got == want, f"findDisappearedNumbers({nums})={got} want {want}"  # 断言校验
    print("PASS")  # 全部用例通过，输出 PASS
