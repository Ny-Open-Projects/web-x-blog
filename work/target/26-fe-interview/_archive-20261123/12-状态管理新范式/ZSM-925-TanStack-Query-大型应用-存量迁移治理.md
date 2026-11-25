---
title: [925] 存量项目迁移到 TanStack Query 的路径
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 迁移]
type: 面试题
---

## 925：存量项目迁移到 TanStack Query 的路径

**答**：
- 迁移评估先行：盘点存量数据的真相来源——服务端状态域迁 Query（受益最大）、客户端 UI 域留原地或迁 Zustand、领域逻辑抽服务层后再判断。
- 迁移顺序：新功能零 Redux（冻结增量）-> 读多写少的数据域先迁（风险低收益立现）-> 写操作域 mutation 化 -> 最后清 Redux 残壳。
- 双轨期治理：过渡期同实体两个来源（禁止！），用「适配器」——Redux selector 内部读 Query 缓存（单向流动）直到旧域退役。
- 验收指标：请求去重率、store 代码行数、页面数据一致性 bug 数——迁移是工程，要有指标证明收益。

```ts
// 过渡期适配器：Redux selector 读 Query 缓存
export const selectUser = (state, id) => (qc) =>
  qc.getQueryData(userKeys.detail(id)) ?? legacyFromRedux(state, id);
// 迁移验收：去重率提升 / store 行数下降 / 一致性 bug 归零
```

