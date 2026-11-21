---
title: [NODE-204] Node 22 的 --experimental-strip-types 与 TS 运行策略？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-204：Node 22 的 --experimental-strip-types 与 TS 运行策略？
**答**：
- strip-types：22.6+ 直接运行 TS——只做"类型擦除"（去掉类型注解），不做类型检查，不支持 enum/namespace/参数属性等需要代码转换的语法（要用 --experimental-transform-types）。
- 工具链定位：本地脚本/小工具直跑最省事；正式服务仍建议 tsc/tsup 预构建（类型检查在 CI 做，产物确定性更强）。
- 边界：.ts 后缀在 import 里要显式写（Node 22.7 之前）；type 字段 package.json 影响解析。
- 生产建议：strip-types 适合 CLI/脚本/实验，服务端构建产物 + sourcemap 仍是首选（NODE-153 构建链选型延续）。

```typescript
// scripts/migrate.ts —— node --experimental-strip-types scripts/migrate.ts 直跑
import { createClient } from './lib/client.ts';   // .ts 后缀显式
interface Row { id: number; name: string }         // 类型注解：擦除
const rows: Row[] = await fetchRows();             // 顶层 await OK（作为 ESM 入口）
for (const { id } of rows) console.log(id);
// 不支持的写法（需要 transform）：
// enum Mode { A, B }                              // enum → 用 union type + const object
// const Mode = { A: 0, B: 1 } as const; type Mode = typeof Mode[keyof typeof Mode];  // 替代
```
