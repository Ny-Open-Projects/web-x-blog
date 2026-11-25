---
title: "[A294] 线段树区间加与区间和：lazy 下推时机、边界裁剪与暴力数组对拍"
date: 2026-11-25
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A294 · 线段树区间加与区间和：lazy 下推时机、边界裁剪与暴力数组对拍

> 难度:★★★★ | 标签:线段树, lazy标记, 区间加, 区间和, 对拍

**问**（笔试·编程题）：维护一个长度 n 的数组，支持两种操作——区间 `[l,r]` 每个元素加 `delta`、查询区间 `[l,r]` 的和，要求 O(log n)：① 为什么 `tree` 要开 4n，节点编号 `node` 与它管辖的 `[l,r]` 怎么对应，`mid` 划分后左右孩子是谁；② `lazy[node]` 的精确语义——为什么它表示「已加到 node、还没下推给孩子」，`apply` 时 `tree[node] += delta * (r-l+1)` 里的长度因子为什么不能省；③ `push` 的时机是什么，查询为什么也得 push，查询里的 push 会不会破坏「查询不改数据」的约定、会不会让复杂度退化；④ 完全覆盖、部分覆盖、无交集三种情况分别怎么写，越界入参（`l<0`、`r>=n`、`l>r`）在 wrapper 里怎么裁剪，空数组为什么要单独短路；⑤ 与暴力数组做 30 组 × 80 次混合操作对拍，再跑 n=200000 建树与全区间加，算清 O((n+m)log n) 的账，并对比「两个树状数组维护差分」能否做同样的事、线段树多出来的能力在哪。

**答**：① 线段树把区间二分到底，形成一棵近似完全二叉树：根编号 1 管 `[0,n-1]`，节点 `node` 的孩子是 `2*node` 与 `2*node+1`，`mid=(l+r)//2` 后左孩子管 `[l,mid]`、右孩子管 `[mid+1,r]`。n 个叶子的树高是 ⌈log2 n⌉+1，编号不再是连续的 2n，最坏会跳到 4n 附近（非 2 的幂时尤其明显），所以统一开 `4n` 是「一定不越界」的最省心写法，代价只是常数倍内存。② `lazy[node]=d` 的语义必须背准：**d 已经计入 node 的区间和，但还没有下推给它的两个孩子**。因此 `apply(node,l,r,d)` 要做两件事——`tree[node] += d*(r-l+1)`，因为这段区间有 `r-l+1` 个元素、每个都加 d；`lazy[node] += d`，多次加可以合并成一次。只写 `tree[node] += d` 是把「区间和」当成「单点值」用，是最经典的错误；反过来只改 lazy 不改 tree，则查询到大区间时会漏掉增量。③ 只要当前区间**不是**被操作区间完全覆盖，就必须先 `push` 再递归孩子，否则孩子缺了祖先的增量；查询也一样，因为查询要读孩子的真实和。`push` 会把 `lazy[node]` 清零、把增量转给孩子，本质上只是「把标记下移」，不改变任何真实值，所以不违反「查询不改数据」——数据没变，变的是标记的存放位置。复杂度不退化：每次 push 只做 O(1) 工作，且只发生在被访问到的节点上，一次操作访问 O(log n) 个节点。④ 完全覆盖（`ql<=l and r<=qr`）直接 apply 返回；否则 push，若 `ql<=mid` 递归左、若 `qr>mid` 递归右，两边都不进说明无交集（但入口保证至少有一边进）。越界入参在 wrapper 里先 `ql=max(0,ql)`、`qr=min(n-1,qr)`，再判 `ql>qr` 直接返回，避免负下标或空区间把递归带进死路；`n==0` 必须最前面短路，否则 `n-1=-1`、`mid` 计算出负数区间。⑤ 对拍：30 组随机数组（n=1..50）各 80 次混合操作，55% 区间加、45% 区间查，delta 取负值，逐次与暴力数组比较；极值用 n=200000 建树、全区间加 5、再查三个子区间与单点。复杂度账：建树 O(n)（每个节点一次），每次操作把区间拆成 O(log n) 个「完全覆盖」节点，故 m 次是 O(m log n)，总 O(n + m log n)；空间 4n 的 tree 与 4n 的 lazy。与树状数组对比：区间加 + 区间和确实可以用两个 BIT 维护差分 `d[i]` 与 `i*d[i]` 做到 O(log n)，代码更短、常数更小，工程上应优先选它；但线段树的 lazy 框架可以自然扩展到区间赋值、区间乘、区间最值、区间最大子段和、可持久化与节点合并，这些是 BIT 做不到或很难做的——所以面试里要能说出「这题 BIT 够用，但我写线段树是为了展示 lazy 框架」。

