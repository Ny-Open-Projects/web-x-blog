---
title: [A244] 文本 diff 与最小编辑脚本：Myers 算法与可读输出
date: 2026-11-23
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A244 · 最小编辑脚本

> 难度:★★★★ | 标签:diff, Myers, 动态规划, 编辑距离

**问**（笔试·编程题）：实现行级文本 diff，输出**最短**编辑脚本（只允许 insert/delete，不允许 replace），并把脚本渲染成人能读的「旧行号 / 新行号 / 操作 / 内容」。约束与追问：① 为什么不用 LCS 的 O(NM) DP，Myers 的 `k` 对角线和 `D` 分别是什么、为什么是 O((N+M)·D)；② 回溯怎么还原路径、为什么要存每轮的 V 快照、内存代价多大、线性空间变体牺牲了什么；③ 10 万行文件怎么处理（前后缀裁剪、行哈希、分块与 hunk）；④ 已有一行只改了一个词，行级 diff 输出「删一行 + 加一行」合理吗，怎么做到行内高亮。注意 `difflib` 已能算 diff（Q2100），本题要的是算法本体与最短性证明。

**答**：① 为什么不用 DP：LCS 的 O(NM) 时间在万行级就是上亿次比较，10 万行直接不可行；空间即使压到 O(min(N,M)) 也无法回溯出完整脚本（要存方向或分治）。Myers 的洞察是**编辑距离 D 通常远小于 N+M**（两份配置/两版代码的差异行占比很小），所以沿「编辑步数」而不是「矩阵格子」推进，时间 O((N+M)·D)，`D` 小的时候是线性级。② 坐标含义：`k = x - y` 是第几条对角线——删除让 x 增（k 从 k−1 来）、新增让 y 增（k 从 k+1 来），`V[k]` 记录该对角线当前能到达的**最大 x**；第 `d` 轮只在 `|k| ≤ d` 且与 `d` 同奇偶的对角线上扩展，先比较「从 k−1 下移（删除）」与「从 k+1 右移（新增）」哪个能拿到更大的 x，取大者，再沿对角线吃掉所有相同行（snake）。某一轮 `x ≥ N 且 y ≥ M` 时，该轮号就是最短编辑距离。③ 回溯与内存：必须保存**每一轮的 V 快照**，从终点反推每步是 delete / insert / keep；快照总大小 O(D²)，D 很大时内存比时间先爆。线性空间变体用分治找「中间 snake」递归两半，空间降到 O(N+M)，代价是实现复杂度高一个量级、常数变大；git 的默认实现还有启发式截断（`--minimal` 才严格最短）。④ 工程侧：先裁掉公共前缀与后缀（通常能砍掉 90% 以上），再对中间段跑算法并按行哈希比较（避免长行逐字符比较）；大文件按 hunk 分块输出、上下文默认 3 行；设置 D 上限，超过就降级成「整段替换」，防止最坏情况 O((N+M)²)。⑤ 可读性：行级 diff 对「改一个词」会输出一删一增，工程上做**两级 diff**——先按行对齐，再对配对的删/增行做词级或字符级比较，输出行内高亮；但「一行拆多行」「多行合一行」的配对本身有歧义，所以工业工具只做启发式配对，不追求全局最优（最小 ≠ 最好读，patience/histogram 算法甚至主动放弃最小性换人类直觉）。

