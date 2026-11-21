---
title: [AGT-357] 多 Agent 的用户呈现——Agent 团队在 UI 上怎么表达？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-357：多 Agent 协作在用户界面上怎么呈现——角色化与进度可视化？

**答**:
- 角色化表达：给每个 Agent 一个明确的"角色卡"（名字/职责/擅长——"规划者/研究员/审查者"），用户能理解谁在干什么——角色化降低多 Agent 的认知负担，但避免过度拟人（用户要知道背后是系统不是人）。
- 协作可视化：任务视图展示 Agent 间的协作流（谁派给谁/谁审谁/当前在哪一环，AGT-231 拓扑的可视化），关键分歧的呈现（AGT-239 冲突仲裁过程对用户可见可干预——用户可以提前拍板）。
- 进度与责任聚合：用户视角的进度是"任务级"而非"Agent 级"（整体完成度+当前阶段），详细过程按需展开——默认聚合、详情可钻，两全。
- 交互路由：用户的问题该转给哪个 Agent（或主 Agent 转发）——对用户呈现统一的"一个入口"，多 Agent 是内部实现——用户不该需要知道内部有几个 Agent。

```jsx
<AgentFlow task={t}>
  <AggregatedProgress />        {/* 默认：任务级进度 */}
  <ExpandableFlowGraph />       {/* 展开：协作流 */}
  <ConflictCard c={t.conflict}
    onDecide={userDecide} />    {/* 分歧可干预 */}
</AgentFlow>
// 统一入口（主 Agent 路由），
// 角色卡命名职责但不拟人化。
```
