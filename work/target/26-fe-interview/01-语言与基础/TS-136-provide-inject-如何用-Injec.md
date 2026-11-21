---
title: [TS-136] provide/inject 如何用 InjectionKey 做到类型安全？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-136：provide/inject 如何用 InjectionKey 做到类型安全？
**答**：
- key 用 `InjectionKey<T>` 类型的 Symbol：provide 端值类型被约束为 T，inject 端返回类型自动为 `T | undefined`。
- inject 带默认值时去掉 undefined，杜绝 `as Theme` 式手写断言导致 key 与类型脱节。
- key 导出在独立文件中作为"注入契约"，跨团队协作时即文档。

```typescript
import { inject, provide, InjectionKey } from "vue";

// theme-key.ts —— 注入契约
export const ThemeKey: InjectionKey<{
  color: string;
  toggle: () => void;
}> = Symbol("theme");

// 祖先组件：值类型必须严格匹配，多字段少字段都报错
provide(ThemeKey, { color: "dark", toggle: () => {} });

// 后代组件：类型自动推导，无需断言
const theme = inject(ThemeKey);                              // 类型 | undefined
const theme2 = inject(ThemeKey, { color: "light", toggle: () => {} }); // 非 undefined

// 反例：inject<Theme>("theme") 手写泛型断言，key 改名/类型改动编译器无法追踪
```

## 第三十章 React 中的 TS 深入（TS-137 ~ TS-142）
