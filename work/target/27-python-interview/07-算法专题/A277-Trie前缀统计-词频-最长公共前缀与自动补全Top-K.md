---
title: [A277] Trie 前缀统计：词频、最长公共前缀与自动补全 Top-K
date: 2026-11-24
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A277 · Trie 的前缀统计三件套：词频、LCP 与自动补全 Top-K

> 难度:★★★★ | 标签:Trie, 前缀统计, 词频, 最长公共前缀, 自动补全, Top-K

**问**（笔试·编程题）：搜索框输入「py」要 200ms 内给出 10 个候选词——面试官要的不是「知道 Trie 是树」，而是**统计能力的实现与代价账**：① 实现 Trie：插入（重复词累计词频而非拒绝）、`count_end(word)` 精确词频、`count_with_prefix(p)` 前缀命中数，两个计数都在**插入时**沿路径维护（`end` 记词频、`prefix` 记经过次数），查询 O(|p|)；② `lcp_all()`：求当前词集的**最长公共前缀**——利用「分叉/有词结尾即停」的结构性质，不写两两比较；③ `autocomplete(prefix, k)`：按词频降序（频次相同按字典序）返回前缀下 Top-K 补全，与 Counter 暴力基线逐元素对账；④ 词集含「一个词是另一个的前缀」（如 app/applet）、含重复插入、含全集单叉链三种边界断言；⑤ 说清与 Q2440（Trie 路由器：按 `/` 分段的段级匹配、静态段优先于参数段）、Q2788（前缀树做事件序列的路径归并与 Top-K 序列）的分工——本题只回答「**字符级 Trie 的词频/前缀计数/LCP/补全 Top-K 的实现与维护代价**」。

**答**：① 分工：Q2440 的 Trie 节点是「路径段 → 子路由」，匹配到段就查 handler，考的是路由裁决优先级；Q2788 把整个访问序列当一个词压进前缀树，考的是序列压缩；本题回到最朴素的字符级 Trie，考的是**把「统计」从查询期挪到写入期**——这是三张卡真正分岔的地方。② 两个计数器的落点：`end` 只在词尾节点 +1（重复插入累加，词频天然是多重集），`prefix` 从根开始每个途经节点都 +1——插入 O(L) 顺手做掉，查询就是一次下走。反过来「查询时 DFS 子树累加」也能得到同样数字，但每次查询 O(子树大小)：搜索框这种读远多于写的场景，前移维护是唯一正解；代价是**删除必须同步 -1**（且减到 0 的节点回不回收是内存与简单性的取舍），只加不减的词频账本则会随时间膨胀成「历史热度」而非「当前热度」。③ LCP 的结构性质：从根下走，只要当前节点**恰好一个孩子且不是任何词的结尾**就继续——一旦分叉（两个词在这是分歧点）或停止（短词到此结束，如 app/applet 的 LCP 是 app 而非 applet），立即收手。两两比较是 O(n·L)，结构判定是 O(LCP 长度)，且天然处理「词是另一词前缀」的边界——这个边界恰好是两两比较版最容易写错的地方。④ 自动补全：走到前缀节点后 DFS 整棵子树收集 `(词, 词频)`，按 `(-词频, 词)` 排序取前 K——与 Counter 暴力基线（全量词扫 startswith 再排序）结果逐元素相等，复杂度从 O(N) 降到 O(子树大小 + M log M)（M 为候选数）；K 很小时可换堆省掉全排序，但候选池本身（子树 DFS）才是大头，排序优化是次要项。⑤ 追问里再展开「预挂 Top-K 汇总」的代价账与 Trie vs 有序数组的选型边界。

