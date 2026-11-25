---
title: [A273] HyperLogLog 误差实证：调和平均抗离群、分桶权衡与 sketch 合并
date: 2026-11-24
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A273 · HyperLogLog 的误差账与调和平均实证

> 难度:★★★★★ | 标签:HyperLogLog, 基数估计, 调和平均, 分桶, sketch 合并, 误差实证

**问**（笔试·编程题）：Q1004 已给过迷你 HLL 的单次运行（桶分摊 + 前导零 + 调和平均 + 小基数线性计数）。面试官的下一问是「**误差从哪来、你能不能实证它**」：① 实现 64 位哈希 HLL（低位选桶、高位算 `rho`），估计器带三段修正——原始调和平均、小基数线性计数、大基数修正分支（64 位哈希下应断言永不触发）；② **标准差实证**：理论相对标准误 = `1.04/√m`（m=1024 时 3.25%）——固定基数跑 40 次独立试验（不同哈希扰动），实测误差均值与样本标准差，与理论区间对账；③ **调和平均 vs 算术平均**：人为构造一个离群桶（某桶 rho 被打到 50），实测算术平均估计器被 `2^R` 支配直接爆炸、调和平均几乎不动——说清为什么必须调和平均；④ **m 的权衡账**：m=256/1024/16384 的理论误差与内存表（bytearray 是 m 字节、Redis 6bit 打包后 12KB），指出「误差 ∝ 1/√m、内存 ∝ m」的对偶关系；⑤ **sketch 合并**：两个 HLL 逐桶取 max 合并后估计并集基数，断言合并估计 ≥ 各自估计且与真实并集偏差在误差带内。请说清与 Q1004（单次运行演示）、Q5123（位图/set 的精确容量账）、A262（布隆过滤器：判存在、可误判、不可计数）的分工——本题只回答「**HLL 误差的来源分解、调和平均的必要性实证与 m 的定价**」。

**答**：① 分工：Q1004 回答「PFADD/PFCOUNT 为什么 12KB 能估上亿」，给的是一次运行的演示；A262 的布隆过滤器回答「元素在不在」，本题回答「**误差是多少、为什么是这个数、什么参数下的定价**」。三个近似结构各管一件事：布隆判成员（有假阳性）、HLL 计基数（有相对误差）、set 给精确（内存爆炸）——面试里最常见的话术错误就是把三者混成「近似去重」。② 误差来源分解：对每个元素哈希取 `rho`（最高位 1 的位置），基数 n 越大出现大 `rho` 的概率越高——单桶的 `2^max_rho` 是 n 的一个极粗的指数型估计量，方差天文数字；HLL 用 m 个桶**分摊风险**再取调和平均压方差，理论相对标准误 `1.04/√m` 与 n 无关、只随桶数走——这是「固定内存换固定精度」的核心性质。实证对账：n=20000、m=1024 跑 40 次独立试验，理论 σ=3.25%，实测样本标准差落在 2%-5.5% 区间、均值偏置 <2%，断言全过——**误差是可复现实验验证的统计承诺，不是拍脑袋数字**。③ 调和平均的必要性：估计量形如 `α·m²/Σ2^{-r}`——调和平均等价于对 `2^{-r}`（概率量）取算术平均，而直接对 `2^r` 取算术平均的朴素估计器会被最大桶支配：一个离群桶 rho=50 就贡献 `2^50/m` 的分子，估计直接爆炸到天文数字。离群桶从哪来：哈希函数有偏、或者攻击者构造碰撞（把特定 key 全打进同一桶）——调和平均对此**免疫**（`2^{-50}≈0`，该桶在分母里几乎消失，其余桶照常投票）。实测：注入一个 rho=50 的桶后，调和平均估计相对原值漂移 <30%，算术平均估计器放大百万倍以上。这就是「为什么 Redis 源码里是调和平均而不是平均的平均」的实验级答案。④ m 的定价表：m=256 → 误差 6.5%/256B；m=1024 → 3.25%/1KB；m=16384 → 0.81%/12KB（Redis 默认）——误差 ∝ 1/√m、内存 ∝ m，**精度翻倍要四倍内存**，这条对偶曲线决定了选型只能取「业务容忍误差」对应的最小 m，而不是越大越好。另外注意实现细节：本 demo 用 bytearray 是每桶 1 字节（m 字节），Redis 用 6bit 紧凑打包（`m·6/8` 字节 = 16384×6/8 = 12KB）——rho 上限 63 时 6bit 够用，这正是 64 位哈希 + 上限截断的原因。⑤ 合并语义：HLL 是**线性可合并 sketch**——逐桶取 max 合并后的估计 = 并集基数的估计，因为「桶内最大 rho」这个统计量天然满足 `max(a,b) ` 可交换。这使「分天 PV 独立统计、月底合并出月 UV」成为可能，且合并是 O(m) 不是 O(n)。断言三连：合并估计 ≥ max(各自估计)（并集不减）、合并估计与真实并集偏差 < 5%（误差带内）、合并结果与「直接把两份数据喂进一个 HLL」逐桶相等——sketch 的合并是**数学等价**而非工程近似。

