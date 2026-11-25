---
title: [Q5119] str.find 双向子串查找原理
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5119 · str.find 双向子串查找原理

> 难度:★★★★★ | 标签:原理深挖, str, 算法

**问**:`"x" in s`、`s.find(sub)`、`s.index(sub)` 底层是 KMP 吗？CPython 用什么子串查找算法，为什么它对"长模式"和"随机文本"都稳？什么时候会退化到平方级？

**答**:结论：**不是 KMP**。CPython 的 `str.find`/`in` 采用 **Crochemore-Perrin "双向"（Two-Way）算法**（`stringlib/fastsearch.h`），外加一套混合策略：a) 短模式（≤ ~10 字符）用简化 Boyer-Moore-Horspool 式的"跳表"（按模式末字符移位）；b) 长模式切换到 Two-Way：先对模式做**关键因子分解**（critical factorization，找最长重复后缀切点），从切点向后比对、失配时按切点周期**双向移位**（正向跳周期或反向用后缀信息），保证 O(n+m) 且**不需要 O(m) 额外表**（对比 KMP 的 next 数组）；c) 3.10+ 又加了自适应：模式很小、文本很大时先跳读（`stringlib` 的 skip loop 用异或预筛）。Two-Way 的卖点：最坏线性、常数小、零辅助内存——这就是 CPython 不选 KMP 的原因（KMP 要预计算前缀表，且实际常数更大）。退化为平方级的场景：极短模式 + 大量接近匹配的位置（如 `find("aa")` 在 "aaaa...a" 上），但这受跳表策略缓解。另一个工程细节：**bytes 与 str 共用 fastsearch 但 memchr 优化不同**；多字节编码（UTF-16/32 kind）下比较按 kind 宽度整块进行（Q1264 的 kind 布局在这里兑现收益）。

```python
# 行为层验证：find/index/in 三者关系与成本差异
s = "hello world" * 1000
sub = "world"

print(s.find(sub), s.index(sub), sub in s)   # 三者同一查找内核，不同失败语义
print(s.find("xyz"))                          # -1 不抛
try:
    s.index("xyz")
except ValueError as e:
    print("index 失败:", e)

# 定位差异：find 只给首个位置，全部位置要自己推进
import re
positions = []
i = s.find(sub)
while i != -1:
    positions.append(i)
    i = s.find(sub, i + 1)
print("出现次数:", len(positions), "首/尾:", positions[0], positions[-1])

# 退化样本：短模式在重复文本上的 worst case
s2 = "a" * 100_000
import timeit
t = timeit.timeit(lambda: s2.find("aa"), number=1000)
print(f"重复文本 find('aa') x1000: {t*1000:.1f}ms")

# 模式长度跨越策略切换：短模式跳表 vs 长模式 Two-Way
big = ("abcdefgh" * 200_000)          # 1.6MB 文本
for m in ("ab", "abcdefgh" * 4, "abcdefgh" * 1000):
    t = timeit.timeit(lambda: big.find(m), number=200)
    print(f"模式长 {len(m):>6}: {t/200*1e3:.3f}ms/次")

# 无算法保证的对比：朴素 O(n*m) 在 adversarial 输入下爆炸（原理示意）
def naive(hay, needle):
    n, m = len(hay), len(needle)
    return next((i for i in range(n - m + 1) if hay[i:i+m] == needle), -1)
print("naive 结果与 find 一致:", naive(s2, "aa") == s2.find("aa"))
```

**追问一层**:为什么 Two-Way 需要 critical factorization？切点的"周期"（period）在失配移位里起什么作用？
**追二层**:3.11 的 PEP 659 自适应特化会不会把 `in` 的查找路径也特化（如常驻 kind 的 SIMD 化 memchr）？`bytes.find` 与 `str.find` 在非 ASCII 下性能差异怎么解释（引 Q1264）？

**背诵要点**
- CPython 子串查找是 Crochemore-Perrin Two-Way，非 KMP：最坏 O(n+m) 且零辅助表。
- 短模式走简化 Boyer-Moore 跳表，长模式切 Two-Way（critical factorization + 周期移位）。
- find 失败返回 -1，index 抛 ValueError；全量定位要自己推进 start。

**复盘追问**
- 网关做关键词过滤用几十个 `in` 循环还是合并成一个 Aho-Corasick？提示：模式数多时多模式自动机才能线性。
- 线上"在 100MB 日志里 find 一个词很慢"怎么定位？提示：先确认是查找本身还是解码成 str 的成本（bytes 直接 find 省解码）。
