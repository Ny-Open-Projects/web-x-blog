---
title: "[A295] KMP 前缀函数：回退链、重叠匹配与 str.find 对拍"
date: 2026-11-25
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A295 · KMP 前缀函数：回退链、重叠匹配与 str.find 对拍

> 难度:★★★★ | 标签:KMP, 前缀函数, 字符串匹配, 重叠匹配, 对拍

**问**（笔试·编程题）：实现 `prefix_function(p)` 与 `kmp_search(text, pat)`，返回模式在文本中**所有**出现位置（含重叠），要求：① `pi[i]` 的精确含义，为什么必须是「真前后缀」、`pi[0]` 为什么恒为 0；② 失配时 `j = pi[j-1]` 的回退为什么不会漏掉任何可能的匹配，为什么 while 的总次数是 O(n) 而不是退化成 O(n²)，请用「j 的势能」讲清楚；③ 匹配成功后为什么写 `j = pi[j-1]` 而不是清零，各自的后果是什么，举一个能区分两者的例子；④ 边界：空模式、模式长于文本、空文本、`aaaa` 找 `aa`、`abababab` 找 `abab`、无匹配；空模式为什么必须显式约定返回什么，和 `str.find("")` 的行为差在哪；⑤ 与 `str.find` 循环做 300 组随机对拍（小字母表制造重叠），再用 pi 的三条性质（长度上界、前后缀真的相等、最长性）反向校验，跑 10 万全 a 的极值，最后说清 KMP 与 A278 Rabin-Karp、Python 内置 `find` 的取舍。

**答**：① `pi[i]` 是子串 `p[0..i]` 的**最长相等真前后缀**长度：真前缀不含最后一个字符、真后缀不含第一个字符。必须强调「真」，否则任意串都满足「整个串等于整个串」，`pi[i]=i+1` 恒成立，回退信息为零；`pi[0]` 对应长度为 1 的串，它没有任何真前后缀，所以恒为 0。② 失配时 `p[i] != p[j]`，说明「当前候选长度 j」不成立，下一个候选只能是 `p[0..j-1]` 的最长 border，即 `pi[j-1]`；为什么不会漏？因为任何长度 `L < j` 的相等前后缀，都同时是 `p[0..j-1]` 的前缀和后缀，必然出现在 `j → pi[j-1] → pi[pi[j-1]-1] → …` 这条回退链上，链枚举了全部候选。复杂度用势能看：i 每轮加 1，j 每轮最多加 1，而每次 `j = pi[j-1]` 至少让 j 减 1，所以 j 的总下降量不超过总上升量 ≤ n，while 总执行次数 O(n)，加上外层 O(n)，整体 O(n+m)——注意是**总次数**摊还，单次失配仍可能连续回退很多步。③ 匹配到 `j==m` 后记下起点 `i-m+1`；若把 j 清零，下一次匹配只能从当前位置重新开始，会漏掉与当前匹配**重叠**的起点：`aaaa` 找 `aa`，清零只能得到 0 和 2，正确答案是 0、1、2；写 `j = pi[m-1]` 则回退到「已匹配部分的最长 border」，对 `aa` 而言 `pi[1]=1`，于是从 1 继续，正好补上重叠位置。④ 空模式是唯一的语义分歧点：数学上它在每个边界都匹配，应返回 `[0,1,…,n]` 共 n+1 个位置；但 `"abc".find("")` 只返回 0，`str.find` 的定义是「第一个出现位置」，两者不是同一件事。代码里选择「每个边界」并注释清楚，对拍只对非空模式跑，否则会假失败。模式长于文本、空文本 + 非空模式都返回 `[]`；`aaaa` 找 `aa` 返回 `[0,1,2]`；`abababab` 找 `abab` 返回 `[0,2,4]`；无匹配返回 `[]`。⑤ 对拍用字母表 `ab`/`abc`/`aab` 制造大量重叠，300 组随机文本长度 0..30、模式长度 1..6，与「反复 `find` 且 start 每次 +1」的暴力逐元素比较；再用 100 组随机串校验 pi 的三条性质：`0<=pi[i]<=i`、`p[:pi[i]] == p[i+1-pi[i]:i+1]`、以及 `pi[i]+1` 不再是 border（最长性）；极值用 10 万全 a 文本配 500 长模式，命中数必须是 `n-m+1`。取舍：KMP 最坏 O(n+m)、无哈希碰撞、能顺带求所有重叠位置与最小循环节 `n-pi[n-1]`（还要补 `n % p == 0` 才是真周期）；Rabin-Karp 平均 O(n+m)、实现短、天然适合多模式与二维，但有碰撞必须二次校验；Python 的 `str.find` 是 C 实现的 Two-Way 算法，常数极小，工程里直接用内置函数即可——KMP 在面试里的价值是证明你能把匹配讲到线性、能解释回退链，而不是让你在生产里替换 `find`。

