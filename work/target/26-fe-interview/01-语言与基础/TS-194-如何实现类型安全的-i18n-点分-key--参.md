---
title: [TS-194] 如何实现类型安全的 i18n（点分 key + 参数插值）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-194：如何实现类型安全的 i18n（点分 key + 参数插值）？
**答**：
- key 层：语言包 as const 后递归生成点分路径联合（`nav.home` | `greet`）。
- 参数层：从翻译模板字符串提取 `{name}` 占位符，t 函数第二参约束为参数记录。
- 缺参数、错 key、错参数名全部编译期报错，语言包改动时调用点自动报错。

```typescript
const zhCN = {
  nav: { home: "首页", about: "关于" },
  greet: "你好，{name}！今天 {count} 条消息",
} as const;

// 递归生成点分 key 联合
type DotPaths<T, P extends string = ""> = T extends string
  ? P
  : { [K in keyof T & string]: DotPaths<T[K], `${P}${P extends "" ? "" : "."}${K}`> }[keyof T & string];
type MessageKey = DotPaths<typeof zhCN>; // "nav.home" | "nav.about" | "greet"

// 按点路径取模板字符串
type PathValue<T, P extends string> =
  P extends `${infer H}.${infer R}` ? (H extends keyof T ? PathValue<T[H], R> : never)
  : P extends keyof T ? T[P] : never;

// 提取 {param} 占位符
type ExtractParams<S extends string> =
  S extends `${string}{${infer P}}${infer Rest}` ? P | ExtractParams<Rest> : never;

type MessageParams<K extends MessageKey> = ExtractParams<PathValue<typeof zhCN, K>>;

declare function t<K extends MessageKey>(
  key: K,
  ...args: MessageParams<K> extends never ? [] : [params: Record<MessageParams<K>, string | number>]
): string;

t("nav.home");
t("greet", { name: "张三", count: 3 });
// t("greet");                 // 报错：缺 params
// t("greet", { name: "a" });  // 报错：缺 count
// t("nav.hom");               // 报错：key 不存在
```
