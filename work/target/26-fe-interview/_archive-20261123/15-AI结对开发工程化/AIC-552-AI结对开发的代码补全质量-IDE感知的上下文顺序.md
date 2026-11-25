---
title: [AIC-552] IDE 感知的上下文顺序
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-552：IDE 感知的上下文顺序

**答**:
- AI 补全的上下文顺序影响生成质量：1) **光标位置最近的代码影响最大**（LLM 的注意力权重：光标前 500 字符的权重 >> 文件开头的代码——"就近原则"；2) **IDE 的上下文排序策略**：光标前代码 → 光标后代码 → import 声明 → 同文件其他函数 → 相关文件签名（按"距离"排序 RBL-544 的优先级扩展——距离 = 物理距离 + 语义距离）；3) **上下文的"前重后轻"**：光标前的代码比光标后的更重要（AI 的生成方向 = 从上到下——前面的上下文是"已知的"，后面是"待确定的"）。
- 追问钩子：为什么「光标前 500 字符的权重 >> 文件开头」？——LLM 的自回归生成：下一个 token 基于前文预测——前文 = 上下文（越近 = 越相关 = 注意力权重越高——attention 的 locality bias）；文件开头的 import 声明虽然重要但与光标处的生成目标"距离远"（注意力权重衰减）；「上下文的"距离"」= token 距离（不是语义距离——语义由 RBL-502 的 embedding 检索补充）——IDE 的上下文排序应该把"光标前最近的代码"放在最前（LLM 注意力的甜蜜点）。

```typescript
// IDE 上下文的排序策略
function orderContext(file: { before: string; after: string; imports: string[] },
  related: { content: string; priority: number }[]) {
  return [
    { type: 'cursor-before', content: file.before.slice(-500), weight: 10 },  // 光标前 500
    { type: 'cursor-after', content: file.after.slice(0, 200), weight: 5 },   // 光标后 200
    { type: 'imports', content: file.imports.join('\n'), weight: 3 },
    ...related.map(r => ({ type: 'related', content: r.content, weight: r.priority })),
  ].sort((a, b) => b.weight - a.weight);               // 权重降序
}
// 光标前 500 字符 >> 光标后 200 字符 >> import >> 相关文件
// LLM 的 attention locality bias：近处 > 远处
```
