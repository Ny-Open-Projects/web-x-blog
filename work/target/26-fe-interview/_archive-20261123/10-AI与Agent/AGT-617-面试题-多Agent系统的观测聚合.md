---
title: [AGT-617] 主 Agent 调三个子 Agent，观测上如何聚合（总耗时/总成本/瓶颈子任务）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-617：主 Agent 调三个子 Agent，观测上如何聚合（总耗时/总成本/瓶颈子任务）

**答**：
- 树状聚合：root 汇总 = 子树 span 的并集去重聚合（耗时用关键路径而不是简单相加——并行子任务的耗时取 max）；成本/ token 可加总。
- 瓶颈识别：关键路径算法（树中决定总时长的链路），输出"本轮被子 Agent B 的检索卡了 12s"这种可行动结论。
- 子 Agent 独立 SLA：每个子 Agent 有自己的成功率/延迟预算，父任务失败时能定位"哪个子任务先崩的"（首个失败节点传播链）。

```javascript
function aggregate(root) {
  return {
    cost: sumTree(root, 'cost.usd'),                 // 可加总
    duration: criticalPath(root),                    // 关键路径非相加
    bottleneck: criticalPath(root).spans.at(-1),     // 瓶颈节点
    subSla: root.children.map(c => ({
      name: c.name, ok: c.status === 'ok', p95: pct(c.duration, 0.95) })),
  };
}
function firstFailure(root) {                        // 失败传播链
  const path = []; let n = root;
  while (n && n.status === 'error') { path.push(n); n = n.children.find(c => c.status === 'error'); }
  return path;
}
```

