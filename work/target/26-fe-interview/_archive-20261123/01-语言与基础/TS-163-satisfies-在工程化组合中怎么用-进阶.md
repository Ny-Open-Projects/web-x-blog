---
title: [TS-163] satisfies 在工程化组合中怎么用？（进阶）
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-163：satisfies 在工程化组合中怎么用？（进阶）
**答**：
- TS-021 讲过基本语义；进阶在于三种写法的选型：type 标注（丢字面量）、as const（丢校验）、satisfies（两者兼得）。
- 标准姿势：`satisfies 校验形状` + `keyof typeof 推导键联合`，配置即类型的单一来源。
- 键集需要严格封死时，satisfies 放不拦"多余键"，改用显式标注。

```typescript
// satisfies：校验 + 保留字面量推断
const routes = {
  home: { path: "/", auth: false },
  user: { path: "/user/:id", auth: true },
} satisfies Record<string, { path: string; auth: boolean }>;

routes.user.path;                      // 字面量类型 "/user/:id"（type 标注会退化为 string）
type RouteName = keyof typeof routes;  // "home" | "user"（as const 写法没有形状校验）

// 与 as 断言对比：as 不校验字段，写错字段也放行
const typed = {
  user: { path: "/u", auth: "yes" },   // 换成 satisfies 会在这里报错
} as Record<string, { path: string; auth: boolean }>;

// 组合技：路由注册表 + 派生类型（与 TS-171 呼应）
type RoutePath = (typeof routes)[RouteName]["path"]; // "/" | "/user/:id"
```

## 第三十四章 模块与声明进阶（TS-164 ~ TS-169）
