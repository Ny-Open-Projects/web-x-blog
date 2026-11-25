---
title: [1122] 下游 Agent 引用上游结论时，怎么处理「结论过期」
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 一致性]
type: 面试题
---

## 1122：下游 Agent 引用上游结论时，怎么处理「结论过期」

**答**：
- 引用要带版本：下游消费上游结论时记录「结论 id + 生成时间 + 依赖的数据版本」；上游重新计算后，广播「结论作废」事件，依赖方标记过期并决定重算或接受。
- 「接受旧结论」要分类：展示类可以旧（标注数据时间），决策类必须重算（决策基于过期结论就是事故）。
- 级联作废：A 的结论依赖 B 的，B 作废则 A 级联作废——依赖图反向传播，和构建系统的 affected 计算同构。
- 追问钩子：频繁重算会不会成本爆炸？——加「合并窗口」（短时间多次作废合并成一次重算）与「惰性重算」（下次真正被消费时才算）。

```ts
class Conclusions {
  deps = new Map();   // id -> 依赖的结论 id
  invalidate(id) {    // 级联作废：反向依赖传播
    for (const [cid, ds] of this.deps) if (ds.has(id)) this.invalidate(cid);
    bus.emit('stale', id);
  }
}
bus.on('stale', async id => {
  const c = store.get(id);
  if (c.usage === 'decision') await recompute(id);       // 决策类必须重算
  else store.mark(c, { stale: true, asOf: c.ts });       // 展示类标注即可
});
```

