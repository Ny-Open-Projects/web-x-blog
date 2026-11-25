---
title: [AIC-512] AI diff 审查的最小 diff 原则
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-512：最小 diff 原则

**答**:
- 最小 diff 原则：1) **AI 只生成必要变更**（AI 倾向于"重写整个文件"——人的审查成本 = diff 大小；最小 diff = 只改需要的行（其余不动——审查负担最小化）；2) **最小 diff 的 prompt 约束**（"只修改 X 函数，不要动其他代码"——显式约束 AI 的变更范围 RBL-506 prompt 精确性）；3) **diff 审查的效率**：diff < 50 行 = 快速审查（5 分钟）；diff > 500 行 = 需要 PR review（15 分钟+）——审查成本与 diff 大小成正比。
- AI 的"过度重写"倾向：1) **重排 import**（AI 自动排序 import——与项目无关的变更——噪声 diff）；2) **重命名变量**（AI"优化"命名——非必要变更）；3) **改格式**（AI 重排空格/引号——格式化噪声）；「噪声 diff 的过滤」：diff 的语义变更 vs 格式变更分离（语义 = 需要审；格式 = 忽略——git diff --ignore-all-space + 语义 diff 工具）。
- 追问钩子：为什么「最小 diff」比「完整重写」的审查效率高？——完整重写：人需要理解 AI 的整个实现（1000 行——10 分钟+）；最小 diff：人只需要看变更部分（20 行——2 分钟）；「审查的认知负担」：完整重写 = 从零理解 AI 的思路；最小 diff = 在已有理解上验证变更（上下文已有——增量认知负担）；最小 diff 的信任建立：小的 diff 审查通过 → 对 AI 的信任增加 → 大的 diff 也敢审（信任的累积效应）。

```typescript
// diff 的语义过滤
function filterSemanticDiff(diff: string[]) {
  const NOISE = [/^\s*$/, /^[-+]\s*import\s/, /^[-+]\s*import\s+type\s/, /^\s*$/, /^[-+]\s*\/\/\s*/];
  const semantic = diff.filter(line =>
    !NOISE.some(pattern => pattern.test(line) && line.match(/^[-+]/)));
  const noiseLines = diff.length - semantic.length;
  return { semantic, noiseLines, noiseRatio: diff.length ? +(noiseLines / diff.length * 100).toFixed(1) : 0 };
}
// diff 审查分级
function reviewEffort(diffLines: number) {
  if (diffLines <= 50) return { level: 'quick', estMin: 5 };
  if (diffLines <= 200) return { level: 'normal', estMin: 15 };
  return { level: 'thorough', estMin: 30 };
}
// 最小 diff 的 prompt 约束
const MIN_DIFF_PROMPT = `Only modify the specified function. Do NOT:
- Re-sort imports
- Rename variables
- Change formatting
- Add comments to unchanged code`;
```
