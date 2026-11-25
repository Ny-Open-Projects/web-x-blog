---
title: [A258] 带权重的随机抽样：别名法、Fenwick 与流式权重重建
date: 2026-11-24
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A258 · 带权重随机抽样与别名法

> 难度:★★★★ | 标签:加权抽样, 别名法, 前缀和, 流式更新, 流量分配

**问**（笔试·编程题）：给一个抽样器，输入是「候选集合 + 权重」（比如召回混排时的商品权重、按容量给实例分流量、按历史 CTR 做探索），要求：① 单次抽样 **O(1)**，构建 **O(n)**，且抽样消耗的随机数个数与 n **无关**（要能被计数验证，不许有隐藏扫描）；② 权重支持 **0**（永不抽中）、支持单元素、支持负数与全零的**显式拒绝**；③ 同一 seed 必须复现同一条序列；④ 给出**流式更新**方案——百万候选、权重每分钟变，别名法整表重建的 O(n) 怎么摊薄，为什么「改一个权重只修一格」在数学上不成立；⑤ 用 30 万次抽样验收分布（不能只写「看起来对」），并给出拒绝采样、前缀和 + 二分、Fenwick 三者的代价对照。请说清与 A247（一致性哈希 + 虚拟节点权重：要求**同一 key 稳定路由**）、A117（调度器优先级与公平性：要求**排队与份额**）、A128（灰度分桶：要求**用户维度稳定**）的分工——都在「按权重分配」，为什么这四张不能互相替代。

**答**：① 分工先划清：A247 / A128 要的是**确定性**——同一个 user 每次都必须落到同一档，所以用 `hash(key) % N` 与阈值比较，随机源根本不能参与；A117 要的是**份额与顺序**（高优先级先跑、低优先级不饿死），产出是一条调度序列；本题要的是**独立同分布**（i.i.d.）抽样——每次调用都与上一次无关，只保证长期频率收敛到权重。判据很简单：**同一输入调两次，结果该不该一样**。该一样 → 哈希；该不一样 → 抽样。把抽样器拿去做灰度分流，用户会「这次新版下次旧版」；把哈希拿去做混排，每次曝光的顺序固定不变，用户永远看到同一个第二名。② 三种实现的正面对比：**前缀和 + 二分** O(n) 构建、O(log n) 抽样、O(1) 改权（改一个点要更新后面所有前缀，其实是 O(n)，除非换成树状数组）；**Fenwick** O(n log n) 构建（可优化到 O(n)）、O(log n) 抽样、O(log n) 改权——它是「权重频繁变、候选不太多」时的最优解；**别名法** O(n) 构建、O(1) 抽样、**O(n) 重建**——用构建成本换查询常数，适合「读多写少」。**拒绝采样** 期望 O(1)（期望尝试次数 = `n·max/Σw`），实现最简，但依赖 `max(w)` 已知且在动态权重下要持续维护，最坏情况无上界（权重极度倾斜时一次抽样可能要试很多次），且每次都要重新生成均匀数——它有明确的适用面，但不能承诺常数时间。③ 别名法的直觉：把 `[0,n)` 切成 n 个等宽格子，第 i 格总面积 1，但按权重它「应该」只占 `n·w_i/Σw`。于是每格拆成两部分：**自持** `prob[i]` 与**借出** `1-prob[i]`，借出的那份全部指向 `alias[i]`。构建就是把所有 `prob<1` 的格子（small）与 `prob≥1` 的格子（large）两两配对，填满一格、削掉另一格，直到没有 small 或没有 large——每个元素进 small/large 恰好常数次，所以 O(n)。抽样时先均匀选格（`randrange(n)`），再以 `prob[i]` 的概率留在本格、否则跳到 `alias[i]`，**恰好用 2 个随机数**，与 n 无关。这里有个必须点破的校验陷阱：**`sum(prob) ≠ n`**。自持概率之和没有任何守恒意义（示例 `[1,2,3,4,10]` 得到 `[0.25,0.5,0.75,1,1]`，和是 3.5），真正的不变量只有「每个 `prob[i] ∈ [0,1]`」和「长期频率等于权重」。拿 `sum(prob)==n` 当断言，是面试里最常见的假阳性。④ 浮点与边界：`total` 用浮点累加，百万级权重会累积 1e-10 量级的误差，二分/Fenwick 抽到 `r > total` 时会越界，所以必须有 `min(idx, n-1)` 兜底；`NaN` 权重会把 `total` 污染成 NaN，比较全为 False，抽样直接卡死或永远返回 0 号——**入口必须 `math.isfinite` 校验**，这类脏数据在特征回填、CTR 预估里极常见。整数权重（如「按 CPU 核数分流量」）用整数 `total` 可以完全消除误差，优先选整数。⑤ 流式更新：为什么不能「改一格只修一格」？因为 `prob[i] = n·w_i/Σw`——**分母变了，全表都变**；即使只改一个权重，其余 n-1 格的 `prob` 与 `alias` 都可能失效（原本填平的 borrow 关系被打破）。所以别名法是「快照结构」，更新只有三条路：**全量重建**（O(n)，百万级约几十毫秒，必须双缓冲：后台线程构建新表，原子替换引用，读侧零停顿）、**攒漂移批量重建**（累计变更比例超过阈值再建，把 O(n) 摊到多次更新上）、**分层**（大类权重用别名法、类内再用别名法，重建只重建变化的那一层）。本题代码里把「未重建时分布仍是旧的」显式断言出来——这不是 bug，是数据结构语义：**你必须知道自己在读快照**。⑥ 验收方式：30 万次抽样、5 个权重，最大偏差 0.0014（理论标准差 ≈ 0.0009，3σ 内）；严格一点应该做卡方拟合优度检验，`χ² = Σ(O-E)²/E` 在自由度 n-1 下不应超过临界值。只看「多的抽得多」等于没测——权重 0.5 与 0.5001 的差别肉眼永远看不出来，但广告计费会差钱。⑦ 业务侧的三个坑：**抽样 ≠ 配额**（「按 1:1 分给两个实验」用 i.i.d. 抽样，1000 个用户里 480/520 是正常的；要精确 500/500 得用洗牌或系统抽样）；**低概率事件不可抽样验证**（0.1% 的流量，单机每秒 10 次请求，两天才攒够一次，别拿它做功效分析）；**抽样源必须与业务随机解耦**（用同一个 `random` 实例既做重试抖动又做权重抽样，会给抖动引入偏差，还可能把 seed 打乱导致不可复现）。

