---
title: [1185] 回归集越攒越大跑不动了，怎么分层维护
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 回归]
type: 面试题
---

## 1185：回归集越攒越大跑不动了，怎么分层维护

**答**：
- 分层三档：L1 核心层（200 条，关键路径 + 高发失败模式，MR 门禁必跑）、L2 场景层（按意图分组的 1000 条，夜间跑）、L3 归档层（历史用例，不进常规跑，只在新模型上线等大变更时全量激活）。
- 晋级与降级：L2 中反复失败的意图晋升 L1（进门禁保护）；L1 中连续 3 个月零失败且低风险的降级 L2（门禁保持精悍）。
- 分层的依据数据：每条用例记录「历史失败次数 + 意图 + 难度」，分层决策基于数据不靠感觉。
- 追问钩子：L1 会不会越来越胖？——配额硬约束：L1 上限 300 条，晋级必须同时降级等量条目，逼着团队定期审视门禁组成。

```ts
const layers = {
  L1: { cap: 300, trigger: 'MR', sel: c => c.fails >= 3 || c.risk === 'high' },
  L2: { trigger: 'nightly', sel: c => c.fails >= 1 },
  L3: { trigger: 'major-release' },
};
function rebalance() {
  const promoted = L2.filter(c => hotFailure(c));
  const demoted = L1.filter(c => dormant(c, '3m') && c.risk === 'low');
  swap(promoted, demoted, { cap: layers.L1.cap });  // 晋降配对，配额硬约束
}
```
