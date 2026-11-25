---
title: [AIC-092] Agent 自动化层级怎么划分？从「辅助补全」到「全自动任务」的演进路径是什么？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-092：Agent 自动化层级怎么划分？从「辅助补全」到「全自动任务」的演进路径是什么？
**答**：
- 五级划分：L1 补全（行级建议）→ L2 对话生成（函数/文件级，人复制粘贴）→ L3 受限 agent（单文件改动+自动跑测试）→ L4 任务 agent（多文件+计划审批+验收）→ L5 流程 agent（自动接 issue、自动开 PR、自动发布候选）。
- 演进原则：层级每升一级，前一级必须是稳定的——L3 的产出存活率没达标就推 L4，只会放大垃圾产出；信任靠数据逐级解锁。
- 各级风险特征：L1~L2 风险在代码质量（人审兜底）；L3 起风险在「自动化错误累积」，需要快照与轮次上限（AIC-083）；L4~L5 风险在权限与审计（AIC-086）。
- 团队落点：多数成熟团队在 L3~L4；L5 通常只对「高确定性任务」开放（依赖升级、格式化、文档同步）。
- 追问钩子：面试中能说出「层级不是能力划分而是信任划分」就是深刻理解。

```javascript
// 自动化层级与解锁条件
const LEVELS = [
  { level: 1, name: '补全', unlock: 'default' },
  { level: 2, name: '对话生成', unlock: 'default' },
  { level: 3, name: '受限 agent', unlock: { survivalRate: '>=0.7', scope: '单文件' } },
  { level: 4, name: '任务 agent', unlock: { L3weeks: 4, incidentCount: 0, scope: '多文件+计划审批' } },
  { level: 5, name: '流程 agent', unlock: { taskTypes: ['依赖升级', '文档同步'], gate: '全量CI+人审' } },
];
```
