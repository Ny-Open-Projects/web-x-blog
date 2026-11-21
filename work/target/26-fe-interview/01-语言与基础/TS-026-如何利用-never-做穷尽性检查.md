---
title: [TS-026] 如何利用 never 做穷尽性检查？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-026：如何利用 never 做穷尽性检查？
**答**：
- switch 处理完联合类型所有成员后，default 分支里值类型是 never。
- 把它赋给一个显式 `never` 类型的变量，将来新增成员而忘记处理时，这里会编译报错。
- 相比"不写 default 依赖返回类型检查"，这种写法能精确定位漏分支位置。
- 通常封装成 assertNever 工具函数复用。

```typescript
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "square"; size: number }
  | { kind: "rect"; width: number; height: number };

function area(s: Shape): number {
  switch (s.kind) {
    case "circle":
      return Math.PI * s.radius ** 2;
    case "square":
      return s.size ** 2;
    case "rect":
      return s.width * s.height;
    default: {
      const _exhaustive: never = s; // 若新增 kind 而漏写 case，这里编译报错
      return _exhaustive;
    }
  }
}
```

## 第六章 可辨识联合
