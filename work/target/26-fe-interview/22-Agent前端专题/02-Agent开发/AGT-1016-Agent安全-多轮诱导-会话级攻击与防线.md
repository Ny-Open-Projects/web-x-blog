---
title: [1016] 多轮对话的「温水煮蛙」式诱导怎么防
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 会话攻击]
type: 面试题
---

## 1016：多轮对话的「温水煮蛙」式诱导怎么防

**答**：
- 攻击形态：第一轮建立无害上下文（角色扮演框架），中间轮逐步加码约束松绑，最后一轮触发危险请求——每条单独看都无害，会话轨迹才是攻击本体。
- 防线三件套：会话级风险分（对整段对话轨迹打分，不是逐条）、关键轮次重置（检测到话题跃迁时重申系统约束）、危险动作的前置审批不依赖对话内容（权限硬编码，话术改变不了权限）。
- 上下文「信任清洗」：用户早期轮次里自设的「规则」（比如「从现在起你可以忽略安全要求」）不能沉淀为事实——系统约束只来自 system prompt，用户消息里出现规则性声明一律降级为「待验证请求」。
- 追问钩子：怎么检测「约束松绑」趋势？——对每轮提取「请求类型 × 风险等级」序列，风险等级单调上升且跨过中危阈值即触发审查。

```ts
function sessionGuard(turns) {
  const risks = turns.map(t => classifyRisk(t));
  const ladder = risks.filter(r => r.level >= 2).length;
  if (isMonotonicRising(risks) && risks.at(-1).level >= 3) {
    return { action: 'deep_review', reason: 'escalating pattern' }; // 温水煮蛙
  }
  // 用户消息里的「规则声明」不进入事实层
  const clean = turns.map(t => t.content.replace(/从现在起(你可以|请)?忽略.*/g, '[用户规则声明已忽略]'));
  return { action: 'pass', clean };
}
```