```python
# 全部标准库；Myers 差分：O((N+M)·D) 求最短编辑脚本，再渲染成可读行
def myers(a, b):
    """返回 (d, ops)。ops: ('=', i, j) 保留 / ('-', i, None) 删除 / ('+', None, j) 新增。"""
    n, m = len(a), len(b)
    v = {1: 0}
    trace = []
    for d in range(n + m + 1):
        trace.append(v.copy())
        for k in range(-d, d + 1, 2):
            if k == -d or (k != d and v.get(k - 1, -1) < v.get(k + 1, -1)):
                x = v.get(k + 1, 0)
            else:
                x = v.get(k - 1, -1) + 1
            y = x - k
            while x < n and y < m and a[x] == b[y]:
                x += 1
                y += 1
            v[k] = x
            if x >= n and y >= m:
                return d, _backtrack(trace, a, b)
    raise AssertionError("unreachable")


def _backtrack(trace, a, b):
    x, y = len(a), len(b)
    ops = []
    for d in range(len(trace) - 1, -1, -1):
        v = trace[d]
        k = x - y
        if d == 0:
            while x > 0 and y > 0:
                x -= 1
                y -= 1
                ops.append(("=", x, y))
            break
        if k == -d or (k != d and v.get(k - 1, -1) < v.get(k + 1, -1)):
            prev_k = k + 1
        else:
            prev_k = k - 1
        prev_x = v.get(prev_k, 0)
        prev_y = prev_x - prev_k
        while x > prev_x and y > prev_y:      # 先回退对角线上的相同行
            x -= 1
            y -= 1
            ops.append(("=", x, y))
        if x == prev_x:                        # 从 k+1 斜着过来 = 新增 b[y]
            y -= 1
            ops.append(("+", x, y))
        else:                                  # 从 k-1 斜着过来 = 删除 a[x]
            x -= 1
            ops.append(("-", x, None))
    ops.reverse()
    return ops


def lcs_len(a, b):
    """O(NM) 的 LCS 长度，只用来交叉验证 Myers 的最短性。"""
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b, 1):
            cur.append(prev[j - 1] + 1 if x == y else max(prev[j], cur[j - 1]))
        prev = cur
    return prev[-1]


def render(a, b, ops):
    """行级可读输出：旧行号 / 新行号 / 内容。"""
    out = []
    for kind, i, j in ops:
        if kind == "=":
            out.append(f"  {i + 1:>3} {j + 1:>3} | {a[i]}")
        elif kind == "-":
            out.append(f"- {i + 1:>3}     | {a[i]}")
        else:
            out.append(f"+     {j + 1:>3} | {b[j]}")
    return out


def apply_ok(a, b, ops):
    old = [a[i] for kind, i, j in ops if kind != "+"]
    new = [b[j] for kind, i, j in ops if kind != "-"]
    return old == a and new == b


if __name__ == "__main__":
    a = "the quick brown fox jumps over".split()
    b = "the quick red fox jumped over the lazy dog".split()

    d, ops = myers(a, b)
    assert apply_ok(a, b, ops), "编辑脚本回放必须还原两段文本"
    expected = len(a) + len(b) - 2 * lcs_len(a, b)
    assert d == expected == sum(1 for k, _, _ in ops if k != "=")
    assert d == 7
    print("Myers D =", d, "= N+M-2LCS，编辑脚本回放一致 ✅")
    for line in render(a, b, ops):
        print(line)

    assert myers([], []) == (0, [])
    d1, ops1 = myers([], ["x"])
    assert d1 == 1 and ops1 == [("+", 0, 0)]
    d2, ops2 = myers(["same", "line"], ["same", "line"])
    assert d2 == 0 and [k for k, _, _ in ops2] == ["=", "="]
    print("边界: 空/空、空/1、完全相同 均正确 ✅")

    for x, y in [("abcabba", "cbabac"), ("kitten", "sitting"), ("aaaa", "aa")]:
        x, y = list(x), list(y)
        dd, oo = myers(x, y)
        assert apply_ok(x, y, oo)
        assert dd == len(x) + len(y) - 2 * lcs_len(x, y), (x, y, dd)
    print("随机小样本: 与 LCS 下界全部一致（最短性校验通过）✅")
```

**追问**：1) Myers 的最坏情况什么时候发生，怎么防？——两段文本几乎没有公共行时 `D ≈ N+M`，时间退化到 O((N+M)²)，同时 V 快照的内存 O(D²) 会先撑爆。防法：先算长度差作为 `D` 的下界、设 `D` 上限（超限降级为整段删增）、裁前后缀、按行哈希分块；真正的通用做法是线性空间 Myers（分治），把内存压到 O(N+M)。2) 为什么 git diff 的结果不一定是「最小」编辑脚本？——git 默认的 Myers 带启发式（找到足够好的路径就收），只有 `--minimal` 才保证最短；`patience` / `histogram` 更是彻底放弃最小性，改用「唯一行先对齐」的策略，因为最小脚本经常把代码块切得七零八落，人类读起来更费劲。这是「算法最优」与「可读性最优」的取舍。3) 行级 diff 说「删 1 行、加 1 行」，但实际只改了一个词，怎么优化？——两级 diff：行对齐后，把相邻的删除块与新增块按相似度配对（相似度高才配对，否则视为独立增删），对配对行再做词级/字符级 diff 输出行内高亮。注意配对歧义（一行拆成三行时该跟谁配）没有唯一正确答案，工具只能用启发式，并允许用户切换算法。

## 背诵要点
1. Myers 沿 `k = x - y` 对角线推进，`V[k]` 存该线最远 x；第 d 轮的 snake 吃相同行，终点轮号即最短编辑距离，时间 O((N+M)·D)。
2. 回溯要存每轮 V 快照，内存 O(D²)；线性空间变体用分治换 O(N+M)，代价是复杂度与常数。
3. 工程四件套：裁前后缀 + 行哈希 + D 上限降级 + hunk 分块；可读性靠两级 diff（行级对齐后行内再 diff），最小 ≠ 最好读。

## 复盘追问
1. 两份 10 万行文件只有 3 行不同，但 Myers 跑了 8 秒，问题在哪？——如果已裁前后缀还慢，通常是「差异分散在文件各处」导致 D 不小，加上每轮 `dict` 快照复制的常数开销；改用数组 + 只保留必要轮次、或先按块哈希对齐（rsync 式），把大文件切成同构块后再逐块 diff。
2. 为什么「只允许 insert/delete」也能表达「修改」？（提示：修改 = 删旧行 + 增新行，编辑距离因此是 LCS 的补集：`d = N + M - 2·LCS`；允许 replace 会让距离定义变成另一套（Levenshtein），最短脚本不再等价于 LCS，代价模型也不同）
