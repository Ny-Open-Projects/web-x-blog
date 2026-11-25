---
title: [AIC-228] 架构评审的 AI 提示词需要准备哪些上下文材料？缺了会怎样？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-228：架构评审的 AI 提示词需要准备哪些上下文材料？缺了会怎样？
**答**：
- 必备：分层规则、相关 ADR、目录结构约定、变更 diff、既有同类实现示例。
- 加分：业务背景（为什么改）、性能约束、团队技术路线图。
- 缺业务背景 → AI 会用通用最佳实践评判，结论看似专业但不落地。
- 缺既有示例 → AI 推荐与仓库风格冲突的方案。上下文优先级：仓库事实 > 规范 > 通用知识。

```javascript
const ctx = {
  must: ['layerRules.md', 'relatedADRs/', 'dirConvention.md', 'diff.patch', 'similarImpl/*.ts'],
  nice: ['businessContext.md', 'perfBudget.json', 'roadmap.md'],
  priority: 'repo facts > standards > general knowledge',
};
r
```
