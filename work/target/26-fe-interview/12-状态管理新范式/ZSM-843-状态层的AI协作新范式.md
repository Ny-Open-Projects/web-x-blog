---
title: [ZSM-843] 状态层的 AI 协作新范式：把状态规范喂给 AI 的工程化方法
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-843：状态层的 AI 协作新范式：把状态规范喂给 AI 的工程化方法

**答**：
- AI 编码助手（Copilot/Claude/Cursor）写状态代码的质量取决于**给它的规范上下文**——把本库的治理资产变成 AI 可消费的规范文件是新的工程任务：
- **规范注入三层**：1) 全局层（AGENTS.md/Cursor rules）——分层规范（ZSM-776）、命名约定、审计八问（766）作为系统约束；2) 域层——每个 store 的 ADR（712）放同目录（AI 读文件时自然带上决策上下文）；3) 示例层——「标准 store 模板」（含 selector 拆分/退订/评分点注释的范例）让 AI few-shot。
- **AI 产出的验收闭环**：AI 写的 store 过 lint（780 自定义规则）+ 契约测试——「AI 写代码、CI 管纪律」取代「AI 写代码、人肉眼审」；审计八问直接作为 AI 的 self-check prompt。
- 反模式：把全部代码塞给 AI（上下文爆炸质量降）——正确姿势是「按层注入」（全局规范 + 当前域 ADR + 相邻 1-2 个文件）；AI 幻觉状态库 API（编造不存在的方法）→ 用类型定义约束（AI 产出的代码必须过 tsc）。
- 高杠杆用法：用 AI 批量做「机械迁移」（ZSM-714 的 codemod 替代——自然语言描述迁移规则，AI 生成 jscodeshift 脚本）；用 AI 生成竞态测试用例（审计八问逐条生成）。
- 追问钩子：AI 协作的度量——「AI 产出的一次通过率」（过 lint+tsc+测试的比例）作为规范质量反推指标：通过率低说明规范没写清楚，先修规范再怪 AI。

```javascript
// AI 协作的规范注入三层
const AI_SPEC_INJECTION = {
  全局层: {
    file: 'AGENTS.md / .cursorrules',
    content: [
      '分层规范（776）：core/domain/feature/ui 依赖方向',
      '命名约定：useXxxStore / xxxStoreApi / xxxAtom',
      '审计八问（766）作为 self-check',
      '禁令：渲染期写状态、subscribe 不退订、persist 无 partialize',
    ],
  },
  域层: {
    file: 'stores/domain/cart/ADR.md（与 store 同目录）',
    content: '决策背景/否决方案/边界——AI 读文件自然带上上下文',
  },
  示例层: {
    file: 'templates/store.template.ts',
    content: '标准模板：selector 拆分 + useShallow + 退订 + 评分点注释（few-shot）',
  },
}

// 验收闭环
const AI_ACCEPTANCE = {
  pipeline: 'AI 产出 → eslint(自定义状态规则) → tsc → 竞态测试 → 合入',
  selfCheck: '审计八问作为 AI prompt 的一部分（产出前自检）',
  antiPattern: [
    '全代码塞上下文（爆炸降质）——按层注入',
    'AI 幻觉 API——必须过 tsc',
    '人肉眼审 AI 代码——CI 管纪律',
  ],
  高杠杆: [
    'AI 生成 codemod 脚本（714 机械迁移）',
    'AI 按八问逐条生成竞态测试用例（624）',
  ],
  metric: '一次通过率（过 lint+tsc+test）——低则先修规范',
}
```
