---
title: [TS-054] strict 家族包含哪些选项？各自的作用是什么？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-054：strict 家族包含哪些选项？各自的作用是什么？
**答**：
- `strict: true` 一键开启全部严格检查，等价于下面所有选项。
- `noImplicitAny`：禁止隐式 any；`strictNullChecks`：null/undefined 独立成类型。
- `strictFunctionTypes`：函数参数默认逆变检查；`strictBindCallApply`/`strictPropertyInitialization` 补齐相关检查。
- `noUncheckedIndexedAccess`（4.1+，独立选项）：索引访问结果自动带 undefined，建议开启。

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "alwaysStrict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true
  }
}
```