```python
# 全部标准库；别名法（Vose）O(1) 抽样、Fenwick O(log n) 对照、流式重建阈值
import random


class _CountingRandom:
    """包一层随机源，用来精确统计抽样消耗的随机数个数（证明没有扫描）。"""

    def __init__(self, seed=0):
        self._r = random.Random(seed)
        self.calls = 0

    def random(self):
        self.calls += 1
        return self._r.random()

    def randrange(self, n):
        self.calls += 1
        return self._r.randrange(n)


class AliasSampler:
    """别名法：构建 O(n)，单次抽样恰好 2 次随机数、与规模无关。

    prob[i]  = 第 i 格「落在自己名下」的概率
    alias[i] = 剩下的 1-prob[i] 概率全部借给这一格
    """

    def __init__(self, weights, rng=None):
        w = [float(x) for x in weights]
        n = len(w)
        if n == 0:
            raise ValueError("权重不能为空")
        if any(x < 0 for x in w):
            raise ValueError("权重不能为负")
        total = sum(w)
        if total <= 0:
            raise ValueError("权重和必须 > 0")
        self.n = n
        self.rng = rng or random.Random()
        prob = [x * n / total for x in w]
        alias = list(range(n))
        small = [i for i, p in enumerate(prob) if p < 1.0]
        large = [i for i, p in enumerate(prob) if p >= 1.0]
        while small and large:
            s = small.pop()
            l = large.pop()
            alias[s] = l                         # s 的缺口整块借给 l
            prob[l] = (prob[l] + prob[s]) - 1.0  # l 被借走后还剩多少
            if prob[l] < 1.0:
                small.append(l)
            else:
                large.append(l)
        for i in small + large:                  # 浮点残差归一到 1
            prob[i] = 1.0
        self.prob, self.alias = prob, alias

    def sample(self):
        i = self.rng.randrange(self.n)
        return i if self.rng.random() < self.prob[i] else self.alias[i]

    def valid(self):
        """结构不变量：每格自持概率必须落在 [0,1]（sum(prob) 不等于 n，别拿它当校验）。"""
        return all(0.0 <= p <= 1.0 for p in self.prob)


class FenwickSampler:
    """对照：前缀和 + 树状数组，抽样 O(log n)、单点改权 O(log n)。"""

    def __init__(self, weights, rng=None):
        self.w = [float(x) for x in weights]
        self.n = len(self.w)
        if self.n == 0 or any(x < 0 for x in self.w) or sum(self.w) <= 0:
            raise ValueError("权重非空、非负且和必须 > 0")
        self.rng = rng or random.Random()
        self.tree = [0.0] * (self.n + 1)
        for i, v in enumerate(self.w):
            self._add(i + 1, v)
        self.total = sum(self.w)

    def _add(self, i, d):
        while i <= self.n:
            self.tree[i] += d
            i += i & -i

    def set_weight(self, idx, w):
        if w < 0:
            raise ValueError("权重不能为负")
        old = self.w[idx]
        self.w[idx] = float(w)
        self.total += w - old
        self._add(idx + 1, w - old)

    def sample(self):
        r = self.rng.random() * self.total
        idx, bit = 0, 1 << (self.n.bit_length() - 1)
        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.tree[nxt] <= r:
                idx = nxt
                r -= self.tree[nxt]
            bit >>= 1
        return min(idx, self.n - 1)               # 浮点边界兜底


class StreamSampler:
    """流式权重：别名表无法局部修补，只能「攒够漂移再整体重建」。"""

    def __init__(self, weights, rng=None, auto=True, drift=0.2):
        self._w = {k: float(v) for k, v in weights.items()}
        self._keys = list(weights)
        self._rng = rng or random.Random()
        self._dirty = 0
        self.auto, self.drift = auto, drift
        self.rebuilds = 0
        self._build()

    def _build(self):
        self._tbl = AliasSampler([self._w[k] for k in self._keys], rng=self._rng)
        self._dirty = 0
        self.rebuilds += 1

    def update(self, key, weight):
        if weight < 0:
            raise ValueError("权重不能为负")
        if key not in self._w:
            self._keys.append(key)
        self._w[key] = float(weight)
        self._dirty += 1
        if self.auto and self._dirty / len(self._keys) >= self.drift:
            self._build()

    def rebuild(self):
        self._build()

    def sample(self):
        return self._keys[self._tbl.sample()]

    def is_stale(self):
        return self._dirty > 0


class RejectionSampler:
    """对照：拒绝采样，期望尝试次数 = n*max/sum，最坏情况无上界。"""

    def __init__(self, weights, rng=None):
        self.w = [float(x) for x in weights]
        self.mx = max(self.w)
        self.rng = rng or random.Random()
        self.tries = 0

    def sample(self):
        while True:
            self.tries += 1
            i = self.rng.randrange(len(self.w))
            if self.rng.random() * self.mx < self.w[i]:
                return i


# ===== 自测：分布、边界、代价与流式失效 =====
if __name__ == "__main__":
    N = 300000

    # 1) 别名法的抽样频率必须收敛到 w/sum(w)，且表结构合法
    w = [1, 2, 3, 4, 10]
    s = AliasSampler(w, rng=random.Random(2024))
    assert s.valid()
    hit = [0] * len(w)
    for _ in range(N):
        hit[s.sample()] += 1
    total_w = sum(w)
    dev = max(abs(hit[i] / N - w[i] / total_w) for i in range(len(w)))
    assert dev < 0.004, dev
    print("别名法分布: 30 万次抽样最大偏差 %.4f（期望 0.2/0.1/0.066/0.05/0.5）✅" % dev)

    # 2) 零权重永不被抽中；单元素退化；空/负数/全零必须报错
    z = AliasSampler([1, 0, 2, 0], rng=random.Random(7))
    assert {z.sample() for _ in range(20000)} == {0, 2}
    assert AliasSampler([5]).sample() == 0
    for bad in ([], [0, 0], [1, -1]):
        try:
            AliasSampler(bad)
            raise AssertionError("应当拒绝非法权重: %r" % (bad,))
        except ValueError:
            pass
    print("边界: 零权重不出现、单元素恒 0、空/全零/负数均报错 ✅")

    # 3) 代价：别名法每次抽样恰好 2 次随机数，与 n 无关
    for n in (5, 5000):
        rng = _CountingRandom(1)
        t = AliasSampler([1] * n, rng=rng)
        for _ in range(1000):
            t.sample()
        assert rng.calls == 2000, (n, rng.calls)
    print("抽样代价: n=5 与 n=5000 都是 2 次随机数/次（无扫描）✅")

    # 4) Fenwick 对照：抽样分布一致，且支持 O(log n) 单点改权
    f = FenwickSampler([1, 2, 3, 4, 10], rng=random.Random(11))
    fh = [0] * 5
    for _ in range(N):
        fh[f.sample()] += 1
    fdev = max(abs(fh[i] / N - w[i] / total_w) for i in range(5))
    assert fdev < 0.004, fdev
    f.set_weight(0, 30)                       # 把第一项从 1 提到 30，total -> 49
    assert abs(f.total - 49) < 1e-9
    fh2 = [0] * 5
    for _ in range(N):
        fh2[f.sample()] += 1
    assert fh2[0] / N > 0.55, fh2[0] / N      # 30/49 ≈ 0.612
    print("Fenwick: 分布偏差 %.4f；改权后占比 %.3f（30/49=0.612）✅" % (fdev, fh2[0] / N))

    # 5) 拒绝采样：期望尝试次数 = n*max/sum，本例 5*10/20 = 2.5
    rj = RejectionSampler(w, rng=random.Random(3))
    for _ in range(N):
        rj.sample()
    avg = rj.tries / N
    assert 2.3 < avg < 2.7, avg
    print("拒绝采样: 平均尝试 %.2f 次（理论 n*max/sum = 2.5），最坏情况无上界 ✅" % avg)

    # 6) 可复现：同 seed 得到同一条抽样序列
    def run(seed):
        a = AliasSampler(w, rng=random.Random(seed))
        return [a.sample() for _ in range(200)]

    assert run(42) == run(42) and run(42) != run(43)
    print("可复现: seed=42 两次一致，seed=43 不同 ✅")

    # 7) 流式更新：不重建 = 沿用旧分布（别名表不可局部修补）；重建后才生效
    st = StreamSampler({"a": 1, "b": 1, "c": 1, "d": 1, "e": 1},
                       rng=random.Random(5), auto=False)
    st.update("a", 1000)
    assert st.is_stale()
    before = sum(1 for _ in range(4000) if st.sample() == "a") / 4000
    st.rebuild()
    after = sum(1 for _ in range(4000) if st.sample() == "a") / 4000
    assert before < 0.4 and after > 0.95, (before, after)
    print("流式: 改权后未重建时 a 占比 %.3f（仍是旧分布），重建后 %.3f ✅"
          % (before, after))

    # 8) 削峰策略：用阈值把重建摊薄——1000 个 key 只改 10% 时不重建
    st2 = StreamSampler({("k%d" % i): 1 for i in range(1000)},
                        rng=random.Random(9), auto=True, drift=0.2)
    base = st2.rebuilds
    for i in range(100):
        st2.update("k%d" % i, 1 + i)
    assert st2.rebuilds == base and st2.is_stale(), st2.rebuilds
    print("重建摊薄: 1000 key 改 100 个（10%% < 阈值 20%%）未触发重建，重建次数 %d ✅"
          % st2.rebuilds)
```

