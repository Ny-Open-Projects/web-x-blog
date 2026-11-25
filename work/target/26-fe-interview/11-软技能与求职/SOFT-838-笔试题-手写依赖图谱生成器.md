---
title: [SOFT-838] 手写 depGraph：协作依赖的图谱构建（谁依赖谁的交付物）、瓶颈节点识别、变更影响面查询？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-838：手写 depGraph：协作依赖的图谱构建（谁依赖谁的交付物）、瓶颈节点识别、变更影响面查询

**需求与边界**：
- 实现 buildDepGraph(deps)：deps 每条 { from, to, artifact }（from 依赖 to 的 artifact）。
- 边界要求：① 图构建+查询：impactOf(node)（该节点变更影响的上游集合——闭包）、bottleneck()（被依赖最多的节点=全局风险 SOFT-823）；② 环检测（from 与 to 互相依赖→循环依赖告警——SOFT-823 链条脆弱）；③ 断点查询：若节点失效哪些链断——预案建议输出。

**答**：
```javascript
function buildDepGraph(deps) {
  const edges = deps;
  const impactOf = (node) => {                    // node变更影响的上游闭包
    const affected = new Set(); const queue = [node];
    while (queue.length) {
      const cur = queue.shift();
      for (const d of edges)
        if (d.to === cur && !affected.has(d.from)) {
          affected.add(d.from); queue.push(d.from);
        }
    }
    return [...affected];
  };
  const bottleneck = () => {
    const count = {};
    for (const d of edges) count[d.to] = (count[d.to] ?? 0) + 1;
    const max = Math.max(...Object.values(count), 0);
    return { nodes: Object.entries(count)
      .filter(([, v]) => v === max && max > 1).map(([k]) => k),
      note: '被依赖最多=全局风险节点——重点保护+断点预案（SOFT-823）' };
  };
  const cycles = (() => {                         // 环检测
    const found = [];
    for (const d of edges)
      if (edges.some(x => x.from === d.to && x.to === d.from))
        found.push([d.from, d.to]);
    return found;
  })();
  return { impactOf, bottleneck,
    cycles, cycleWarning: cycles.length
      ? `循环依赖：${cycles.map(c => c.join('↔'))}——链条脆弱告警`
      : null };
}
```

**评分点**:
- 变更影响面闭包（上游传导计算——变更通知契约的数据基础 SOFT-823）。
- 瓶颈节点识别（被依赖最多=全局风险）。
- 环检测（互依链条的脆弱告警）。

