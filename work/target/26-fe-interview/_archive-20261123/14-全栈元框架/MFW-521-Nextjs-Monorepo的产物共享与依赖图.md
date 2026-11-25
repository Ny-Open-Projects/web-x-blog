---
title: [MFW-521] Next.js Monorepo：产物共享、依赖图与构建编排
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-521：Next.js Monorepo：产物共享与依赖图

**答**:
- Next 在 monorepo 的三个协作点：1) **内部包双形态**（shared 包同时供 server（直接源码/ts）与 client（编译产物）消费——`exports` 条件 `"./x": { "types": ..., "import": ... }` RBL-602 + transpilePackages 让 Next 编译内部 ts 包）；2) **多 app 共享组件**（编译产物 vs 源码直引的失效面差异 RBL-701——monorepo 推荐 source 直引 + transpile，CI 才产物化）；3) 构建编排（turbo/nx 的 build 拓扑——next build 内部自己打包共享包，编排层只需声明输入）。
- Next 的产物黑盒：next build 产物不可外部增量（Next 自己的缓存管理）——编排器缓存「整个 build 任务」（turbo 任务级缓存 RBL-581），不试图增量 Next 内部。
- 追问钩子：为什么内部包推荐「source 直引 + transpilePackages」而不是「先构建再引用」？——source 直引 = Next 的编译器统一处理（tree shaking 跨包生效/HMR 生效/turbopack 可见）；产物引用 = 每次 shared 包变更要重建包再重建 app（两跳构建）且 HMR 失效——「编译边界后移」让打包器获得全局视图（跨包 shaking/缓存键统一）——这是 bundler 收敛内部包处理的架构理由。

```javascript
// shared 包的 package.json（双形态 exports）
{
  "name": "@org/ui",
  "exports": {
    ".": "./src/index.ts",                               // 源码直引（Next transpile）
    "./server": "./src/server.ts"
  }
}
// next.config: transpilePackages: ['@org/ui']           // 编译内部 ts
// 编排层只做任务级
// turbo.json: { "build": { "dependsOn": ["^build"], "outputs": [".next/**", "!.next/cache/**"] } }
// 注意排除 .next/cache（Next 自己管，跨任务缓存会脏）
```
