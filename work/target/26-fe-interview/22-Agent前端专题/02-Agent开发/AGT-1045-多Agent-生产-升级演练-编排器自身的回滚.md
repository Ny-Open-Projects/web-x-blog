---
title: [1045] 编排器（多 Agent 大脑）自身出 bug 怎么回滚
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 发布]
type: 面试题
---

## 1045：编排器（多 Agent 大脑）自身出 bug 怎么回滚

**答**：
- 编排器是「单点大脑」，它的 bug 影响所有任务，发布纪律最严：双版本热备（新旧编排器同时在线，路由层按流量切），回滚 = 路由切回，秒级。
- 「计划兼容」：新旧编排器对同一任务可能给出不同计划，进行中的任务绑定发布时的编排器版本直到完成（粘性路由），否则任务中途换大脑必乱。
- 编排器发布前置检查：任务回放测试（历史真实任务 100 条在新版重跑，与旧版结果 diff）+ 混沌场景（依赖故障时的行为对比）。
- 追问钩子：任务中途「换脑」具体会坏在哪？——子任务 ID 体系、消息协议版本、黑板状态 schema 都可能不兼容，粘性路由就是为避开这些。

```ts
const router = {
  sticky: new Map(),   // taskId -> orchestratorVer
  route(task) {
    if (!this.sticky.has(task.id)) this.sticky.set(task.id, activeVer());
    return pool.get(this.sticky.get(task.id));   // 任务全程粘住同一版本
  },
};
// 发布：新版先接 5% 新任务，旧版跑完存量后下线
async function rollout(newVer) {
  setWeight(newVer, 0.05);
  await drainPool(oldVer);                        // 等存量任务完成
  promote(newVer);
}
```
