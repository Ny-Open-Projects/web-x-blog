---
title: "[A289] 最长递增子序列 O(n log n)：patience 二分、路径重建与严格/非降的等号处理"
date: 2026-11-25
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A289 · 最长递增子序列 O(n log n)：patience 二分、路径重建与严格/非降的等号处理

> 难度:★★★★ | 标签:动态规划, 二分, LIS, 路径重建, 对拍

**问**（笔试·编程题）：LIS 的 O(n log n) 写法人人会背，面试官追问的是**语义**：① `tails` 数组到底存什么？为什么 `tails` 本身**不是**一条 LIS；② `bisect_left` 与 `bisect_right` 分别对应严格递增与非降（LNDS），等号处理错在哪；③ 如何用 `prev` 指针重建一条具体路径，更新 `tails` 时 `prev` 该指向谁；④ 与 O(n²) DP 在 40 组小规模（含大量重复值）上逐例对拍长度，并校验重建序列「严格递增 + 是原数组子序列」；⑤ 说清与 A007（最大子数组和·Kadane）、A009（第 K 大·快速选择）的分工——本题只回答「**用二分维护每长度最小结尾、并证明它够用**」。

**答**：① 分工：A007 是「连续子数组」的线性 DP，A009 是选择问题；LIS 是**子序列**（可不连续）问题，O(n²) DP 的定义是「以 i 结尾的最长长度」，而 O(n log n) 换了一个状态：`tails[k]` = 所有长度为 `k+1` 的递增子序列中**最小的结尾值**——注意它记录的是「结尾」而非「序列」，同一个 `tails` 可能由不同下标的元素拼成，所以 `tails` 内容本身不保证是原数组的子序列，直接输出它是常见错误。② 为什么只维护最小结尾就够：若长度 `k+1` 存在结尾 `x`，把结尾换成更小的 `y < x` 只会让后续更容易接上，不会损失任何可能性——这是「贪心替换」的正确性来源；`tails` 天然严格递增（长度更长必然要求结尾更大），才能二分。③ 等号：严格递增要求新元素 `x` 接在「结尾 < x」之后，用 `bisect_left` 找第一个 `>= x` 的位置覆盖；非降允许相等，用 `bisect_right` 找第一个 `> x` 的位置。以 `[2,2,2]` 为例：`bisect_left` 三次都命中下标 0，长度 1；`bisect_right` 依次追加到 1、2、3，长度 3——**一个符号决定答案差 3 倍**，题面必须逐字读「递增 / 非递减」。④ 重建：开 `prev[i]` 记录「i 接在哪个下标后面」，当 `x` 落到 `tails` 的位置 `j` 时，`prev[i] = tails_idx[j-1]`（长度 `j` 那条链的末尾），随后再更新 `tails[j]` 与 `tails_idx[j]`；最终从 `tails_idx[-1]` 沿 `prev` 回溯再反转。必须先写 `prev` 再覆盖 `tails_idx[j]`，顺序反了会指向自己。⑤ 对拍地基：O(n²) DP 的 `dp[i] = 1 + max(dp[j] for j<i and a[j]<a[i])` 是定义式，正确性不依赖任何贪心；随机值取 `0..5` 制造大量重复，专门打等号 bug；重建结果除长度外还要验「相邻严格递增」和「是子序列」，否则可能长度对但路径是拼出来的假链。

