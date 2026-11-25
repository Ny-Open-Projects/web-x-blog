---
title: [NODE-795] 笔试题——实现多级超时编排器（树形 deadline 分配）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-795：手写超时编排

**需求与边界**：
- 需求：树形调用链的超时编排（SCN-NODE-642/728）——① 树形预算分配（父节点预算按子节点权重分配——剩余动态再分配）；② 快子节点完成预算回收（前序完成后剩余分配后序——SCN-NODE-728）；③ 关键子调用保障（must 子调用预算不足时抢占 may 的——优先级分配）。
- 边界：① 预算分配比例声明（权重配置化）；② 时钟漂移容忍（±1s——SCN-NODE-728）；③ 分配日志（预算分配与实际使用——调参依据）。

**答**：
```javascript
class TimeoutTree {
  async run(node, budget) {                            // 树形递归分配
    const weights = node.children.map(c => c.weight ?? 1);
    const alloc = weights.map(w => budget * w / sum(weights));   // 按权重分配
    const results = await Promise.all(node.children.map(async (c, i) => {
      const childBudget = Math.min(alloc[i], remaining(node));   // 不超父剩余
      if (childBudget < c.min) {                       // 关键子调用不足 → 抢占 may 的预算
        if (c.criticality === 'must' && node.hasStealable())
          return this.run(c, stealBudget(node, c));    // 抢占分配（SCN-NODE-795）
        throw new BudgetExhausted(c.key);
      }
      return this.run(c, childBudget);
    }));
    if (node.call) {                                   // 节点自身调用
      const used = performance.now() - node.start;
      node.children.forEach(c => { /* 回收：剩余预算归父 */ });
      return node.call(node, results);
    }
    return results;
  }
}
```

**评分点**:
- 树形权重分配（子节点预算按权重——SCN-NODE-642 预算制进阶）。
- 剩余动态回收（前序完成后重分配——SCN-NODE-728）。
- 关键子调用抢占（must 抢 may 预算——优先级分配）。
- 分配日志（调参依据）。
