---
title: [AIC-044] AI Review 发现的什么问题应该「阻断合并」？阻断策略怎么设计才不会卡死流程？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-044：AI Review 发现的什么问题应该「阻断合并」？阻断策略怎么设计才不会卡死流程？
**答**：
- 只阻断三类：安全红线（密钥泄漏、XSS/注入点）、数据正确性（明显的空指针/竞态/金额精度）、约定的不可破坏（公共 API 签名变更未走评审）。
- 其余一律 suggestion：风格、命名、可疑但不确证的逻辑，交给人类判断——阻断面越大，豁免申请越多，门禁权威性越差。
- 豁免机制必须有：blocker 允许「本人确认 + 上级 ack」豁免并留痕（写明理由），豁免率也是监控指标——长期 0 豁免说明阈值太松，10%+ 说明阈值太严。
- 阻断实现上挂在 CI status check，而不是聊天区喊话；意见必须可一键跳转到代码位置。
- 追问钩子：阻断与「误报治理」是跷跷板——每次调阈值都要用历史 PR 回放验证（不引入新误报阻塞的前提下多抓真问题）。

```javascript
// 阻断决策 + 豁免留痕
function gate(findings, exemptions) {
  const blockers = findings.filter(f => f.level === 'blocker' && f.confidence >= 0.8);
  const unblocked = blockers.filter(b => !exemptions.some(e => e.id === b.id && e.ack));
  if (unblocked.length) {
    return { pass: false, reasons: unblocked.map(b => `${b.file}:${b.line} ${b.issue}`) };
  }
  return { pass: true, exempted: blockers.length - unblocked.length };
}
```