```python
# 全部标准库；LIS O(n log n)（严格/非降）+ 路径重建，与 O(n^2) DP 逐例对拍
import bisect
import random

def lis_len(a):
    """目标实现：tails[k] = 长度 k+1 的递增子序列的最小结尾值。"""
    tails = []
    for x in a:
        i = bisect.bisect_left(tails, x)   # 严格递增：第一个 >= x
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

def lnds_len(a):
    """非降版本：只把 bisect_left 换成 bisect_right。"""
    tails = []
    for x in a:
        i = bisect.bisect_right(tails, x)  # 允许相等：第一个 > x
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

def lis_path(a):
    """重建一条严格递增子序列（长度等于 lis_len）。"""
    n = len(a)
    tails, tails_idx = [], []              # tails 值 + 对应原数组下标
    prev = [-1] * n
    for i, x in enumerate(a):
        j = bisect.bisect_left(tails, x)
        if j > 0:
            prev[i] = tails_idx[j - 1]     # 接在长度 j 的链尾后
        if j == len(tails):
            tails.append(x)
            tails_idx.append(i)
        else:
            tails[j] = x                   # 覆盖：更小的结尾，机会更多
            tails_idx[j] = i
    if not tails:
        return []
    out, k = [], tails_idx[-1]
    while k != -1:
        out.append(a[k])
        k = prev[k]
    return out[::-1]

def lis_dp(a):
    """参考实现：定义式 O(n^2)，返回长度与一条路径。"""
    n = len(a)
    if n == 0:
        return 0, []
    dp, pre = [1] * n, [-1] * n
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                pre[i] = j
    L = max(dp)
    k = dp.index(L)
    seq = []
    while k != -1:
        seq.append(a[k])
        k = pre[k]
    return L, seq[::-1]

def lnds_dp(a):
    """非降参考实现：只在比较处去掉等号限制。"""
    n = len(a)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j] <= a[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    return max(dp) if dp else 0

def is_subseq(seq, a):
    it = iter(a)
    return all(any(v == x for x in it) for v in seq)

if __name__ == "__main__":
    rng = random.Random(2891)

    # 1) 40 组随机（值域 0..5 制造重复）长度对拍 + 路径合法性校验
    for _ in range(40):
        a = [rng.randint(0, 5) for _ in range(rng.randint(0, 12))]
        L, ref = lis_dp(a)
        assert lis_len(a) == L, (a, lis_len(a), L)
        path = lis_path(a)
        assert len(path) == L, (a, path, L)
        assert all(path[t] < path[t + 1] for t in range(len(path) - 1)), path
        assert is_subseq(path, a), (path, a)
        assert lnds_len(a) == lnds_dp(a), (a, "lnds")
    print("LIS 对拍: 40 组随机（含大量重复）长度/路径/非降三线全等 ✅")

    # 2) 边界：空、单元素、全相同、严格递减、已递增
    assert lis_len([]) == 0 and lis_path([]) == [] and lis_len([9]) == 1 and lis_path([9]) == [9]
    assert lis_len([4, 4, 4, 4]) == 1 and lis_path([4, 4, 4, 4]) == [4] and lnds_len([4, 4, 4, 4]) == 4
    assert lis_len([5, 4, 3, 2, 1]) == 1 and lis_len([1, 2, 3, 4, 5]) == 5
    assert lnds_len([1, 2, 2, 3, 3]) == 5
    print("边界断言: 空/单元素/全相同/递减/递增/等号 全过 ✅")

    # 3) tails 不是答案的实证：a=[5,6,1] 得 tails=[1,6]，长度对但不是子序列
    a = [5, 6, 1]
    tails = []
    for x in a:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    assert tails == [1, 6] and not is_subseq(tails, a)
    print("语义实证: tails=[1,6] 长度对但非子序列，必须靠 prev 重建 ✅")

    # 4) 长序列性能与规模：20000 个随机值，O(n log n) 秒级完成
    big = [rng.randint(0, 10 ** 6) for _ in range(20000)]
    assert lis_len(big) >= 1 and lnds_len(big) >= lis_len(big)   # 放宽等号只会更长
    print("对拍通过：LIS 40 组随机 + 7 条边界 + tails 语义实证全绿")
```

**追问**：1) 举一个 `tails` 内容不是合法子序列的反例？—— `a = [5, 6, 1]`：扫描 `5` 得 `tails=[5]`，扫描 `6` 追加成 `[5,6]`，扫描 `1` 时 `bisect_left` 命中下标 0，把 5 覆盖成 1，最终 `tails = [1, 6]`。长度 2 是对的，但 `[1,6]` 不是原数组的子序列（1 出现在 6 之后）。这正是「`tails` 只维护每长度的最小结尾、丢失了顺序信息」的实证，所以重建必须靠 `prev` 指针，不能直接输出 `tails`。2) 重建时 `prev` 会不会指向一个「未来才被覆盖」的下标导致链断裂？—— 不会，因为 `prev[i]` 指向的是长度 `j` 的链尾，而每条长度的链尾只会被**更晚**的下标覆盖，`prev` 一旦写下就固定指向那个历史下标，后续覆盖只影响 `tails_idx[j]` 的新值、不影响旧链；所以从最终 `tails_idx[-1]` 回溯，每一步都是「当前的链尾」，天然单调递减，回溯必终止于 `-1`。3) 严格递增和非降在工程里哪个更常见？—— 取决于「相等元素算不算冲突」：求「最多能选多少个互不相同的值」用严格 LIS；求「最长可保留的已排序序列（重复可保留）」用非降。面试里若题面只写「递增」，先按严格做，并主动说一句「如果允许相等，把 `bisect_left` 换成 `bisect_right`、DP 的 `<` 换成 `<=`」——**主动暴露等号这个开关**，比等面试官追问更能证明你真的理解 `tails` 语义。
