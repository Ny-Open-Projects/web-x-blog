# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
# LeetCode 113951689. 动态规划之 LCS — Python 版（最长公共子序列：DP 填表 + 回溯构造）


import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def lcs_length(a, b):  # 定义函数 lcs_length（参数：数组, b）
    m, n = len(a), len(b)  # 把 长度(数组), 长度(b) 写入 m, n
    dp = [
        [0] * (n + 1) for _ in range(m + 1)
    ]  # 把 [[0] 乘 (元素个数 加 1) for _ in range(映射表 加 1)] 存入 DP 表
    for i in range(1, m + 1):  # 让 下标 i 从 1 到 映射表 加 1 遍历
        for j in range(1, n + 1):  # 让 下标 j 从 1 到 元素个数 加 1 遍历
            if a[i - 1] == b[j - 1]:  # 若 数组[下标 i 减 1] 等于 b[下标 j 减 1]
                dp[i][j] = dp[i - 1][j - 1] + 1  # 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1 写入 dp[i][j]
            else:  # 否则
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]  # 返回 DP 表[映射表][元素个数]


def lcs_string(a, b):  # 定义函数 lcs_string（参数：数组, b）
    m, n = len(a), len(b)  # 把 长度(数组), 长度(b) 写入 m, n
    dp = [
        [0] * (n + 1) for _ in range(m + 1)
    ]  # 把 [[0] 乘 (元素个数 加 1) for _ in range(映射表 加 1)] 存入 DP 表
    for i in range(1, m + 1):  # 让 下标 i 从 1 到 映射表 加 1 遍历
        for j in range(1, n + 1):  # 让 下标 j 从 1 到 元素个数 加 1 遍历
            if a[i - 1] == b[j - 1]:  # 若 数组[下标 i 减 1] 等于 b[下标 j 减 1]
                dp[i][j] = dp[i - 1][j - 1] + 1  # 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1 写入 dp[i][j]
            else:  # 否则
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    out = []  # 把 [] 存入 out
    i, j = m, n  # 把 映射表, 元素个数 写入 i, j
    while i > 0 and j > 0:  # 循环，直到不满足「下标 i 超过 0 and 下标 j 超过 0」
        if a[i - 1] == b[j - 1]:  # 若 数组[下标 i 减 1] 等于 b[下标 j 减 1]
            out.append(a[i - 1])  # 把 数组[下标 i 减 1] 追加到列表尾部
            i -= 1  # 下标 i累减 1
            j -= 1  # 下标 j累减 1
        elif (
            dp[i - 1][j] >= dp[i][j - 1]
        ):  # 否则，若 DP 表[下标 i 减 1][下标 j] 不低于 DP 表[下标 i][下标 j 减 1]
            i -= 1  # 下标 i累减 1
        else:  # 否则
            j -= 1  # 下标 j累减 1
    return "".join(reversed(out))  # 返回 「」.join(reversed(out))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cases = [
        ("ABCBDAB", "BDCABA", 4),
        ("AGGTAB", "GXTXAYB", 4),
        ("abc", "abc", 3),
        ("", "abc", 0),
        ("abc", "xyz", 0),
    ]
    for a, b, want in cases:  # for 数组, b, want in cases:
        got = lcs_length(a, b)  # 把 lcs_length(数组, b) 存入 got
        assert got == want, f"lcs_length({a},{b})={got} want {want}"  # 断言校验
    for a, b in [("ABCBDAB", "BDCABA"), ("AGGTAB", "GXTXAYB")]:
        s = lcs_string(a, b)  # 把 lcs_string(数组, b) 存入 字符串
        assert len(s) == lcs_length(a, b), f"lcs_string length mismatch: {s}"  # 断言校验
        ia = ib = 0  # 把 ib 赋值为 0 存入 ia
        for ch in s:  # 逐个取出 字符串 的元素（字符）
            while (
                ia < len(a) and a[ia] != ch
            ):  # 循环，直到不满足「ia 小于 长度(数组) and 数组[ia] 不等于 字符」
                ia += 1  # ia累加 1
            while ib < len(b) and b[ib] != ch:  # 循环，直到不满足「ib 小于 长度(b) and b[ib] 不等于 字符」
                ib += 1  # ib累加 1
            assert ia < len(a) and ib < len(b), f"not a common subsequence: {s}"  # 断言校验
            ia += 1  # ia累加 1
            ib += 1  # ib累加 1
    print("PASS")  # 全部用例通过，输出 PASS
