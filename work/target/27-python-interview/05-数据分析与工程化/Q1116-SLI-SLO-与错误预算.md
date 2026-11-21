---
title: [Q1116] SLI、SLO 与错误预算
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1116 · SLI、SLO 与错误预算

> 难度:★★★★ | 标签:SRE, SLO

**问**:SLO 99.9% 意味着什么?错误预算怎么用来做工程决策?

**答**:SLI 是测量指标(如 5 分钟窗口的请求成功率),SLO 是目标(99.9%),错误预算 = 1 - SLO,30 天窗口即约 43 分钟不可用额度。预算的用法是"花预算买变更自由":预算充足正常迭代,烧得快(burn rate 高)就冻结非关键发布、优先修稳定性。多窗口燃烧率告警是标准实践:1 小时窗 burn > 6 倍配 5 分钟窗确认触发 P0,避免单点毛刺误报。SLO 必须由产品与工程共同确认,不是 SLA 的内部抄写。

```python
# file: code/05_数据分析与工程化/q1116_error_budget.py

WINDOW_DAYS = 30
SLO = 99.9
TOTAL_MIN = WINDOW_DAYS * 24 * 60
BUDGET_MIN = TOTAL_MIN * (1 - SLO / 100)

bad_minutes_7d = 30
burn_rate = (bad_minutes_7d / (7 * 24 * 60)) / (1 - SLO / 100)

print(f"30 天总分钟 {TOTAL_MIN:,},错误预算 {BUDGET_MIN:.1f} 分钟")
print(f"近 7 天不可用 {bad_minutes_7d} 分钟,burn rate {burn_rate:.1f}x")
if burn_rate > 6:
    print("动作:P0,冻结发布全力救火")
elif burn_rate > 1:
    print("动作:关注,减少非关键变更")
else:
    print("健康,可正常迭代")
```

**追问**:
- 追问 1:为什么用多窗口燃烧率告警?—— 单短窗口易被毛刺误报,单长窗口反应慢,长短窗口组合兼顾灵敏与准确。
- 追问 2:预算烧完了还发版吗?—— 按约定冻结非关键变更,只允许稳定性修复,产品与 SRE 共同决策而不是 SRE 单方面拦截。
