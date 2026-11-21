---
title: [Q1050] 缺失机制 MCAR/MAR/MNAR
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1050 · 缺失机制 MCAR/MAR/MNAR

> 难度:★★★★ | 标签:统计, 缺失值

**问**:面试官问"缺失值直接填中位数行不行",你先反问什么?

**答**:先反问缺失机制,处理策略必须跟着机制走。MCAR 完全随机缺失,删除或简单填充偏差小;MAR 缺失概率取决于其他观测变量(如年龄越大越不填收入),要在条件分布上插值(按年龄段分组填充、模型插补);MNAR 缺失依赖缺失值本身(高收入者不愿填),任何基于观测数据的填充都仍有偏,只能声明局限、加权或建模选择机制。判断方法:把缺失指示器当哑变量,看它与已知变量的相关性,相关性强基本是 MAR 以上,就要放弃"一刀切填中位数"。

```python
# file: code/05_数据分析与工程化/q1050_missing_mechanism.py
import random
import statistics

random.seed(3)
n = 2000
age = [random.gauss(35, 8) for _ in range(n)]
income = [a * 300 + random.gauss(0, 2000) for a in age]  # 收入与年龄相关

# MAR:收入缺失概率随年龄增大
income_mar = [inc if random.random() > 0.02 * max(0, a - 40) else None for a, inc in zip(age, income)]
# MNAR:高收入者更不愿填,缺失依赖自身
income_mnar = [inc if random.random() > inc / 300000 else None for inc in income]

def report(tag, xs):
    obs = [x for x in xs if x is not None]
    miss = 1 - len(obs) / len(xs)
    print(f"{tag}: 缺失率 {miss:.1%} 观测均值 {statistics.mean(obs):.0f} 真实均值 {statistics.mean(income):.0f}")

report("MAR  按年龄缺失  ", income_mar)
report("MNAR 按收入缺失  ", income_mnar)
# MAR 的均值下滑可用分组填充纠偏,MNAR 无论怎么填都系统偏低
```

**追问**:
- 追问 1:怎么用代码初判机制?—— 构造 isna 指示器,与各已知变量算相关/分组缺失率,显著相关即 MAR。
- 追问 2:MNAR 场景怎么办?—— 引入外部辅助数据、做敏感性分析、在报表标注"仅观测样本口径"。
