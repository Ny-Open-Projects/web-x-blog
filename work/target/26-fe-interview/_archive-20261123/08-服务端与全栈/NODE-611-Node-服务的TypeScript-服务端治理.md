---
title: [NODE-611] Node 服务的 TypeScript 治理（严格度/类型边界/生成）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-611：服务端 TS 治理
**答**:
- 严格度策略：strict 全开（服务端新代码）、存量渐进（allowJs 过渡/逐步 strict 化——ARC-464 any 治理）、构建分离（tsconfig：dev 与 build 严格度一致——防"dev 过 build 不过"）。
- 类型边界：入口校验（请求 schema → 类型——zod parse 是类型入口 NODE-411）、DB 层类型（ORM 类型（Prisma 生成）——查询返回类型可信）、对外导出（API 契约类型单源生成 NODE-528——不手写接口类型）。
- 运行时与编译期鸿沟：TS 类型不校验运行时（信任边界：外部输入必须 parse——类型断言 as 是谎言）、enum 与 union 策略（const 对象 + type 推导——运行时可用）、unknown 优于 any（外部数据一律 unknown——校验后收窄）。
- 构建工具链：tsc --noEmit 校验 + esbuild/swc 转译（类型检查与转译分离——CI 跑 tsc 一次全量）、增量构建（项目引用/缓存——大型 monorepo 构建提速 NODE-514）、sourceMap 生产保留（堆栈还原——不进产物公网 ARC-422）。
- 治理指标：类型覆盖率（any/断言数量趋势）、编译错误逃逸（运行时类型相关事故）。
```json
// tsconfig.build.json（服务端）
{ "compilerOptions": { "strict": true, "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true, "exactOptionalPropertyTypes": true },
  "exclude": ["src/generated"] }   // 生成物单独治理
```
