---
title: [AIC-293] 什么情况下应该绕过工具直接用模型 API 自建工作流？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-293：什么情况下应该绕过工具直接用模型 API 自建工作流？
**答**：
- 需求是流程级而非编码级：批量代码审查、自动修复 CI、测试生成流水线——需要编程控制。
- 需要深度定制：私有上下文引擎、特殊校验逻辑、成本精细控制。
- 代价：自己处理重试/超时/结构化输出/上下文管理，工程量不小。
- 判断标准：如果工具的 80% 能力用不上且瓶颈在「编排」而非「模型」，走 API 自建。

```javascript
const buildVsBuy = (need: Need) => ({
  buy: need.kind === 'interactive-coding' || need.teamSize < 5,
  api: need.kind === 'pipeline' || need.customCtx === true,
  hybrid: '工具覆盖日常编码 + API 自建 CI 流水线（共享规则资产）',
});
r
```
