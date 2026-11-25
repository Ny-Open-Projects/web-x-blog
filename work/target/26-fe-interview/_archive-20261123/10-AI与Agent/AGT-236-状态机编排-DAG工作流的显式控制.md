---
title: [AGT-236] 状态机/DAG 编排——显式工作流怎么控制多 Agent？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-236：用显式 DAG/状态机编排 Agent 工作流，相比自由 Agent 有什么优势？

**答**:
- 可控性优势：每个节点的输入/输出/重试/超时/人工审批点都是显式配置——可预测、可回放、可审计，这正是企业级场景（审批流/数据管道）的刚需；自由 Agent 的动态性在这些场景是风险而非特性。
- 编排器职责：节点调度（拓扑序/并行分支）、状态持久化（每节点完成落库，支持断点续跑）、错误策略（重试/降级/短路）、观察（每节点 trace + 耗时 + 成本）。
- LLM 与 DAG 的结合方式：节点内部可以是 Agent（带工具与多轮决策），节点间的流转是确定性规则或 LLM 路由（Router 节点按分类结果选分支）——"确定性的框，智能的节点"。
- 缺点与弥补：灵活性低（新需求要改图）——用"图配置化"（YAML 定义图，热更新）+ 少量动态兜底节点（计划外的走通用 Agent）平衡。

```yaml
# DAG 定义示例
nodes:
  parse:  { agent: parser, timeout: 30s, retries: 2 }
  route:  { router: classify, branches: {bug: fix, feature: design} }
  fix:    { agent: coder, approval: true }   # 人工审批点
  deploy: { agent: deployer, depends: [fix] }
edges: [parse -> route, route -> fix, fix -> deploy]
policies: { onNodeFail: retry_then_dlq, checkpoint: perNode }
```