```python
# 全部标准库；Trie 前缀统计：词频/前缀计数写入期维护 + LCP 结构判定 + 补全 Top-K 对账
from collections import Counter


class TrieNode:
    __slots__ = ("children", "end", "prefix")

    def __init__(self):
        self.children = {}
        self.end = 0      # 以此节点结尾的词频（重复插入累加）
        self.prefix = 0   # 经过此节点的词总数（含结尾），前缀计数的落点


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        node.prefix += 1
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
            node.prefix += 1
        node.end += 1

    def _walk(self, s):
        node = self.root
        for ch in s:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def count_end(self, word):
        """精确词频：O(|word|)。"""
        node = self._walk(word)
        return node.end if node else 0

    def count_with_prefix(self, p):
        """前缀命中数：O(|p|)——查询期不再扫任何子树。"""
        node = self._walk(p)
        return node.prefix if node else 0

    def lcp_all(self):
        """全集最长公共前缀：单叉且无词尾才继续，分叉/短词即停。"""
        node, out = self.root, []
        while len(node.children) == 1 and node.end == 0:
            (ch, nxt), = node.children.items()
            out.append(ch)
            node = nxt
        return "".join(out)

    def autocomplete(self, prefix, k):
        """Top-K 补全：频次降序，同频字典序升序。"""
        node = self._walk(prefix)
        if node is None:
            return []
        out, stack = [], [(node, prefix)]
        while stack:
            cur, word = stack.pop()
            if cur.end:
                out.append((word, cur.end))
            for ch in sorted(cur.children, reverse=True):   # 逆序入栈=正序出栈
                stack.append((cur.children[ch], word + ch))
        out.sort(key=lambda wc: (-wc[1], wc[0]))
        return out[:k]


def brute(t, words):
    """Counter 暴力基线：全量扫 + 排序。"""
    cnt = Counter(words)
    cand = [(w, c) for w, c in cnt.items() if w.startswith(t)]
    cand.sort(key=lambda wc: (-wc[1], wc[0]))
    return cand


if __name__ == "__main__":
    words = ["python", "pytorch", "py", "py", "py", "python",
             "pycache", "pyc", "pyc", "pypy", "java", "pyenv"]
    t = Trie()
    for w in words:
        t.insert(w)

    # 1) 词频与前缀计数 vs 暴力基线
    cnt = Counter(words)
    for w in ("py", "python", "pyc", "java", "java8"):
        assert t.count_end(w) == cnt[w], w
    for p in ("p", "py", "pyt", "pyc", "j", "z"):
        expect = sum(1 for w in words if w.startswith(p))
        assert t.count_with_prefix(p) == expect, p
    print("词频/前缀计数: count_end + count_with_prefix 与 Counter 基线全等 ✅")

    # 2) LCP：p* 家族公共前缀 py（java 在根处分叉故不影响？不对——单叉才走）
    assert t.lcp_all() == "", "java 与 p* 在根分叉，LCP 应为空"
    del_words = [w for w in words if not w.startswith("j")]
    t2 = Trie()
    for w in del_words:
        t2.insert(w)
    assert t2.lcp_all() == "py", t2.lcp_all()
    print("LCP: 全集含 java 时为空串，剔除后为 'py'（结构判定）✅")

    # 3) 补全 Top-K 与暴力基线逐元素相等（含同频字典序裁决）
    for p in ("py", "pyc", "", "z"):
        got = t.autocomplete(p, 3)
        want = brute(p, words)[:3]
        assert got == want, (p, got, want)
    assert t.autocomplete("z", 5) == []
    print("补全 Top-3: 'py'→%s 与基线全等 ✅" % (t.autocomplete("py", 3),))

    # 4) 前缀词边界：app/applet，LCP 停在词尾节点
    t3 = Trie()
    for w in ("app", "applet", "apple"):
        t3.insert(w)
    assert t3.lcp_all() == "app", t3.lcp_all()      # app 本身是词，不能再走
    assert t3.count_with_prefix("app") == 3
    assert t3.count_end("app") == 1
    print("前缀词边界: app/applet/apple 的 LCP='app'（短词结尾即停）✅")
```

**追问**：1) 两个计数器为什么在插入时维护、查询时 DFS 累加不行吗？—— 行不行看读写比：搜索框/输入法候选是读百万写千的负载，查询期累加让每次前缀计数都变成一次 O(子树大小) 的遍历（热前缀子树可能上万节点）；写入期 +1 只把插入从 O(L) 摊到 O(L)，常数极小。反面是**动态词频**：`prefix` 记的是「历史经过次数」，新热词要几百次插入才抬得动老词的计数——所以实时热点榜要配滑动窗口衰减（A110 的热点探测是另一个问题域），Trie 计数只回答「语料里有多少」，不回答「最近多火」。2) 能不能在节点上预挂 Top-K 汇总，把补全降到 O(|prefix| + K)？—— 可以但代价三层：每节点存子树 Top-K，一次词频变化要沿插入路径回传修正 O(L·K)；冷前缀的汇总纯属内存浪费；词集一变（新词上架）全部失效要重算。工程折衷是**离线批算 + 热门前缀缓存**：定时任务对头部前缀重算 Top-K 存缓存，查询命中缓存 O(1)、未命中走子树 DFS 兜底——分钟级可接受的搜索框几乎都这么做，在线维护只留给高频字级别的输入法引擎。K 很小时 `heapq.nsmallest` 能省全排序，但候选池（子树 DFS）才是大头，排序优化是次要项。3) Trie、`sorted list + bisect`、dict 三者前缀能力的边界？—— dict 只有精确匹配，前缀问题直接出局；sorted list（Q494 的 `bisect` 路线）能做前缀列举：`bisect_left(p)` 起步逐个核对 startswith，复杂度 O(logN + 命中数)，**命中数少时比 Trie 好**（无指针开销、缓存友好）；Trie 的独占能力是 O(|p|) 的前缀计数与 LCP 判定——这两个数不依赖命中多少。选型口诀：**要计数选 Trie，要列举选有序表，两者都要且词集大才付 Trie 的内存账**（每节点一个 dict，英文 26 叉可换双数组 Trie 压内存）。这与 Q2440 再划一次界：路由 Trie 的节点值是 handler、查询是「最深匹配」，统计 Trie 的节点值是计数、查询是「子树聚合」——同一种数据结构、两种查询语义，别拿路由题的答案去答统计题。
