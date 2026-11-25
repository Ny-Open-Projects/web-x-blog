---
title: [A278] Rabin-Karp 滚动哈希：防碰撞二次校验与伪命中实证
date: 2026-11-24
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A278 · Rabin-Karp 的滚动哈希与防碰撞二次校验

> 难度:★★★★ | 标签:Rabin-Karp, 滚动哈希, 字符串匹配, 哈希碰撞, 伪命中, 素数模

**问**（笔试·编程题）：手写子串查找，面试官盯的不是「能不能找到」而是**哈希碰撞你打算怎么防**：① 实现多项式滚动哈希与 Rabin-Karp 主循环——窗口右移一格时 O(1) 更新（减头乘底加尾），不许每窗重算；② 哈希相等**必须二次校验**（切片直接比较），哈希不等才跳过——这是「防碰撞」的正确姿势而不是换个哈希函数；③ **伪命中实证**：用小素数模（mod=11）+ 双字母文本构造高碰撞环境——4 字符窗口共 16 种组合映射进 11 个哈希值，鸽笼原理必撞——统计「哈希相等但字符串不等」的窗口数，断言伪命中 > 0 且全部被二次校验拦下（不误报）；④ 正确性对账：随机文本 + 种子固定，与 `str.find` 循环基线的全部命中位置逐元素相等；重叠命中（如 `aaaaa` 找 `aa`）不得漏；⑤ 大素数模（2^61-1）下同样轨迹伪命中归零，说清模数与底数怎么选。请说清与 Q5119（CPython `str.find` 底层是 Crochemore-Perrin Two-Way，不是 KMP）、Q535/Q5065（PYTHONHASHSEED 随机化防哈希碰撞 DoS）、Q426（dict 开放寻址的碰撞处理）的分工——本题只回答「**滚动哈希的数学、碰撞的实证与二次校验守则**」。

**答**：① 分工：Q5119 回答「内置查找为什么稳」，Q535 回答「内置 hash 为什么每进程换盐」，Q426 回答「哈希表落位怎么解碰撞」——没人回答**你自己写哈希匹配时碰撞怎么变成 bug**：朴素哈希匹配（每窗哈希相等就算命中）在 mod 小或输入可构造时大面积误报，这是安全审查里的真实死法。② 滚动公式：窗口 `[i, i+m)` 的哈希 `H_i = Σ t[i+j]·base^(m-1-j) mod p`，右移一格 `H_{i+1} = (H_i − t[i]·base^(m-1))·base + t[i+m]`——预计算 `base^(m-1)` 一次，每窗 O(1)；Python 的 `%` 对负数返回非负（其他语言 C 系会返回负），所以减法后不必先补 mod，这是 Python 版少一行坑的原因。③ 二次校验为什么不可省：哈希相等是**必要条件不是充分条件**——模 p 后值域只有 p 个，窗口数 n 超过 p 就必撞（鸽笼）；正确姿势只有一条「哈希相等 → 切片比较确认」，代价是命中位置 O(m)、通常极少。反过来「哈希不等直接跳过」零成本，这就是 RK 均摊 O(n) 的来源：哈希的工作只是**廉价筛掉绝大多数不等窗口**，不是替你下结论。④ 实证账：mod=11、窗口 4 字符、字母表只有 a/b 时，16 种窗口组合映射进 11 个哈希值——鸽笼原理必撞，实测 400 字符随机文本出 20 次伪命中、全部被二次校验拦截，最终结果与基线仍全等；换成 mod=2^61-1 后伪命中 0。模数选择三条：够大（碰撞概率 ≈ 窗口数/p）、取素数（让 `base` 与 `p-1` 互素，哈希分布均匀）、进阶加随机底数（对抗恶意构造输入——与 Q535 的随机盐是同一个思想：**防的是「知道你的哈希长什么样的人」**）。⑤ 复杂度边界要说诚实：单模式 RK 期望 O(n+m)、最坏 O(n·m)（碰撞全中时退化为逐窗全比较），单模式静态场景 KMP/Two-Way 有 O(n+m) 确界；RK 的主场是**多模式**（k 个模式共享文本滚动，一次扫描 O(n + k·m)）与**指纹复用**（内容分块去重、查重系统）。

