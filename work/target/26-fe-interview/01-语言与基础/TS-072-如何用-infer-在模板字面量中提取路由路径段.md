---
title: [TS-072] 如何用 infer 在模板字面量中提取路由路径段？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-072：如何用 infer 在模板字面量中提取路由路径段？
**答**：
- 模板字面量模式 `` `${infer Seg}/${infer Rest}` `` 可同时捕获一个段和剩余字符串。
- 提取后递归处理 Rest，把每段收进联合类型。
- 与 TS-060 的区别：TS-060 提取 `:id` 形式的**动态参数对象**，这里提取**静态路径段**本身，常用于生成菜单、面包屑配置的 key。

```typescript
type PathSegments<S extends string> = S extends `/${infer Seg}/${infer Rest}`
  ? Seg | PathSegments<`/${Rest}`>
  : S extends `/${infer Seg}`
    ? Seg
    : never;

type Segs = PathSegments<"/user/profile/settings">;
// "user" | "profile" | "settings"

// 应用：按段生成配置 key 联合
type MenuKey = `menu-${PathSegments<"/user/profile/settings">}`;
// "menu-user" | "menu-profile" | "menu-settings"
```