```python
# 全部标准库；线段树 lazy 区间加 + 区间和，与暴力数组逐操作对拍
import random


class SegTree:
    """下标 0..n-1；add(ql,qr,delta) 区间加，query(ql,qr) 区间和，均 O(log n)。"""

    def __init__(self, arr):
        self.n = len(arr)
        if self.n == 0:
            self.tree = []
            self.lazy = []
            return
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, arr)

    def _build(self, node, l, r, arr):
        if l == r:
            self.tree[node] = arr[l]
            return
        mid = (l + r) // 2
        self._build(node * 2, l, mid, arr)
        self._build(node * 2 + 1, mid + 1, r, arr)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _apply(self, node, l, r, delta):
        # 把 delta 记在 node 上：node 的区间和立刻改，子节点等下次下推
        self.tree[node] += delta * (r - l + 1)
        self.lazy[node] += delta

    def _push(self, node, l, r):
        if self.lazy[node] != 0 and l != r:
            mid = (l + r) // 2
            delta = self.lazy[node]
            self._apply(node * 2, l, mid, delta)
            self._apply(node * 2 + 1, mid + 1, r, delta)
            self.lazy[node] = 0

    def _add(self, node, l, r, ql, qr, delta):
        if ql <= l and r <= qr:
            self._apply(node, l, r, delta)
            return
        self._push(node, l, r)
        mid = (l + r) // 2
        if ql <= mid:
            self._add(node * 2, l, mid, ql, qr, delta)
        if qr > mid:
            self._add(node * 2 + 1, mid + 1, r, ql, qr, delta)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _query(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree[node]
        self._push(node, l, r)
        mid = (l + r) // 2
        total = 0
        if ql <= mid:
            total += self._query(node * 2, l, mid, ql, qr)
        if qr > mid:
            total += self._query(node * 2 + 1, mid + 1, r, ql, qr)
        return total

    def add(self, ql, qr, delta):
        if self.n == 0:
            return
        ql, qr = max(0, ql), min(self.n - 1, qr)
        if ql > qr:
            return
        self._add(1, 0, self.n - 1, ql, qr, delta)

    def query(self, ql, qr):
        if self.n == 0:
            return 0
        ql, qr = max(0, ql), min(self.n - 1, qr)
        if ql > qr:
            return 0
        return self._query(1, 0, self.n - 1, ql, qr)

    def total(self):
        return self.tree[1] if self.n else 0


def brute_ops(arr, ops):
    a = list(arr)
    out = []
    for kind, l, r, x in ops:
        l, r = max(0, l), min(len(a) - 1, r)
        if len(a) == 0 or l > r:
            if kind == "q":
                out.append(0)
            continue
        if kind == "a":
            for i in range(l, r + 1):
                a[i] += x
        else:
            out.append(sum(a[l:r + 1]))
    return out


if __name__ == "__main__":
    rng = random.Random(2941)

    # 1) 30 组随机数组 × 80 次混合操作（区间加/区间查，含负增量）与暴力对拍
    for _ in range(30):
        n = rng.randint(1, 50)
        arr = [rng.randint(-20, 20) for _ in range(n)]
        st = SegTree(arr)
        ops, got = [], []
        for _ in range(80):
            if rng.random() < 0.55:
                l = rng.randint(0, n - 1)
                r = rng.randint(l, n - 1)
                d = rng.randint(-15, 15)
                st.add(l, r, d)
                ops.append(("a", l, r, d))
            else:
                l = rng.randint(0, n - 1)
                r = rng.randint(l, n - 1)
                got.append(st.query(l, r))
                ops.append(("q", l, r, 0))
        assert got == brute_ops(arr, ops), (arr, ops)
    print("线段树对拍: 30 组随机数组 × 80 次混合操作 vs 暴力，全等 ✅")

    # 2) 上述循环里顺带校验 total()：重放所有加操作后全区间和等于叶子总和
    for _ in range(10):
        n = rng.randint(1, 40)
        arr = [rng.randint(0, 10) for _ in range(n)]
        st = SegTree(arr)
        cur = list(arr)
        for _ in range(40):
            l = rng.randint(0, n - 1)
            r = rng.randint(l, n - 1)
            d = rng.randint(-9, 9)
            st.add(l, r, d)
            for i in range(l, r + 1):
                cur[i] += d
        assert st.total() == sum(cur) == st.query(0, n - 1)
    print("整树一致性: total() == query(0,n-1) == 暴力总和 ✅")

    # 3) 边界：单元素、空数组、全区间加、单点加、越界裁剪、负增量归零
    st = SegTree([5])
    assert st.query(0, 0) == 5
    st.add(0, 0, -5)
    assert st.query(0, 0) == 0
    assert SegTree([]).query(0, 3) == 0 and SegTree([]).total() == 0
    st = SegTree([1, 2, 3, 4])
    st.add(0, 3, 7)
    assert st.query(0, 3) == 10 + 28 and st.query(1, 2) == 5 + 14
    st.add(2, 2, -3)
    assert st.query(2, 2) == 10 - 3
    assert st.query(-5, 100) == st.total() == st.query(0, 3)   # 越界自动裁剪
    st.add(3, 3, 2)
    assert st.query(0, 2) == 24 and st.total() == 37
    print("边界: 单元素/空数组/全区间/单点/越界裁剪/负增量 全过 ✅")

    # 4) 极值：n=200000 建树 + 全区间加 + 三次部分查询，递归深度只有 log2(n)
    n = 200000
    arr = [1] * n
    st = SegTree(arr)
    assert st.total() == n
    st.add(0, n - 1, 5)
    assert st.total() == 6 * n
    assert st.query(0, 0) == 6 and st.query(n - 1, n - 1) == 6
    assert st.query(12345, 54321) == 6 * (54321 - 12345 + 1)
    st.add(100, 199, 4)
    assert st.query(100, 199) == 10 * 100 and st.total() == 6 * n + 400
    print("极值: n=200000 建树/全区间加/部分查询，O(log n) 递归无压力 ✅")

    print("对拍通过：线段树 30 组随机混合操作 + 边界 + 20 万极值全绿")
```

