---
title: [TS-130] TS 编译慢如何优化？项目级手段有哪些？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-130：TS 编译慢如何优化？项目级手段有哪些？
**答**：
- 工程结构：`project references` 把 monorepo 拆成子项目，增量只编译改动包；`incremental: true` 持久化编译缓存。
- 编译范围：`skipLibCheck: true` 跳过第三方 d.ts 检查（收益最大且基本无副作用）；`isolatedModules: true` 保证单文件可转译，配合 babel/esbuild/swc 快速构建。
- 代码层面：类型体操控制递归深度（见 TS-082、TS-111）；公共巨型工具类型拆文件按需引用；避免在热路径声明超大联合（如上千个字面量）。
- 监控：`tsc --extendedDiagnostics`、`--generateTrace` 定位热点类型。

```json
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": ".cache/tsbuildinfo",
    "skipLibCheck": true,
    "isolatedModules": true,
    "target": "ES2020",
    "moduleResolution": "bundler"
  },
  "references": [
    { "path": "./packages/shared" },
    { "path": "./packages/ui" },
    { "path": "./packages/app", "references": [{ "path": "./packages/shared" }, { "path": "./packages/ui" }] }
  ],
  "files": []
}
```

```typescript
// 常用诊断命令
// npx tsc --noEmit --extendedDiagnostics
// 输出关注：Types / Instantiations / Check time
// npx tsc --noEmit --generateTrace trace
// 用 Chrome tracing 打开 trace 下的 trace.json，定位最耗时的类型实例化

// 拆分参考：把上百个字面量的大联合改为命名空间分片
type RouteA = "/a1" | "/a2"; // 拆前：Route = "/a1" | ... | "/a999" 导致实例化爆炸
type RouteB = "/b1" | "/b2";
type AllRoutes = RouteA | RouteB; // 按需引用分片，而不是全量并入热路径类型
```

## 第二十九章 Vue3 中的 TS 深入（TS-131 ~ TS-136）
