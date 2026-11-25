---
title: [TST-770] AI×混沌：面试官问「能不能让 AI 自动做混沌实验」
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-770：AI×混沌：面试官问「能不能让 AI 自动做混沌实验」

**答**：
- 结论：可以「AI 辅助自动化」，不宜「AI 全自动无人值守」——注入是破坏性操作，必须有人在环（human-in-the-loop）把关爆炸半径与回滚。
- 可全自动：稳态监测、日志聚合、假设候选生成、结果初步分析；需人确认：注入决策、爆炸半径、生产环境执行。
- 全自动的前提是「强沙箱 + 硬熔断 + 可秒级回滚」，且仅在内网/预发环境。
- 追问钩子：如果一定要全自动跑生产混沌，最低限度要有哪些保护？

```javascript
// AI 自动混沌的分级授权
function autoChaos(env, action, hasHumanApproval) {
  const destructive = ['inject', 'rollback-disable'];
  const autoSafe = ['monitor', 'analyze', 'hypothesize'];
  if (autoSafe.includes(action)) return { run: true, by: 'AI' };
  if (destructive.includes(action)) {
    return env === 'prod'
      ? { run: hasHumanApproval, by: 'human-gated' }
      : { run: true, by: 'AI-sandbox' };
  }
  return { run: false, by: 'none' };
}
console.log(autoChaos('prod', 'inject', false)); // run:false
```
