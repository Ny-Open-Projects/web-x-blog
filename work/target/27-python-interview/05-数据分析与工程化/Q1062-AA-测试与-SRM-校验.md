---
title: [Q1062] AA 测试与 SRM 校验
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1062 · AA 测试与 SRM 校验

> 难度:★★★★ | 标签:实验, A/B

**问**:实验还没开跑,上线前要做哪两件事来证明平台本身没坏?

**答**:AA 测试和 SRM 校验。AA 测试:两个配置完全相同的组互相对比,主指标应无显著差异,显著差异说明分流有偏或埋点/统计管道有问题。SRM(样本比不匹配)检查:观测到的各桶样本量与设计比例对比,双桶用卡方(df=1 时 3.84 为 α=0.05 阈值),超阈值必须停实验排查,常见原因有埋点丢失、重定向过滤、分桶服务与统计侧桶号口径不一致。两者都是实验平台的"仪表自检",任何显著性结论之前先过这两关。

```python
# file: code/05_数据分析与工程化/q1062_aa_srm.py

def srm_chi2(observed, expected):
    total_o, total_e = sum(observed), sum(expected)
    exp_scaled = [e * total_o / total_e for e in expected]
    return sum((o - e) ** 2 / e for o, e in zip(observed, exp_scaled))

chi = srm_chi2([4800, 5200], [1, 1])
print(f"SRM 卡方 = {chi:.2f},阈值 3.84 -> {'SRM 异常,停实验排查' if chi > 3.84 else '正常'}")
print("AA 测试:两个对照组对同一指标做两比例检验,p 应 >= 0.05")
print("AA 显著或 SRM 报警都指向平台问题,而不是业务效应")
```

**追问**:
- 追问 1:SRM 常见的工程原因?—— 分桶与统计用了不同 ID、埋点在跳转页丢事件、某一桶的客户端崩溃不上报。
- 追问 2:AA 要跑多久?—— 与正式实验同量级(至少一个完整周期),指标方差大时更长,目的是稳定估出噪音水平。
