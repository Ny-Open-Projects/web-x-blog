---
title: [AIC-217] Cursor 的 rules 与会话 memory（记忆文件）有什么区别？什么信息该放哪边？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-217：Cursor 的 rules 与会话 memory（记忆文件）有什么区别？什么信息该放哪边？
**答**：
- rules 是团队级、版本化、评审过的约束；memory 是个人/项目级、AI 自动沉淀的经验笔记。
- 稳定规范进 rules（可复现、对全队生效），临时上下文与个人偏好进 memory。
- memory 要定期人审：AI 沉淀的错误经验会持续误导后续会话。
- 有价值的 memory 经评审可以「晋升」为正式规则。

```javascript
const promotion = (mem: MemoryNote) => ({
  eligible: mem.verifiedBy >= 3 && mem.kind === 'convention', // 被多次验证的约定
  flow: 'memory → PR 提案 → 规则评审 → rules/xxx.mdc → evalSet 验证',
});
r
```
