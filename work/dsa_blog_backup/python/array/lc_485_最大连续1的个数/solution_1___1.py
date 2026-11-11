# 来源（blog）：LeetCode 485. 最大连续1的个数 — 一次扫描维护当前连续段与最优值
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def find_max_consecutive_ones(nums):  # 定义函数 find_max_consecutive_ones（参数：数组）
    best = 0  # 把 0 存入 当前最优
    cur = 0  # 把 0 存入 当前值
    for x in nums:  # 逐个取出 数组 的元素（x）
        if x == 1:  # 若 x 等于 1
            cur += 1  # 当前值累加 1
            if cur > best:  # 若 当前值 超过 当前最优
                best = cur  # 把 当前值 存入 当前最优
        else:  # 否则
            cur = 0  # 把 0 存入 当前值
    return best  # 返回 当前最优


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cases = [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2),
        ([0], 0),
    ]
    for nums, want in cases:  # for 数组, want in cases:
        got = find_max_consecutive_ones(nums)  # 把 find_max_consecutive_ones(数组) 存入 got
        assert got == want, f"got {got} expected {want}"  # 断言校验
    print("PASS")  # 全部用例通过，输出 PASS