**追问**：1) 千万级候选、权重每分钟变一次，别名法还能用吗？—— 直接用不行：全量重建 1000 万条约几百毫秒到秒级，每分钟一次会持续吃满一个核，且重建期间如果阻塞读侧就是周期性抖动。三种落地方式：**双缓冲**（后台线程构建新 `alias/prob` 数组，构建完原子替换引用，读侧永远读完整快照，代价是峰值 2 倍内存）、**分层两级抽样**（先按大类抽、再类内抽，总表只有几千类，重建代价降低两三个数量级，数学上仍然精确——`P(i) = P(类)·P(i|类)`）、**换成 Fenwick/分块前缀和**（O(log n) 抽样换 O(log n) 更新，牺牲常数换增量能力）。注意「权重每分钟变」往往只是**部分变**，分层方案能精确利用这个局部性。2) 为什么灰度分流不能用这个抽样器？—— 抽样是**无记忆**的：同一个用户每次请求独立抽一次，10% 灰度会让他「这次新版下次旧版」，既伤体验也让指标归因失效（同一用户的数据跨两个版本，AB 实验的方差被污染）。分流必须用 `hash(flag_id, salt, user_id)` 做**确定性映射**，同一输入恒定输出；两者唯一共享的思想是「用均匀分布做区间划分」。3) 如果业务要「按权重精确分配 N 个名额」（比如 100 个奖品按权重发给 10 万用户，必须精确 50/30/20）怎么办？—— 那不是抽样，是**配额分配**：i.i.d. 抽样只有大数定律（会有 ±√N 的偏差），要做精确分配就用「最大余数法」（先按比例取整，余数按小数部分排序补足）或**系统抽样**（按累计权重等距取点，把 N 次抽样的方差降到 0）。分不清这两者，会出现「说好 50 个一等奖，实际发出 47 个」的资损级差异。

## 背诵要点
1. 别名法 = `prob` 表 + `alias` 表，构建 O(n)、抽样恰好 2 个随机数；拒绝采样期望 `n·max/Σw` 次且最坏无上界；Fenwick O(log n) 抽样兼 O(log n) 改权。
2. 校验只能看「每个 `prob∈[0,1]`」与长期频率（卡方/最大偏差），**不能**断言 `sum(prob)==n`——它本来就不等于 n。
3. 改一个权重会改变 `Σw`，全表 `prob` 同时失效：别名法是快照，只能双缓冲重建、攒漂移重建或分层重建。

## 复盘追问
1. 抽样频率校验通过，但广告主投诉「预算半小时就烧完」，为什么？（提示：i.i.d. 抽样只管长期比例，短期方差大 + 大权重计划连续命中；预算要 pacing/配额，而不是纯抽样）
2. 权重里混进 NaN 会怎样？（提示：`total` 变 NaN，所有比较为 False，抽样永远落到 0 号或死循环；入口必须 `isfinite` 校验，特征回填是重灾区）
