---
title: [AIC-522] AI 编码规范与团队一致性
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-522：AI 编码规范与团队一致性

**答**:
- AI 时代团队编码规范的挑战：1) **一致性丧失**（每人用不同 AI + 不同 prompt → 代码风格不一致——AI 生成的代码风格取决于 LLM 的训练数据（每个 LLM 的"默认风格"不同）；2) **规范的AI化**：Cursor Rules/.cursorrules（RBL-510）让 AI 遵守团队规范——但"规则的遵守度"取决于 LLM 能力（GPT-4 遵守 90%、小模型遵守 60%——规范遵守度 = LLM 能力 × 规则清晰度）；3) **lint 的兜底**：AI 不遵守规范 → ESLint/Prettier 强制（lint 是规范的最后防线——AI 生成的代码也要过 lint）；4) **规范的进化**：AI 时代的新规范——"AI 生成的代码必须标注 provenance"（RBL-942）、"AI 写的测试必须人审"（RBL-504）。
- 团队一致性的度量：AI 代码风格与人代码风格的一致度（AST 对比——AI 生成的代码 vs 团队风格指南的匹配度）；「一致性的度量 = 代码审查的负担」：不一致 → 审查时指出风格问题（额外负担）；一致 → 审查只看逻辑（效率高）。
- 追问钩子：为什么「lint 兜底」在 AI 时代更重要了？——AI 时代代码生成速度 >> 人写速度（AI 1 秒生成 100 行——人 10 分钟写 100 行）；代码量增长 → 风格不一致的概率增长 → 人审风格的时间增长；lint 自动化 = 风格问题的零人工成本（lint 自动修复——人不需要关心风格）；「AI 生成 → lint 自动修 → Prettier 统一」的流水线让「风格一致性」从人工审查降为零成本自动化——AI 时代 lint 的角色从「代码质量检查」升级为「AI 输出的规范化管道」。

```typescript
// AI 时代的团队编码规范流水线
// 1. AI 生成（Cursor + Cursor Rules 团队规范）
// 2. ESLint（规范检查 + 自动修复）
// 3. Prettier（格式统一）
// 4. TypeScript（类型检查）
// 5. 人工审查（只看逻辑，不看风格）
const PIPELINE = [
  { step: 'ai-generate', tool: 'cursor', humanTime: 0 },
  { step: 'lint-fix', tool: 'eslint --fix', humanTime: 0 },     // 风格自动修
  { step: 'format', tool: 'prettier --write', humanTime: 0 },   // 格式自动修
  { step: 'typecheck', tool: 'tsc --noEmit', humanTime: 30 },   // 类型自动检
  { step: 'review', tool: 'human', humanTime: 120 },            // 人审逻辑
];
// AI 时代代码审查的焦点转移
// 旧：风格 + 逻辑 + 类型 + 安全 → 全审
// 新：风格 = 自动修 / 类型 = 自动检 / 安全 = 自动扫 → 人审只看逻辑
```
