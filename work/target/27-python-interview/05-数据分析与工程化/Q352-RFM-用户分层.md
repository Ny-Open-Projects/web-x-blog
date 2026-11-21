---
title: [Q352] RFM 用户分层
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q352 · RFM 用户分层

> 难度:★★☆ | 标签:分析, RFM

**问**:RFM 模型是什么?如何用 Python 实现用户分层?

**答**:RFM 用三个维度刻画用户:Recency(最近一次消费距今)、Frequency(消费频次)、Monetary(消费金额)。实现:先按用户聚合出 R/F/R 原始值,再各自打分(分位数分箱 1-5 分),最后按"高于/低于均值或阈值"映射到 8 个象限(重要价值客户、重要挽留客户等)输出运营策略。工程提醒:F/M 对低频业务要用"有购买行为的周期数"归一,新用户 R 极小但 F=1,不宜直接归为高价值,分层结果要落地到人群包并跟踪转化效果形成闭环。

```python
# file: code/05_数据分析与工程化/q352_rfm.py
from datetime import date

def rfm_score(orders, today=None):
    """orders: list of (uid, order_date, amount)"""
    today = today or date(2026, 11, 1)
    agg = {}
    for uid, d, amt in orders:
        r, f, m = agg.get(uid, (None, 0, 0.0))
        days = (today - d).days
        agg[uid] = (min(r, days) if r is not None else days,
                    f + 1, m + amt)
    # 打分:R 越小分越高,F/M 越大分越高(此处用固定阈值, 生产用分位数)
    result = {}
    for uid, (r, f, m) in agg.items():
        r_s = 3 if r <= 7 else (2 if r <= 30 else 1)
        f_s = 3 if f >= 3 else (2 if f >= 2 else 1)
        m_s = 3 if m >= 500 else (2 if m >= 100 else 1)
        seg = (r_s, f_s, m_s)
        label = {(3, 3, 3): "重要价值", (1, 1, 1): "流失",
                 (3, 1, 1): "新客户"}.get(seg, "一般")
        result[uid] = {"R": r, "F": f, "M": m, "score": seg, "label": label}
    return result

if __name__ == "__main__":
    orders = [("u1", date(2026, 10, 30), 600.0),
              ("u1", date(2026, 10, 25), 100.0),
              ("u2", date(2026, 6, 1), 30.0),
              ("u3", date(2026, 10, 31), 50.0)]
    for uid, info in rfm_score(orders).items():
        print(uid, info)
```

**追问**:
- R/F/M 打分为什么用分位数?——业务分布长尾,等宽分箱会把大多数用户挤进最低分;分位数保证每档人数均衡可比。
- 新用户怎么处理?——单独分层(new),R 极小但 F=1 不代表高价值;混进通用模型会被误判。
- 分层结果怎么验证有效?——A/B 对比不同层级的运营策略转化率;只分层不跟踪等于没做。

---
