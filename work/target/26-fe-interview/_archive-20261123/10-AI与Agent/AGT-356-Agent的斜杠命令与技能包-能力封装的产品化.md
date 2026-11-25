---
title: [AGT-356] 技能包/命令包——Agent 能力的产品化封装？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-356：把 Agent 能力封装成"技能包/命令"（用户一键调起）怎么设计？

**答**:
- 封装价值：裸 Agent（自由对话）→ 封装技能（`/周报`一键生成、`/排错`走固定诊断流）——封装把 prompt/工具/流程/SOP 打包成产品能力，用户体验从"会聊"变成"会用"，质量也从自由发挥变成标准化执行。
- 技能包结构：元信息（名称/描述/适用场景）、模板（参数化 prompt）、工具集（该技能可用的工具白名单）、流程（可选的 DAG 步骤）、验收（输出格式约束）——技能包是场景包（AGT-328）的最小单元。
- 发现与调用：命令面板（/ 唤起+搜索）、自然语言意图路由（用户说"帮我写周报"自动匹配技能）、技能间组合（技能输出可入下一个技能输入——pipeline）。
- 治理：技能包版本化（AGT-321 同款流程：评测→灰度→发布）、质量基线（每个技能有自己的评测集）、废弃流程（低使用率技能下线）——技能市场是 Agent 平台的产品形态。

```javascript
const skill = {
  id: 'weekly-report',
  desc: '生成本周工作周报（三段式）',
  prompt: loadTemplate('weekly-report@v3'),
  tools: ['git.log', 'tracker.myTasks'],   // 白名单
  schema: REPORT_SCHEMA,                   // 输出约束
  eval: 'weekly-report-suite',             // 专属评测
};
// /weekly-report 或意图路由触发；
// 版本化发布走评测→灰度→全量。
```