```python
# 全部标准库；KMP 前缀函数与全部匹配位置，与 str.find 循环对拍，并用性质断言校验 pi
import random


def prefix_function(p):
    """pi[i] = p[:i+1] 的最长相等真前后缀长度（不含自身）。"""
    pi = [0] * len(p)
    for i in range(1, len(p)):
        j = pi[i - 1]
        while j and p[i] != p[j]:
            j = pi[j - 1]          # 回退到次长候选，不丢解
        if p[i] == p[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_search(text, pat):
    """返回 pat 在 text 中所有起始下标（含重叠）。空模式约定匹配每个边界 0..n。"""
    n, m = len(text), len(pat)
    if m == 0:
        return list(range(n + 1))
    pi = prefix_function(pat)
    res, j = [], 0
    for i in range(n):
        while j and text[i] != pat[j]:
            j = pi[j - 1]
        if text[i] == pat[j]:
            j += 1
        if j == m:
            res.append(i - m + 1)
            j = pi[j - 1]          # 允许重叠：用 pi 回退而不是清零
    return res


def brute_find(text, pat):
    """参考实现：反复调用 str.find，start 每次 +1 以保留重叠匹配。"""
    out, start = [], 0
    while True:
        k = text.find(pat, start)
        if k == -1:
            return out
        out.append(k)
        start = k + 1


if __name__ == "__main__":
    rng = random.Random(2951)

    # 1) 300 组随机（小字母表制造大量重叠）与 str.find 对拍
    for _ in range(300):
        alpha = rng.choice(["ab", "abc", "aab"])
        text = "".join(rng.choice(alpha) for _ in range(rng.randint(0, 30)))
        pat = "".join(rng.choice(alpha) for _ in range(rng.randint(1, 6)))
        assert kmp_search(text, pat) == brute_find(text, pat), (text, pat)
    print("KMP 对拍: 300 组随机文本/模式 vs str.find 循环，全等 ✅")

    # 2) pi 性质自校验：长度上界 + 前后缀真的相等 + 是最长的（pi[i]+1 不成立）
    for _ in range(100):
        s = "".join(rng.choice("abc") for _ in range(rng.randint(1, 40)))
        pi = prefix_function(s)
        for i, v in enumerate(pi):
            assert 0 <= v <= i, (s, i, v)
            if v:
                assert s[:v] == s[i + 1 - v:i + 1], (s, i, v)
            if v < i:
                assert s[:v + 1] != s[i - v:i + 1], (s, i, v)
    print("pi 性质: 100 组随机串的长度上界/前后缀相等/最长性 全部成立 ✅")

    # 3) 边界：空模式、模式长于文本、全同字符、单字符、无匹配、重叠匹配
    assert kmp_search("abc", "") == [0, 1, 2, 3] == list(range(4))
    assert kmp_search("ab", "abc") == []
    assert kmp_search("", "a") == [] and kmp_search("", "") == [0]
    assert kmp_search("aaaa", "aa") == [0, 1, 2]          # 重叠匹配
    assert kmp_search("aaaa", "a") == [0, 1, 2, 3]
    assert kmp_search("abcabcabd", "abcabd") == [3]
    assert kmp_search("abababab", "abab") == [0, 2, 4]    # 周期串重叠
    assert prefix_function("aabaaab") == [0, 1, 0, 1, 2, 2, 3]
    print("边界: 空模式/模式过长/空文本/全同/重叠/周期串 全过 ✅")

    # 4) 最小循环节：n - pi[-1]，且只有能整除 n 时才是真正的重复节
    for s, want in [("abcabcabc", 3), ("aaaa", 1), ("ababab", 2), ("abcd", 4), ("aabaab", 3)]:
        p = len(s) - prefix_function(s)[-1]
        assert p == want and len(s) % p == 0, (s, p)
    print("最小循环节: abcabcabc→3 / aaaa→1 / ababab→2 / abcd→4 / aabaab→3 ✅")

    # 5) 极值：10 万全 a 文本 + 500 长模式，匹配数 (n-m+1)，首尾下标正确
    n, m = 100000, 500
    text, pat = "a" * n, "a" * m
    hits = kmp_search(text, pat)
    assert len(hits) == n - m + 1 and hits[0] == 0 and hits[-1] == n - m
    assert kmp_search(text, "a" * (n + 1)) == []
    pi = prefix_function(pat)
    assert pi[-1] == m - 1 and m - pi[-1] == 1
    print("极值: 10 万全 a 文本 × 500 长模式，%d 个重叠命中，首尾正确 ✅" % len(hits))

    print("对拍通过：KMP 300 组随机 + 100 组 pi 性质 + 边界 + 循环节 + 10 万极值全绿")
```

**追问**：1) 在 10 亿字符的文本里找一个模式，KMP 是最优吗？—— 理论线性但不是实践最优：KMP 的访存模式是「逐字符 + 回退」，缓存不友好；实际常用 Boyer-Moore（坏字符 + 好后缀，平均亚线性，能大段跳过）或 CPython 的 Two-Way。KMP 的优势是流式、最坏可证、能顺带求 border/循环节/前后缀信息，适合作为其他算法（AC 自动机、Z 函数）的基础。2) 多模式匹配怎么办？—— 每个模式各跑一遍 KMP 是 O(k(n+m))，不可取；标准解法是 Trie + fail 指针，即 Aho-Corasick：把所有模式建 Trie，BFS 求每个节点的 fail（本质是多串版的 pi），然后一遍扫文本，复杂度 O(n + 总模式长 + 命中数)。A277 讲了 Trie 的静态前缀统计，AC 自动机是在它上面加「失配跳转」。3) 最小循环节直接说 `n - pi[n-1]` 对吗？—— 不完全对。`p = n - pi[n-1]` 是「最长 border 对应的周期」，只有当 `n % p == 0` 时，串才真正由长度为 p 的块整周期重复；否则它只是「有长度为 p 的周期」但末尾不完整（如 `abcd` 的 p=4 等于自身、`aabaab` 的 p=3 整除 6 才是真循环节）。面试必须补这个整除条件，否则会被追问打回。