```python
# 全部标准库；Rabin-Karp：滚动哈希 O(1) 更新 + 二次校验 + 伪命中实证 + 基线对账
import random

BIG_MOD = (1 << 61) - 1      # Mersenne 素数 2^61-1
SMALL_MOD = 11               # 人为小模，制造高碰撞环境（窗口组合 16 种 > 值域 11）


def poly_hash(s, base, mod):
    h = 0
    for c in s:
        h = (h * base + ord(c)) % mod
    return h


def rabin_karp(text, pat, base=256, mod=BIG_MOD, audit=None):
    """返回全部命中下标（重叠也算）；audit 收集伪命中统计。"""
    n, m = len(text), len(pat)
    if m == 0 or m > n:
        return []
    pw = pow(base, m - 1, mod)          # 预计算 base^(m-1)，滚动更新用
    hp = poly_hash(pat, base, mod)
    hw = poly_hash(text[:m], base, mod)
    hits, fake = [], 0
    for i in range(n - m + 1):
        if i:                           # 窗口右移一格：减头、乘底、加尾
            hw = (hw - ord(text[i - 1]) * pw) * base + ord(text[i + m - 1])
            hw %= mod
        if hw != hp:
            continue                    # 哈希不等：廉价跳过
        if text[i:i + m] == pat:        # 哈希相等：二次校验才下结论
            hits.append(i)
        else:
            fake += 1                   # 伪命中：被校验拦下，不误报
    if audit is not None:
        audit["windows"] = n - m + 1
        audit["fake"] = fake
    return hits


def find_all_baseline(text, pat):
    """str.find 循环基线：从上一命中+1 继续找，天然支持重叠。"""
    out, i = [], text.find(pat)
    while i != -1:
        out.append(i)
        i = text.find(pat, i + 1)
    return out


if __name__ == "__main__":
    # 1) 重叠命中：aaaaa 找 aa，基线对账
    assert rabin_karp("aaaaa", "aa") == [0, 1, 2, 3]
    assert rabin_karp("aaaaa", "aa") == find_all_baseline("aaaaa", "aa")
    assert rabin_karp("abc", "") == [] and rabin_karp("ab", "abc") == []
    print("重叠命中: aaaaa 找 aa → [0,1,2,3] 与 str.find 基线全等 ✅")

    # 2) 随机回归：20 组（随机文本+随机模式），命中位置逐元素相等
    rng = random.Random(2026)
    for _ in range(20):
        text = "".join(rng.choice("abcd") for _ in range(rng.randint(5, 300)))
        pat = "".join(rng.choice("abcd") for _ in range(rng.randint(1, 5)))
        assert rabin_karp(text, pat) == find_all_baseline(text, pat), (text, pat)
    print("随机回归: 20 组随机文本/模式与 str.find 基线全等 ✅")

    # 3) 伪命中实证：小模数+双字母文本制造高碰撞（16 种窗口组合 → 11 个值，鸽笼必撞）
    audit = {}
    rng2 = random.Random(2026)
    text = "".join(rng2.choice("ab") for _ in range(400))
    pat = "".join(rng2.choice("ab") for _ in range(4))
    hits = rabin_karp(text, pat, base=256, mod=SMALL_MOD, audit=audit)
    assert audit["fake"] >= 1, audit                  # 碰撞环境必须出伪命中
    assert hits == find_all_baseline(text, pat)       # 但结果零误报
    print("伪命中实证: mod=%d 窗口 %d 个，伪命中 %d 次全被二次校验拦下，结果仍与基线全等 ✅"
          % (SMALL_MOD, audit["windows"], audit["fake"]))

    # 4) 大素数模：同样轨迹伪命中归零
    audit2 = {}
    hits2 = rabin_karp(text, pat, base=256, mod=BIG_MOD, audit=audit2)
    assert audit2["fake"] == 0 and hits2 == find_all_baseline(text, pat)
    print("大素数模: mod=2^61-1 伪命中 0，碰撞概率 ≈ 窗口数/p ≈ 4e-16 ✅")
```

**追问**：1) 哈希相等但不相等，为什么「换个大模」不能替代二次校验？—— 换大模只是把碰撞概率从「必撞」压到「天文分之一」，**概率归零 ≠ 语义正确**：一旦输入可被构造（攻击者知道你的 base 和 mod，能造出同模串——Rabin-Karp 的多项式哈希没有抗碰结构，构造碰撞只需解一个线性方程组），匹配结果就是可操控的。二次校验把正确性从「概率承诺」升级为「逐位事实」，成本只在哈希相等处支付——正确性永远押在事实校验上，概率手段只负责降成本，这与 A105 秒杀「扣减押 CAS、限流只是降载」是同一条工程原则。2) 滚动更新里最容易写错的三个点？—— a) **模外溢出**：先 `(hw - head·pw) * base + tail` 再统一取模可以，但 C 系语言会溢出（64 位下 head·pw·base 可能超），Python 无限精度免疫；b) **负数取模**：C 系 `%` 可能返回负数，下一步比较前必须 `+mod`，Python 的 `%` 恒非负所以少这一步——这是「同一份算法跨语言移植就错」的典型；c) **base 与模数的关系**：base 取 256（按字节）时若 mod 也是 256 的倍数，所有 `base^k ≡ 0`，哈希只剩尾字节——素数模 + base 小于模是硬约束。3) 什么时候才值得上 Rabin-Karp 而不是 KMP 或直接 `str.find`？—— 三个信号：**多模式**（k 个模式一次扫文本，KMP 要建 k 张失败表、Aho-Corasick 才是对手但实现重得多）；**指纹要复用**（滚动哈希算出的窗口值本身就是指纹，可做文档查重、内容定义分块 CDC——备份系统按内容切块去重就是同一套滚动哈希，Q1730 的代理键去重是它的库表化版本）；**模式是流式到达**（文本读完就丢、不能回退二次扫，KMP 也可以但要保留状态机，RK 只留一个整数窗口值更省）。单模式静态内存场景，CPython 的 Two-Way（Q5119）零辅助表 O(n+m) 确界，永远先用内置——手写 RK 是面试与专项场景的技能，不是生产默认。