**追问**：1) 区间赋值和区间加混在一起，lazy 的优先级怎么定？—— 赋值会覆盖此前所有加，所以节点上要区分两种标记：有 `set` 时 `add` 失效；`push` 时先应用 `set` 再应用 `add`，顺序反了会得到「先加后赋值」的错误结果。工程写法是 `lazy_set` 配 `has_set` 布尔，或用一个哨兵值表示「无赋值」。2) 什么时候需要动态开点或离散化？—— n 到 1e9 但操作数 m 只有 1e5 时，4n 的内存直接爆掉；此时只对操作涉及的区间递归建点（动态开点，节点数 O(m log n)），或离线收集所有端点做离散化后用普通线段树。区别是动态开点支持在线，离散化必须预先知道全部询问。3) 区间加 + 区间和一定要线段树吗？—— 不一定。两个 BIT 分别维护差分 `d` 与 `i*d`，前缀和公式 `sum(x) = (x+1)*Σd - Σi*d`，就能做到 O(log n) 且常数更小、代码二十行。线段树的价值在于可扩展性：区间最值、区间乘/加混合、区间赋值、区间最大子段和、可持久化、多棵树合并，这些都是 BIT 的盲区。答题策略是先说 BIT 更优，再说「但我用线段树展示 lazy 框架」。
