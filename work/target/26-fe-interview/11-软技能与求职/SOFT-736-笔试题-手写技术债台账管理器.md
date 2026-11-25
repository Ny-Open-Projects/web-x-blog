---
title: [SOFT-736] 手写 DebtLedger：债务登记（利息量化）、策略分类、季度审计、高息预警？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-736：手写 DebtLedger：债务登记（利息量化）、策略分类、季度审计、高息预警

**需求与边界**：
- 实现 DebtLedger：register(audit)/repay(id)/quarterlyAudit()。
- 边界要求：① 登记必填 { name, interest（人日/次或风险级）, trigger, strategy }；② 策略三分类（捆绑顺带/专项偿还/新债设限）；③ 高息预警：interest ≥ 2 人日/次 或 risk=high 的债列出优先偿还清单；④ quarterlyAudit 输出：总债数/偿还数/新增数/趋势（增=告警）；⑤ 未还的高息债超 2 季度升级告警。

**答**：
```javascript
class DebtLedger {
  constructor() { this.items = new Map(); this.seq = 0; }
  register({ name, interestDays, risk = 'low', strategy, trigger }) {
    if (!strategy) throw new Error('新债必须带偿还策略');
    const id = `D${++this.seq}`;
    this.items.set(id, { id, name, interestDays, risk,
      strategy, trigger, status: 'open', quarterAdded: curQuarter() });
    return id;
  }
  repay(id, how) {
    const d = this.items.get(id);
    d.status = 'repaid'; d.repaidHow = how; d.at = Date.now();
  }
  highInterest() {
    return [...this.items.values()].filter(d => d.status === 'open'
      && (d.interestDays >= 2 || d.risk === 'high'));
  }
  quarterlyAudit() {
    const open = [...this.items.values()].filter(d => d.status === 'open');
    const addedThisQ = open.filter(d => d.quarterAdded === curQuarter());
    const stale = open.filter(d =>
      curQuarter() - d.quarterAdded >= 2
      && (d.interestDays >= 2 || d.risk === 'high'));
    return { total: open.length,
      trend: addedThisQ.length > open.length - addedThisQ.length
        ? '新增>偿还：告警' : '可控',
      priority: this.highInterest(),
      staleUpgrade: stale.length ? `${stale.length}笔高息债超2季度——升级处理` : null };
  }
}
```

**评分点**:
- 新债强制带策略（借债设限的制度化）。
- 高息定义量化（≥2 人日/次或 high）+ 超期升级。
- 趋势审计（新增>偿还告警——债务规模可控性）。

