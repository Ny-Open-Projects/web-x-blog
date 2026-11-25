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

**追问**：

1. 生成式 UI 只给 AI 白名单物料，怎么防提示注入让它输出越权内容？ → DSL 只允许枚举物料与受控 props，渲染前按 props schema 校验类型与范围，数据权限由服务端按当前用户二次过滤，AI 能改排列但改不了数据范围。
2. 你说写码不再是瓶颈，那架构投入的收益怎么度量？ → 不看代码行与 PR 数，看交付周期、变更失败率、回滚耗时这类 DORA 指标，加上需求澄清到上线的端到端时长。
3. 团队里没人愿意当验收者，转型推不动怎么办？ → 从可执行资产切入：契约、mock、测试即规格，先让验收标准变成 CI 能跑的东西，人的角色随工具落地自然迁移。
