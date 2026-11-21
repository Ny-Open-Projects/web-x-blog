---
title: [AGT-491] 笔试题——实现死信队列处理（重试耗尽归档+告警+重放）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-491：手写 DLQ 处理：重试耗尽入死信、归因标签、告警、重放接口

**需求与边界**：
- 输入：任务执行器、DLQ 存储；输出：死信管理与重放。
- 边界要求：① 重试耗尽（含不可重试错误）→ 入死信（带全量上下文）；② 归因标签（错误类别+发生阶段）；③ 分级告警（同类堆积阈值告警——系统性故障信号）；④ 重放接口（单个/批量，重放前按归因可修参数）。

**答**：
```javascript
class DLQ {
  constructor({ store, alert }) { this.store = store; this.alert = alert; }
  async dead(task, error, attempts) {
    const rec = await this.store.save({
      taskId: task.id, payload: task.payload,
      error: { message: error.message, cat: error.cat },
      attempts, trail: task.trail,               // 全量上下文
      ts: Date.now(),
      tags: [error.cat, task.stage, task.feature],
    });
    // 同类堆积告警：同 tag 1h 内 >10 条 = 系统性故障
    const recent = await this.store.countByTag(error.cat,
      { window: 3600e3 });
    if (recent > 10)
      this.alert({ type: 'dlq_pileup', tag: error.cat,
        count: recent, note: '疑似系统性故障，优先排查' });
    return rec;
  }
  async replay(ids, { patch }) {
    const results = [];
    for (const id of ids) {
      const rec = await this.store.get(id);
      // 重放前按归因修参数（如补齐缺失参数/刷新 token）
      const payload = patch?.[rec.tags[0]]
        ?.call(rec.payload) ?? rec.payload;
      results.push({ id, payload });
    }
    return results;                              // 交回执行器重跑
  }
  stats() {                                      // 死信看板
    return this.store.groupByTag({ fields: ['tags'],
      windows: ['1h', '24h'] });
  }
}
// 重试策略与 DLQ 衔接：selfHeal（AGT-484）耗尽 → dead()；
// 重放仅对"参数修复可解"的类别开放，
// permission 类直接人工处理不重放。
```

**评分点**:
- 死信记录全量上下文（payload/trail/attempts）可独立重放。
- 同类堆积告警（1h>10 条）区分系统性与偶发。
- 重放按归因修参数，且按类别限制（不可恢复类不重放）。
- stats 分组看板支撑运营。
