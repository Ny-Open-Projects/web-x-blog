# 来源（blog）：LeetCode 169. 多数元素 — 方案1：哈希计数取最大值（Counter.most_common(1)）
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def majority_element(nums):  # 定义函数 majority_element（参数：数组）
    cnt = {}  # 把 {} 存入 计数
    for v in nums:  # 逐个取出 数组 的元素（值）
        cnt[v] = cnt.get(v, 0) + 1  # 把 计数 查找 值, 0) 加 1 写入 cnt[v]
    best = 0  # 把 0 存入 当前最优
    best_cnt = -1  # 把 减 1 存入 best_cnt
    for k, c in cnt.items():  # for 下标 k, 字符 in 计数.items():
        if c > best_cnt:  # 若 字符 超过 best_cnt
            best = k  # 把 下标 k 存入 当前最优
            best_cnt = c  # 把 字符 存入 best_cnt
    return best  # 返回 当前最优


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
    ]
    for inp, want in cases:  # for inp, want in cases:
        got = majority_element(inp)  # 把 majority_element(inp) 存入 got
        assert got == want, f"majorityElement({inp}) = {got}, want {want}"  # 断言校验
    print("PASS")  # 全部用例通过，输出 PASS
