---
title: [Q1074] 特征存储 offline 与 online
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1074 · 特征存储 offline 与 online

> 难度:★★★★ | 标签:特征工程, 架构

**问**:模型离线训练 AUC 很高,上线效果差了一截,和特征存储有什么关系?

**答**:大概率是训练/推理特征不一致(训练用批表算的特征,推理用实时服务现算,口径或时点不同)。特征存储的解法:同一套 transform 代码同时服务 offline(批查询,供训练)与 online(低延迟点查,供推理),特征只定义一次;离线批表按事件时间快照,避免"用未来统计回填历史"造成训练泄露;元数据记录特征血缘、版本与新鲜度。最小可行实现就是一个共享的 featurize 函数 + 离线宽表 + 在线 KV 存储,先保证一致性,再谈平台。

```python
# file: code/05_数据分析与工程化/q1074_feature_store.py
import math

def featurize(raw):
    """唯一转换入口:离线批量与在线单条共用,保证训练与推理一致"""
    return {
        "amount_log1p": round(math.log1p(raw["amount"]), 6),
        "recent_7d_cnt": raw.get("recent_7d_cnt", 0),
        "is_new_user": 1 if raw["orders_total"] <= 1 else 0,
    }

offline = {"amount": 200.0, "orders_total": 3, "recent_7d_cnt": 2}
online = {"amount": 200.0, "orders_total": 3, "recent_7d_cnt": 2}
assert featurize(offline) == featurize(online)
print("同一函数保证 offline 与 online 特征一致:", featurize(online))
print("特征存储本质:离线批查 + 在线点查双通道,共用变换、血缘与版本")
```

**追问**:
- 追问 1:为什么强调事件时间快照?—— 用"今天的全量统计"回填历史训练样本就是时间旅行泄露,AUC 虚高,上线必然回落。
- 追问 2:online 点查延迟要求多少?—— 常见 P99 十几毫秒内,决定它必须用 KV 存储(Redis/DynamoDB)而非查批表。
