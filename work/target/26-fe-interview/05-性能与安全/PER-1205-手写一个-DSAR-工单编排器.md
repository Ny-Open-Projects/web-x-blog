---
title: [PER-1205] 手写一个 DSAR 工单编排器
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1205：手写一个 DSAR 工单编排器

**答**：
- 需求：实现 DsarOrchestrator(systems, slaDays)。submit(uid, type) 生成工单 { id, type, systems: [{ name, status: pending }] }；dispatch(id) 并行向各系统派发（dispatchFn(name, task) 返回 Promise），成功置 done 失败置 failed；status(id) 返回 { done, failed, progress }；超时（slaDays 天）未完成的系统标记 timeout 并触发 escalate 回调。
- 边界：重复 dispatch 已完成工单 no-op；部分失败不算整体完成；type 限 access/erase/export/correct。
- 评分点：工单生成；并行派发；超时升级；状态聚合

```javascript
class DsarOrchestrator {
  constructor(systems, slaDays = 30, { dispatchFn, escalate } = {}) {
    this.systems = systems; this.sla = slaDays;
    this.dispatchFn = dispatchFn; this.escalate = escalate;
    this.tickets = new Map();
  }
  submit(uid, type) {
    if (!['access', 'erase', 'export', 'correct'].includes(type))
      throw new Error('bad type');
    const t = { id: `dsar-${Date.now()}-${Math.floor(Math.random() * 1e4)}`,
      uid, type, createdAt: Date.now(),
      systems: this.systems.map(s => ({ name: s, status: 'pending' })) };
    this.tickets.set(t.id, t);
    return t;
  }
  async dispatch(id) {
    const t = this.tickets.get(id);
    if (!t || t.systems.every(s => s.status === 'done')) return;
    await Promise.all(t.systems.map(async s => {
      if (s.status !== 'pending') return;
      try { await this.dispatchFn(s.name, { uid: t.uid, type: t.type });
        s.status = 'done'; }
      catch { s.status = 'failed'; }
    }));
    const overdue = Date.now() - t.createdAt > this.sla * 86400_000;
    if (overdue) t.systems.filter(s => s.status === 'pending')
      .forEach(s => { s.status = 'timeout'; this.escalate?.(t.id, s.name); });
  }
  status(id) {
    const t = this.tickets.get(id);
    const done = t.systems.filter(s => s.status === 'done').length;
    return { done: done === t.systems.length,
      failed: t.systems.filter(s => s.status === 'failed').map(s => s.name),
      progress: +(done / t.systems.length * 100).toFixed(0) + '%' };
  }
}
```
