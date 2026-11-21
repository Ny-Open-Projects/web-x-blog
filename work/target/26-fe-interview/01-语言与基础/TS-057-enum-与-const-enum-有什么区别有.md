---
title: [TS-057] enum 与 const enum 有什么区别？有哪些坑？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-057：enum 与 const enum 有什么区别？有哪些坑？
**答**：
- 普通 enum 编译后生成真实的双向映射对象（数字枚举支持反向索引），有运行时代价。
- const enum 编译时内联，无运行时对象；但 `isolatedModules: true` 下限制较多（不能被单独导出后直接取值，4.x 起需 preserveConstEnums 配合）。
- 数字枚举反向映射的坑：`Color[3]` 也能取到值，key 空间被污染。
- 社区推荐用 `as const` 对象 + `keyof typeof` 替代 enum，零运行时且类型友好。

```typescript
enum Color {
  Red = 1,
  Green,
  Blue,
}
// 编译产物：var Color; Color[Color["Red"] = 1] = "Red"; ...（双向映射）
console.log(Color[1]); // "Red"（反向映射）

const enum FastColor {
  Red = 1,
  Green,
  Blue,
}
const fast: FastColor = FastColor.Green; // 编译后内联为 2，无 FastColor 对象

// as const 替代方案
const Status = {
  Idle: "idle",
  Loading: "loading",
  Done: "done",
} as const;
type Status = (typeof Status)[keyof typeof Status]; // "idle" | "loading" | "done"
```

## 第十七章 协变与逆变
