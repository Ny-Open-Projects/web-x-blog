---
title: [AGT-238] 多 Agent 的容错——超时、降级与失败传播怎么设计？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-238：多 Agent 系统里一个环节失败，怎么避免全局崩塌？

**答**:
- 失败分级：可重试错误（限流/网络抖动→指数退避重试）、可降级错误（模型超时→换便宜模型/缓存答案/跳过该增强步骤）、致命错误（数据损坏/权限失败→短路整条链并告警）——分级决定处置，处置策略在编排配置里声明。
- 失败传播控制：DAG 中下游依赖失败节点时按依赖类型决定（必需依赖→短路；可选依赖→跳过继续）；并行分支互不影响（一个分支失败不拖死其他），最终聚合时标注"部分完成"。
- 超时设计：节点级超时+全链路死线（deadline）双层——节点超时触发重试/降级，全链路死线触发整体降级（返回部分结果+缺口说明），防止僵尸链路空转烧钱。
- 事后：失败样本进评测集与告警看板，区分"偶发"与"系统性"（同类失败聚类，AGT-157 的聚类方法）——容错不是掩盖失败，而是让失败可见、可解释、可自愈。

```javascript
const policy = {
  retry: { errors: ['RATE_LIMIT','TIMEOUT'], max: 2, backoff: 'expo' },
  degrade: { onTimeout: 'cheaper_model', onNoData: 'cache_or_skip' },
  fatal: ['PERMISSION','CORRUPT_INPUT'],
  deadline: 120e3,                        // 全链路死线
};
async function runNode(n, ctx) {
  if (Date.now() - ctx.start > policy.deadline)
    return { status: 'partial', reason: 'deadline' }; // 整体降级
  try { return await exec(n); }
  catch (e) { return policy.dispatch(e, n, ctx); }     // 分级处置
}
```
