---
title: [TS-047] 如何用 infer 从模板字面量类型中提取内容？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-047：如何用 infer 从模板字面量类型中提取内容？
**答**：
- 模板字面量类型的模式匹配里可以嵌入 `infer P`，实现"字符串层面"的解析。
- 典型场景：从事件名提取前缀、从路由路径提取参数、从 getter 名提取字段名。
- 匹配失败走 false 分支，所以通常与递归结合处理多个片段。
- 这类技巧是 TypeScript 4.x 类型体操的核心玩法。

```typescript
// 提取 onXxx 事件名
type EventName<T extends string> = T extends `on${infer Rest}` ? Rest : never;
type A = EventName<"onChange">; // "Change"

// 提取去掉首尾引号的路径片段
type Split<S extends string> = S extends `${infer Head}/${infer Rest}`
  ? Head | Split<Rest>
  : S;
type Path = Split<"a/b/c">; // "a" | "b" | "c"

// 从 Vuex 风格 getter 名中提取模块名
type ModuleOf<T extends string> = T extends `${infer M}/${string}` ? M : never;
type B = ModuleOf<"user/getInfo">; // "user"
```
