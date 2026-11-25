---
title: [WCN-419] 笔试：信号系统的性能计数器（写放大检测）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-419：笔试：信号系统的性能计数器（写放大检测）。
**答**：dev 模式统计：每信号写次数/每 computed 重算次数/每 effect 执行次数。`report()` 输出写放大比（effect 执行总数 / 写总数）。

```javascript
const stats = { writes: 0, effectRuns: 0, computedRuns: 0, perNode: new Map() };
function instrument(node) {
  const origSet = node.set?.bind(node);
  if (origSet) node.set = v => { stats.writes++; stats.perNode.set(node.name, (stats.perNode.get(node.name) || 0) + 1); origSet(v); };
}
function report() {
  const amp = stats.writes ? stats.effectRuns / stats.writes : 0;
  const hot = [...stats.perNode].sort((a, b) => b[1] - a[1]).slice(0, 5);
  return { writes: stats.writes, amplification: +amp.toFixed(1),
    warn: amp > 10 ? '写放大异常，检查信号粒度' : 'ok', hot };
}

```

**评分点**：
- 计数器挂节点（dev only）。
- 写放大 = effectRuns / signalWrites（> 10 异常）。
- 热点节点排行（重算次数 topN）。
- 生产零开销（dev 标记构建剔除）。
