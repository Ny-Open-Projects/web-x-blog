---
title: [931] 多 Agent 系统里子 Agent 挂了怎么保证整体可用
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 容错]
type: 面试题
---

## 931：多 Agent 系统里子 Agent 挂了怎么保证整体可用

**答**：
- 失败分级：可重试错误（网络/限流）走指数退避重试；确定性失败（工具不存在、参数非法）不重试直接换路径；子 Agent 超预算（轮次/token）强制终止并上报。
- 降级链：专业 Agent 失败 → 通用 Agent 兜底 → 静态话术/人工；每一级都记录失败原因，降级率是核心监控指标。
- 部分成功策略：DAG 里非关键路径失败允许继续（结果标注缺失），关键路径失败才整体失败——编排器声明哪些边是关键的。
- 追问钩子：重试会不会放大故障？——会，重试预算全局共享（如全任务最多 3 次重试），防止风暴式重试打挂下游。

```ts
async function runStep(step, budget) {
  for (let i = 0; i < budget.retry; i++) {
    try { return await workers[step.type].run(step); }
    catch (e) {
      if (!e.retryable || budget.retryLeft <= 0) break;  // 全局重试预算
      budget.retryLeft--;
      await sleep(2 ** i * 500);                          // 指数退避
    }
  }
  if (step.critical) throw e;
  return { ok: false, degraded: true, reason: String(e) }; // 非关键降级继续
}
```

