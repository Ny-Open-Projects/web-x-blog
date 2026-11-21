---
title: [TS-041] Record 的典型用法有哪些？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-041：Record 的典型用法有哪些？
**答**：
- 用字面量联合做 key，快速生成"完备映射表"类型，漏 key 会报错。
- 配合对象常量做字典、枚举值映射、状态机表驱动。
- `Record<string, T>` 表示任意字符串 key 的字典（类似索引签名）。
- key 部分也可以是 keyof 某类型的引用，保持与源类型同步。

```typescript
type Role = "admin" | "editor" | "viewer";

// 完备映射：少写任何一个 key 都会编译报错
const roleLabels: Record<Role, string> = {
  admin: "管理员",
  editor: "编辑者",
  viewer: "访问者",
};

const permissions: Record<Role, boolean> = {
  admin: true,
  editor: true,
  viewer: false,
};

// 表驱动状态机
type State = "idle" | "loading" | "done";
const nextState: Record<State, State> = {
  idle: "loading",
  loading: "done",
  done: "idle",
};
```

## 第九章 keyof、typeof 与索引访问
