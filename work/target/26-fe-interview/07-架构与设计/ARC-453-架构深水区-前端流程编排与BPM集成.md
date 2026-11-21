---
title: [ARC-453] 前端如何承载流程编排（BPM/审批流可视化）？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-453：前端承载流程编排（BPM/审批流可视化）
**答**:
- 职责边界：前端负责流程的"可视化与交互"（画流程图、节点表单、进度展示），执行引擎永远在服务端——前端不下发流程逻辑执行。
- 设计器架构：节点模型（节点类型注册表：审批/条件/并行/子流程，各有 schema）+ 连线模型（DAG 校验：无环、可达终点）+ 画布（React Flow/X6 封装）+ 序列化（BPMN 或自定义 JSON，与服务端引擎对齐）。
- 渲染器架构：同一份流程定义两个消费方——设计器（编辑态）与进度视图（运行态：已走路径高亮、当前节点标注、并行分支展示）。运行态数据来自引擎事件。
- 表单联动：节点绑定表单 schema（ARC-094），审批人看到的表单由节点定义 + 权限决定；驳回回到指定节点时表单回填。
- 版本兼容：流程定义版本化，进行中的实例按创建版本执行，新版本只影响新实例——前端进度视图要按实例版本渲染。
```javascript
// 流程定义序列化（简化）
const flowDef = {
  version: 3,
  nodes: [
    { id: 'start', type: 'start' },
    { id: 'approve1', type: 'approval', form: 'expense-form', assignee: 'role:manager' },
    { id: 'cond', type: 'exclusive', branches: [{ to: 'approve2', when: { fact: 'amount', op: 'gt', value: 5000 } }, { to: 'end' }] }
  ],
  edges: [['start', 'approve1'], ['approve1', 'cond'], ['cond', 'end']]
};
// DAG 校验：拓扑排序可达 + 无环校验在保存时执行
```
