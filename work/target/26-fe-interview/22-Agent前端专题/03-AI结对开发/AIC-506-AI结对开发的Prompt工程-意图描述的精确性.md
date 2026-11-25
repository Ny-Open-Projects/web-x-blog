---
title: [AIC-506] AI 结对的 Prompt 工程：意图描述的精确性
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-506：AI Prompt 的意图精确性

**答**:
- AI Prompt 的意图精确性层级：1) **模糊**（"帮我写个分页"——AI 猜：offset 还是 cursor？多少 per page？前端还是后端？）；2) **约束**（"用 cursor-based 分页写一个 React hook"——技术栈/模式确定，但接口不确定）；3) **完整意图**（"写一个 useInfiniteScroll hook，用 IntersectionObserver 触发 fetchMore(cursor)，返回 { items, hasMore, loadMore }，TypeScript 严格类型"——技术栈+模式+接口+类型全确定）；4) 意图的精确性 = AI 产出质量的直接映射（精确 prompt → 一次通过；模糊 prompt → 3 轮迭代）。
- Prompt 的结构化模板：**Context + Constraint + Interface + Example**——Context（在什么场景）；Constraint（技术约束）；Interface（期望的输入/输出签名）；Example（类似实现的参考——"像 X 但做 Y"）。
- 追问钩子：为什么「给 AI 接口签名」比「给 AI 描述」更精确？——描述 = 自然语言（歧义不可避免——"返回 items 和 hasMore" 可以是对象/元组/回调）；接口签名 = TypeScript 类型（编译器级别的精确——`{ items: Item[], hasMore: boolean, loadMore: () => void }` 无歧义）；「类型的精确性 > 语言的精确性」：TypeScript 类型是"可验证的 prompt"——AI 生成的代码要么编译通过要么不通过（类型 = prompt 的验证器）。

```typescript
// Prompt 模板（结构化）
interface PromptTemplate {
  context: string;       // "React 18 + TypeScript 项目中的商品列表页"
  constraints: string[]; // ["用 IntersectionObserver", "不用第三方 infinite scroll 库"]
  interface: string;     // "useInfiniteScroll(fetchPage, initialCursor) → { items, hasMore, loadMore }"
  example?: string;      // "类似 useSWRInfinite 但不用 SWR"
}
// 从模糊到精确的迭代
const prompts = [
  { level: 1, text: "帮我写个分页",                    expectedIterations: 3 },
  { level: 2, text: "用 cursor-based 分页写 React hook", expectedIterations: 2 },
  { level: 3, text: `写 useInfiniteScroll hook：
    - IntersectionObserver 触发 fetchMore
    - 返回 { items: T[], hasMore: boolean, loadMore: () => void }
    - 泛型 <T> 支持任意数据类型
    - TypeScript strict 模式`,                           expectedIterations: 1 },
];
```
