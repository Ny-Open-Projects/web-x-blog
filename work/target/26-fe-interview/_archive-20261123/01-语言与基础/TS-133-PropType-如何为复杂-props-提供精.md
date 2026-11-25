---
title: [TS-133] PropType 如何为复杂 props 提供精确类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-133：PropType 如何为复杂 props 提供精确类型？
**答**：
- 运行时声明中 Object/Array/Function 默认推断为宽类型，用 `Object as PropType<User>` 精确标注。
- 字面量联合 prop 用 `String as PropType<"a" | "b">`，编辑器自动补全可选值。
- 数组默认值必须用工厂函数 `default: () => []`，与类型无关但高频踩坑。

```typescript
import type { PropType } from "vue";

interface User { id: number; tags: string[] }

// 在 <script setup> 或选项式组件的 props 中：
defineProps({
  user: { type: Object as PropType<User>, required: true },
  tags: { type: Array as PropType<string[]>, default: () => [] },
  onChange: { type: Function as PropType<(id: number) => void>, required: true },
  shape: { type: String as PropType<"a" | "b">, default: "a" },
});

// 坑：不用 PropType 时 props.user 推断为 Record<string, any>，
// props.user.tags 是 any —— 类型检查整条链路失效
```
