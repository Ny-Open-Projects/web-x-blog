---
title: [TS-177] 映射键重映射 as 子句有哪些进阶玩法？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-177：映射键重映射 as 子句有哪些进阶玩法？
**答**：
- 过滤键：as 里映射为 never 即删除该键（`_` 开头的内部字段）。
- 重命名键：模板字面量生成 getter/setter 风格的键。
- 组合：as 表达式里可以同时做"键级条件 + 键级转换"，值类型照常取 T[K]。

```typescript
interface RawConfig {
  id: string;
  _internal: symbol;
  maxRetry: number;
}

// 1) 过滤：剔除下划线开头的内部字段
type PublicOnly<T> = { [K in keyof T as K extends `_${string}` ? never : K]: T[K] };
type P = PublicOnly<RawConfig>; // { id: string; maxRetry: number }

// 2) 重命名：getter 键生成
type Getters<T> = { [K in keyof T as `get${Capitalize<K & string>}`]: () => T[K] };
type G = Getters<P>; // { getId: () => string; getMaxRetry: () => number }

// 3) 组合：as 里同时过滤 + 转换
type PublicGetters<T> = {
  [K in keyof T as K extends `_${string}` ? never : `get${Capitalize<K & string>}`]: () => T[K];
};
type PG = PublicGetters<RawConfig>; // { getId: () => string; getMaxRetry: () => number }
```
