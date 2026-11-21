---
title: [TS-050] 如何用模板字面量 + 映射类型批量生成 getter 类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-050：如何用模板字面量 + 映射类型批量生成 getter 类型？
**答**：
- 映射类型里用 as 对 key 重映射，配合模板字面量把 `name` 变成 `getName`。
- `Capitalize<K>` 首字母大写，`string & K` 用于把 key 收窄成 string 以便插入模板。
- 这是"根据数据结构自动派生 API 类型"的典型手法，vuex 的 mapGetters、表单校验器常用。
- 也可以反向做：从 `getXxx` 解析回字段名。

```typescript
interface Person {
  name: string;
  age: number;
}

type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

type PersonGetters = Getters<Person>;
// { getName: () => string; getAge: () => number }

// 更实用的例子：为每个字段生成校验规则 key
type Validators<T> = {
  [K in keyof T as `validate_${string & K}`]: (value: T[K]) => boolean;
};
// { validate_name: (v: string) => boolean; validate_age: (v: number) => boolean }
```

## 第十二章 映射类型
