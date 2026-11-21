---
title: [ARC-432] AI 时代前端架构的转型点：哪些层被重写？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-432：AI 时代前端架构的转型点
**答**:
- 正在变化的层：代码生产（AI 生成让"写码速度"不再是瓶颈，瓶颈移向需求澄清/验收标准/架构判断）、交互范式（自然语言 UI、生成式 UI——界面按意图即时组装）、测试（AI 生成用例但验收标准人工定义）。
- 不变的层：架构边界（模块化/分层/契约——AI 生成也需要可维护结构）、状态与数据一致性、性能与安全工程、可观测性。
- 架构应对：把"AI 可执行的规范"结构化（lint 规则/类型/ADR 即 prompt 上下文，ARC-147）；组件协议化（schema 描述能力，供 AI 编排）；验收自动化（测试即规格）。
- 生成式 UI 架构：意图 → 组件编排引擎（受控物料集合 + 权限与安全边界内渲染），AI 输出受限 DSL 而非自由 HTML——可控性优先于表达力。
- 团队转型：工程师从实现者转向"规格定义者 + AI 产出验收者"；架构师负责设计 AI 友好的工程环境（强类型/自动测试/清晰边界）。
```javascript
// 生成式 UI 的受控渲染
const allowedMaterials = { card: GoodsCard, table: DataTable, form: SchemaForm }; // 白名单物料
function renderAIUI(dsl) {
  if (!validateDSL(dsl)) return showFallback();                 // AI 输出先过校验
  return dsl.nodes.map(n => {
    const C = allowedMaterials[n.type];
    if (!C) return null;                                        // 未授权物料拒绝渲染
    return <C {...sanitize(n.props)} />;                        // props 白名单清洗
  });
}
```
