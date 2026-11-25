---
title: [1042] 子 Agent 依赖的模型版本怎么锁定与升级
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 供应链]
type: 面试题
---

## 1042：子 Agent 依赖的模型版本怎么锁定与升级

**答**：
- 每个 Agent 声明「模型依赖清单」（模型名 + 版本 + 行为基线指纹），编排器启动时校验——版本不符拒绝启动，杜绝「供应商悄悄升级导致子 Agent 行为漂移」。
- 升级流程：新版本先在影子环境跑该 Agent 的专属评估集，行为基线 diff 通过才改依赖声明——和依赖包升级一个纪律。
- 多 Agent 共享模型版本要协调：一个 Agent 升级、另一个不升会产生「协作接口不匹配」（输出格式漂移），依赖清单集中管理（版本锁文件进 Git）。
- 追问钩子：锁版本的代价？——享受不到供应商的免费改进与新功能，所以要定期（季度）主动评估升级，把「被动漂移」变「主动升级」。

```json
// agents.lock —— 模型依赖锁文件，进 Git
{ "coder-1": { "model": "qwen-coder@2025-09", "baseline": "fp-a1b2" },
  "reviewer-1": { "model": "glm-4-plus@2025-08", "baseline": "fp-c3d4" } }
```

```ts
function startupCheck(lock) {
  for (const [agent, dep] of Object.entries(lock)) {
    const cur = fingerprint(dep.model);
    if (cur !== dep.baseline) throw new Error(`${agent} model drift: ${dep.model}`); // 拒绝启动
  }
}
```
