---
title: [AIC-502] AI 代码生成的上下文窗口管理与裁剪
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-502：AI 上下文窗口管理与裁剪策略

**答**:
- 上下文窗口的约束：LLM 的 context window（4K~200K tokens）——大仓库的代码量远超窗口（10 万行代码 ≈ 50 万 tokens）——**裁剪策略**决定 AI 的代码质量（给它看什么 = 它知道什么 = 它生成的质量）。
- 裁剪的层次：1) **文件级**（当前文件 + 相关文件——import 闭包/同目录文件——Cursor 的 @file 引用）；2) **符号级**（函数签名/类型定义/接口——不需要实现体，只需要签名（API 面——RBL-946 推理链的 AI 版）；3) **语义级**（embedding 检索相关代码片段——RAG（语义相似度 > 物理位置）；4) **规则级**（系统提示——编码规范/架构约束（"用 TypeScript 严格模式""遵循 React hooks 规则"）。
- 裁剪的优先级：当前文件 > 直接依赖 > 类型签名 > 语义相关 > 编码规则——预算有限时按优先级裁剪。
- 追问钩子：为什么「符号级裁剪」比「文件级裁剪」更高效？——文件级 = 整个文件的内容（含无关函数——浪费 tokens）；符号级 = 只给签名和类型（API 面——100 行签名 = 10KB vs 1000 行实现 = 100KB——token 节省 90%）；AI 拿到签名可以"假设"实现（类型安全——编译器帮 AI 验证假设）；「签名即 API 契约」——AI 不需要知道实现细节（只需要接口——与人写代码的原则一致：面向接口编程）。

```typescript
// 上下文裁剪策略
interface ContextBudget { maxTokens: number; }
interface ContextItem { type: 'file'|'symbol'|'semantic'|'rule'; content: string; tokens: number; priority: number; }
function trimContext(items: ContextItem[], budget: ContextBudget): ContextItem[] {
  const sorted = items.sort((a, b) => a.priority - b.priority);   // 优先级排序
  const result: ContextItem[] = [];
  let used = 0;
  for (const item of sorted) {
    if (used + item.tokens > budget.maxTokens) continue;  // 超预算跳过（不截断单条）
    result.push(item); used += item.tokens;
  }
  return result;
}
// 符号级提取（TypeScript）
// 从文件中提取 export function/interface/type/class 的签名（不含 body）
function extractSignatures(source: string): string {
  return source.split('\n')
    .filter(line => /^(export\s+)?(async\s+)?(function|class|interface|type|const)\s/.test(line))
    .join('\n');                                         // 签名行
}
// 1000 行文件 → 10 行签名 = token 节省 99%
```
