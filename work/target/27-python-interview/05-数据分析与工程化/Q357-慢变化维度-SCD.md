---
title: [Q357] 慢变化维度 SCD
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q357 · 慢变化维度 SCD

> 难度:★★★ | 标签:数仓, SCD

**问**:用户的收货地址改了,历史订单报表应该显示新地址还是旧地址?谈谈 SCD 的处理方式。

**答**:这就是慢变化维度问题。SCD Type 1 直接覆盖旧值,历史丢失,适合无关紧要属性;SCD Type 2 保留全历史:加 surrogate key、生效时间、失效时间、is_current 标志,事实表通过 surrogate key 关联到"事件发生时"的版本,回答"当时"的问题;SCD Type 3 只保留上一版,很少用。分析场景默认 Type 2;实现上用"每日快照对比 + 拉链表"最稳:字段有变才关旧开新,避免无意义的版本膨胀。

```python
# file: code/05_数据分析与工程化/q357_scd_type2.py
from datetime import date

def apply_scd2(dim_rows, current, new_state, eff_date):
    """拉链表:字段有变才关旧开新。current: uid -> row"""
    uid = new_state["uid"]
    old = current.get(uid)
    if old is None:
        new_state.update(eff_from=eff_date, eff_to=None, is_current=True)
        dim_rows.append(new_state)
    elif any(new_state[k] != old[k] for k in ("city",) ):
        old["eff_to"] = eff_date            # 关旧
        old["is_current"] = False
        new_state.update(eff_from=eff_date, eff_to=None, is_current=True)
        dim_rows.append(new_state)          # 开新
    current[uid] = new_state

if __name__ == "__main__":
    rows = []
    cur = {}
    apply_scd2(rows, cur, {"uid": 1, "city": "BJ"}, date(2026, 1, 1))
    apply_scd2(rows, cur, {"uid": 1, "city": "BJ"}, date(2026, 3, 1))  # 未变,不产生新版本
    apply_scd2(rows, cur, {"uid": 1, "city": "SH"}, date(2026, 6, 1))  # 变更,拉链
    for r in rows:
        print(r)
    assert len(rows) == 2, "未变更不应新增版本"
```

**追问**:
- 拉链表怎么写更新逻辑?——比较新旧记录:有变则关旧(open_end=昨天,is_current=0)、开新(open_start=今天);无变跳过,防版本膨胀。
- 「当时」的查询怎么写?——事实表的 surrogate key 直接关联;没走 surrogate key 而按业务键+日期区间过滤容易踩边界。
- Type 2 的成本是什么?——维度表膨胀、join 多一层;无关紧要的属性(如备注字段)变更不要触发拉链,挑选「影响分析的属性」。

---
