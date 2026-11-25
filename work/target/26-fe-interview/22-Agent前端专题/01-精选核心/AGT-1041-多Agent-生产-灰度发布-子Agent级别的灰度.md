---
title: [1041] 新子 Agent 上线怎么灰度
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 发布]
type: 面试题
---

## 1041：新子 Agent 上线怎么灰度

**答**：
- 子 Agent 灰度粒度：按任务类型灰度（新 coder Agent 只接 10% 的编码任务），编排器路由层实现，主流程无感。
- 影子对比：新子 Agent 影子跑（结果不采用只记录），与旧版 diff 一周，win 率达标再放量——比直接切流量安全得多。
- 失败熔断：新子 Agent 失败率超阈值自动回落旧版（路由层内置），不需要人工介入。
- 追问钩子：子 Agent 灰度和模型灰度的区别？——子 Agent 换版常连带 prompt/工具变化，评估维度更多（行为断言），影子对比要用「行为 diff」不只看最终结果。

```ts
function routeWorker(task) {
  if (task.kind === 'coding' && hash(task.userId) % 100 < CANARY_PCT) {
    return { agent: workers.coderV2, shadow: false, fallback: workers.coderV1 };
  }
  return { agent: workers.coderV1, fallback: null };
}
async function runTask(task) {
  const r = await routeWorker(task).agent.run(task);
  if (r.failed && routeWorker(task).fallback) return routeWorker(task).fallback.run(task); // 自动回落
  return r;
}
```

## 追问（补充）

**追问**：

1. 影子对比的成本怎么控？→ 只对抽样流量影子跑，按任务类型分层抽样，win 率置信区间收敛就停，同时设成本上限，超预算就缩小抽样比例。
2. 灰度期间新旧结果不一致，用户看到哪个？→ 只展示旧版结果，新版仅记录，高风险任务禁止影子执行有副作用的工具，影子结果的存储按保留期清理。
3. 什么指标决定放量？→ 任务成功率、人工改写率、平均轮次与单任务成本，任一显著劣化即停，放量按一成、三成、全量分档走。