```python
# 全部标准库；HyperLogLog：三段修正估计器 + 误差实证 + 调和平均抗离群 + sketch 合并
import hashlib
import math


def h64(item, salt=0):
    """64 位哈希；salt 用于制造不同试验的独立哈希视角。"""
    return int.from_bytes(
        hashlib.sha1(("%d:%s" % (salt, item)).encode()).digest()[:8], "big")


class HLL:
    def __init__(self, m=1024):
        assert m & (m - 1) == 0 and m >= 16
        self.m = m
        self.b = m.bit_length() - 1            # 低位 b 位选桶
        self.reg = bytearray(m)                # demo 每桶 1 字节；Redis 为 6bit 打包

    def add(self, item, salt=0):
        v = h64(item, salt)
        idx = v & (self.m - 1)
        rest = v >> self.b                     # 剩余高位算 rho
        w = 64 - self.b
        rho = (w + 1 - rest.bit_length()) if rest else min(w + 1, 63)
        self.reg[idx] = max(self.reg[idx], min(rho, 63))

    def count(self):
        m = self.m
        alpha = 0.7213 / (1.0 + 1.079 / m)     # m>=128 的修正系数
        raw = alpha * m * m / sum(2.0 ** -r for r in self.reg)
        zeros = self.reg.count(0)
        if raw <= 2.5 * m and zeros > 0:       # 小基数：线性计数
            return m * math.log(m / zeros)
        if raw > (1 << 32) / 30.0:             # 大基数修正（64 位哈希几乎不触发）
            raw = -(1 << 64) * math.log(1.0 - raw / float(1 << 64))
        return raw

    def merge(self, other):
        assert self.m == other.m
        for i in range(self.m):
            self.reg[i] = max(self.reg[i], other.reg[i])
        return self


if __name__ == "__main__":
    N = 20000
    # 1) 三段修正分支的存在性自证：本量级下小基数/大基数分支都不该触发
    h0 = HLL(1024)
    for i in range(N):
        h0.add("u%d" % i, salt=0)
    raw = 0.7213 / (1.0 + 1.079 / 1024) * 1024 ** 2 / sum(2.0 ** -r for r in h0.reg)
    est0 = h0.count()
    assert raw > 2.5 * 1024 and raw <= (1 << 32) / 30.0   # 走主分支
    assert abs(est0 - N) / N < 0.08, est0
    print("主分支: n=%d 估计 %.0f，相对误差 %.2f%% ✅" % (N, est0, abs(est0 - N) / N * 100))

    # 2) 标准差实证：理论 1.04/sqrt(m)=3.25%，40 次独立试验对账
    errs = []
    for t in range(40):
        h = HLL(1024)
        for i in range(N):
            h.add("u%d" % i, salt=t)
        errs.append((h.count() - N) / N)
    mean = sum(errs) / len(errs)
    sd = math.sqrt(sum((e - mean) ** 2 for e in errs) / (len(errs) - 1))
    theory = 1.04 / math.sqrt(1024)
    assert 0.02 <= sd <= 0.055, sd                            # 3.25% ± 采样波动
    assert abs(mean) < 0.02, mean                             # 偏置 < 2%
    print("误差实证: 40 次试验 sd=%.2f%%（理论 %.2f%%），均值偏置 %.2f%% ✅"
          % (sd * 100, theory * 100, abs(mean) * 100))

    # 3) 调和平均 vs 算术平均：一个离群桶就能把算术平均打到爆炸
    h1 = HLL(1024)
    for i in range(5000):
        h1.add("v%d" % i, salt=7)
    est_before = h1.count()
    harm_before = h1.count()
    sum_p = sum(2.0 ** -r for r in h1.reg)
    h1.reg[0] = 50                                            # 注入离群桶
    harm_after = h1.count()
    alpha = 0.7213 / (1.0 + 1.079 / 1024)
    arith = alpha * 1024 * (sum(2.0 ** r for r in h1.reg) / 1024.0)   # 朴素算术估计器
    assert abs(harm_after - est_before) / est_before < 0.30   # 调和平均几乎不动
    assert arith > 1e6 * harm_after                           # 算术平均被 2^50 支配
    print("抗离群: 注入 rho=50 后调和估计 %.0f->%.0f（稳）；算术估计器 %.2e（爆炸）✅"
          % (harm_before, harm_after, arith))

    # 4) 小基数线性计数：n=100 时原始估计有偏，线性计数校正到位
    h2 = HLL(1024)
    for i in range(100):
        h2.add("s%d" % i, salt=3)
    lc = h2.count()
    assert 85 <= lc <= 115, lc
    print("小基数校正: 线性计数 %.0f（真值 100，±15%% 内）✅" % lc)

    # 5) m 权衡表：误差 ∝ 1/√m，内存 ∝ m
    for m in (256, 1024, 16384):
        print("m=%-6d 理论误差 %.2f%%  bytearray %d B  Redis 6bit 打包 %d B"
              % (m, 1.04 / math.sqrt(m) * 100, m, m * 6 // 8))
    assert 1.04 / math.sqrt(256) == 2 * 1.04 / math.sqrt(1024)  # 精度翻倍要四倍内存

    # 6) sketch 合并：逐桶 max = 并集估计，且与直接合并喂入逐桶相等
    ua = ["m%d" % i for i in range(8000)]
    ub = ["m%d" % i for i in range(6000, 18000)]              # 重叠 2000
    ha, hb, hall = HLL(1024), HLL(1024), HLL(1024)
    for x in ua:
        ha.add(x, salt=9)
        hall.add(x, salt=9)
    for x in ub:
        hb.add(x, salt=9)
        hall.add(x, salt=9)
    merged = HLL(1024).merge(ha).merge(hb)
    true_union = len(set(ua) | set(ub))
    est = merged.count()
    assert est >= max(ha.count(), hb.count())
    assert abs(est - true_union) / true_union < 0.05
    assert merged.reg == bytearray(hall.reg)                  # 合并数学等价
    print("sketch 合并: 估计 %.0f / 真实并集 %d（偏差 %.2f%%），与单 sketch 逐桶相等 ✅"
          % (est, true_union, abs(est - true_union) / true_union * 100))
```

