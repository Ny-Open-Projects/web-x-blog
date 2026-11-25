---
title: [AIC-572] AI 代码的 Copyright 合规
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-572：AI 代码的 Copyright 合规

**答**:
- AI 代码的版权风险：1) **训练数据泄露**（AI 复现了训练数据中的 GPL 代码——逐字或近似复制（" memorization"——LLM 的记忆效应）；2) **许可证污染**：AI 生成的代码包含 GPL 片段 → 项目被"传染"（GPL 的 copyleft 要求开源——MIT 项目引入 GPL 代码 = 许可证冲突）；3) **检测方式**：代码指纹匹配（AI 输出 vs 已知开源代码库的相似度——AST 级匹配 vs 文本级匹配；"特征片段"检测（特定函数名/注释模式/结构模式）。
- 合规策略：1) **生成后扫描**（AI 输出 → 许可证扫描（类似 RBL-807 资产审计的代码维度）——匹配已知 GPL 代码片段 → 标记/删除；2) **来源标记**：AI 生成 = 无版权（AI 生成的"原创"代码）vs AI 复现 = 原始许可证（GPL 代码的版权属于原作者）；3) **训练数据的合规**：选择"合规训练"的模型（使用 MIT/Apache 代码训练——避免 GPL 训练数据）。
- 追问钩子：为什么「AI 代码的版权问题」比「人复制代码」更难检测？——人复制代码 = 有明确的复制行为（git blame 显示来源——可追溯）；AI 复现 = 无明确来源（AI "记住"了训练数据但"生成"了代码——没有复制行为——但输出与训练数据几乎相同）；「AI 复现的检测」：不能靠 git blame（没有来源——只能靠代码相似度匹配）；且 LLM 的"创造性改写"（改变量名但逻辑相同）让文本匹配失效——AST 级匹配更有效但成本更高。

```typescript
// AI 代码的版权扫描
const GPL_PATTERNS = [
  { name: 'GPL-header', pattern: /GNU General Public License/i },
  { name: 'gpl-fingerprint', pattern: /this program is distributed in the hope/i },
  { name: 'fsf-address', pattern: /Free Software Foundation/i },
];
function scanCopyright(code: string) {
  const findings = [];
  for (const p of GPL_PATTERNS) {
    if (p.pattern.test(code))
      findings.push({ type: p.name, severity: 'error',
        detail: `疑似 GPL 许可证代码——需要审查来源` });
  }
  // AST 级相似度（简化：特征函数名匹配）
  const knownGPLFunctions = ['g_list_foreach', 'g_hash_table_iter'];
  for (const fn of knownGPLFunctions)
    if (code.includes(fn))
      findings.push({ type: 'gpl-function', severity: 'warn', detail: fn });
  return { findings, ok: !findings.some(f => f.severity === 'error') };
}
```
