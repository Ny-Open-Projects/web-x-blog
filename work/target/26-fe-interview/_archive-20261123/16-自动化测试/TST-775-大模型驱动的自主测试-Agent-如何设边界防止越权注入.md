---
title: [TST-775] 大模型驱动的「自主测试 Agent」如何设边界防止越权注入
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-775：大模型驱动的「自主测试 Agent」如何设边界防止越权注入

**答**：
- 结论：Agent 要有「最小权限 + 动作白名单 + 人类确认高危动作」三层边界，绝不给它无限制的注入/执行权限。
- 权限按环境分级：只读环境可自主探索，预发执行需审批，生产注入必须人确认且限时。
- 动作白名单把 Agent 能调用的工具收敛到安全集合，越界请求直接拒绝并记录。
- 追问钩子：Agent 通过多个低危动作组合出高危效果，如何防范？

```javascript
// Agent 动作网关：权限 + 白名单 + 高危确认
const SAFE = new Set(['readLog', 'queryMetric']);
function agentAction(action, env, confirmed) {
  if (SAFE.has(action)) return { allow: true };
  if (action === 'injectFault') {
    if (env === 'prod') return { allow: !!confirmed };
    return { allow: true }; // 预发可自主
  }
  return { allow: false, why: '动作不在白名单' };
}
console.log(agentAction('injectFault', 'prod', false)); // allow:false
```