**追问**：1) 为什么误差与基数 n 无关、只随 m 走？—— HLL 的每个桶在编码「桶内见过最大的 rho」，桶的分辨能力 ≈ `2^r` 是**乘性**的：基数翻倍，各桶最大 rho 的期望只 +1，估计量按同比例翻倍——相对误差是估计量自身的统计性质（`1.04/√m` 来自调和平均的方差分析），与被估的 n 无关。这与布隆过滤器（误判率随填充率漂移）形成对比：HLL 的精度承诺是**稳态的**，布隆的承诺依赖「装了多少」。2) 大基数修正分支什么时候真的触发？—— 64 位哈希下 `raw > 2^32/30 ≈ 1.4 亿` 才触发，触发原因是 `2^{-r}` 在浮点下溢导致分母失真（sum 都挤在 0 附近，数值精度不够）。Redis 用 64 位哈希所以分支保留但极少走；如果实现用 32 位哈希，n 超过千万这一分支就是主路径——面试里能主动说出「这个分支是数值稳定性的保险丝，不是精度优化」是加分项。3) HLL 与 set 的边界在哪里，什么时候必须放弃 HLL？—— 三条红线：a) 要**明细**（谁来了）——HLL 只剩统计量，明细永远丢了，必须 set/bitmap；b) 要**精确**（财务口径 UV 结算）——0.81% 的相对误差在 1 亿基数下是 ±81 万，不可接受；c) 要**动态增删**——HLL 只能 add 不能 remove，删除语义要换布隆+Cuckoo 或真集合。反过来「要数量、不要明细、容忍 ~1%」的 UV/DAU/独立 IP 场景，HLL 是碾压级性价比：1 亿 UV 的 set 要数 GB（Q5123 的容量账），HLL 恒定 12KB。实践中常见组合是「HLL 做大盘趋势 + 抽样明细做构成分析」，两层各自回答自己的问题。
