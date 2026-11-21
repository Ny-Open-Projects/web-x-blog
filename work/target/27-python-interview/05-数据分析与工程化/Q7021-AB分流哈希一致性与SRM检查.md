---
title: [Q7021] A/B 分流哈希一致性与 SRM 检查
date: 2026-11-20
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7021 · A/B 分流的哈希一致性与 SRM：改个实验层数字为什么会导致用户换组？

> 难度:★★★★ | 标签:A/B测试, 分流, 实验

**问**：A/B 平台按 `hash(userId + salt) % 100` 分流。运营中途把实验从 2 组改成 3 组（A 50/B 50 → A 40/B 30/C 30），结果老用户大面积换组，且数据出现显著不均衡。根因是什么？怎么设计分流才支持实验中途改配置？

**答**：结论：两层问题。其一，**分流口径变更即"再随机化"**——桶边界一变，用户重算落点必然跳组，中途跳组的用户指标被两种处理污染，实验读数作废；正确做法是实验层配置不可变，需要改配置就开新实验（或冻结改配置前数据）。其二，**SRM（Sample Ratio Mismatch）**——实际入组比例与配置比例显著偏离说明分流器或上报有 bug（常见：哈希不均匀、某端 SDK 少上报、缓存/CDN 层丢埋点），不查 SRM 直接看指标是 A/B 平台最大的数据事故来源。

机理与实战：
- 分流哈希的正确姿势：用与业务无关的稳定键（userId/设备 id），盐值 + 域标识进哈希输入（`hash("experiment_id:layer_id:user_id")`），不同实验域天然正交——用户在两个独立实验里的分组互不相关，避免实验间联动污染。选哈希用 SHA-256 或 murmur3 等均匀散列，不要用 Python 内置 `hash()`（字符串随机化 PYTHONHASHSEED 使它**进程间不稳定**，这是最常见的"线上分组乱跳"事故）。
- SRM 检验用卡方拟合：期望比例 p、实际计数 n，`chisquare(n, p*n_total)` p 值 < 0.001 即视为分流异常，报警而非继续观察。AB 平台工程惯例：入组事件实时对账，SRM 触发后实验自动标记"数据不可信"。

```python
# 基线:Python 3.9+ / scipy 可选(缺库降级手算卡方) ;标准库 hashlib
import hashlib
import math


def bucket(user_id: str, salt: str, buckets: int = 100) -> int:
    """稳定分流:SHA-256 + 域盐,跨进程/跨语言结果一致。"""
    h = hashlib.sha256(f"{salt}:{user_id}".encode()).digest()
    return int.from_bytes(h[:8], "big") % buckets


def assign(user_id: str, salt: str, ratios: list[float]) -> int:
    """按比例切桶:边界由累计比例决定,配置不可变才可中途读数。"""
    b = bucket(user_id, salt)
    acc = 0.0
    for i, r in enumerate(ratios):
        acc += r
        if b < acc * 100:
            return i
    return len(ratios) - 1


def srm_p_value(observed: list[int], expected_ratio: list[float]) -> float:
    """卡方拟合优度;缺 scipy 手算,df=k-1,p 用正则化不完全伽马的近似上界。"""
    total = sum(observed)
    chi2 = sum((o - e * total) ** 2 / (e * total)
               for o, e in zip(observed, expected_ratio))
    df = len(observed) - 1
    # Wilson-Hilferty 近似:chi2 近似正态
    z = ((chi2 / df) ** (1 / 3) - (1 - 2 / (9 * df))) / math.sqrt(2 / (9 * df))
    return 0.5 * math.erfc(z / math.sqrt(2))   # 单侧上尾概率


if __name__ == "__main__":
    # 分组稳定性:同用户同盐永远同组
    assert assign("u42", "exp_v1", [0.5, 0.5]) == assign("u42", "exp_v1", [0.5, 0.5])
    # 均匀性抽查
    from collections import Counter
    c = Counter(assign(f"u{i}", "exp_v1", [0.5, 0.5]) for i in range(20000))
    print("分桶分布:", dict(c))
    # SRM 演示:期望 50/50,实际 4980/5020 -> 正常;p<0.001 -> 异常
    print("正常 p =", srm_p_value([9980, 10020], [0.5, 0.5]))
    print("异常 p =", srm_p_value([6000, 4000], [0.5, 0.5]))
```

**追问一**：为什么不能用 Python 内置 `hash()` 或 `random.random()` 做分流？
答：`hash(str)` 受 PYTHONHASHSEED 影响，每次进程重启盐不同，用户分组会随发版漂移；`random` 无状态可复现性差。分流必须用内容寻址的稳定哈希，且同口径要能跨服务（Java/Go 端同算法同结果）。

**追问二**：用户跨设备（登录前后）如何保证同组？
答：分流键优先登录态 userId；匿名期按设备 id 分流，登录后迁移到 userId 口径——迁移会带来一部分换组，工程上接受并记录"换组用户"子群，分析时可剔除或单独观察，关键是口径唯一且全程一致。

**背诵要点**：
- 分流配置不可变，改比例 = 再随机化 = 实验作废；改配置就开新实验。
- PYTHONHASHSEED 使内置 hash 进程间不稳定，分流用 SHA-256/murmur3 + 域盐。
- SRM 卡方 p<0.001 即判数据不可信，入组事件必须实时对账。

**复盘追问**：
- 若 SRM 显示某端少上报 5%，是分流错还是埋点丢？如何二分定位？
- 实验域正交设计里"层"与"域"的关系是什么？

## 背诵要点
- 稳定哈希分流三要素：稳定键、显式盐、跨语言一致算法。
- 中途改比例污染已在组用户，读数窗口必须在配置变更前冻结。
- SRM 是 A/B 数据的第一道质检，比指标显著检验优先级更高。

## 复盘追问
- 卡方 SRM 在小样本实验（每组<500）下为什么不可靠？替代方案？
- 多层实验的正交性如何被"盐含层 id"保证？
