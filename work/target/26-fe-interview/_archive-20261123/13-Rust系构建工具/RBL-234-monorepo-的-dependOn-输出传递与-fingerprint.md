---
title: [RBL-234] monorepo 里任务输出怎么传递与参与指纹
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-234：monorepo 里任务输出怎么传递与参与指纹

**答**:
- 输出传递：依赖包的 outputs（dist/**）作为下游任务的输入——指纹应包含「依赖包输出的 hash」而不是仅源码 hash（否则依赖变了下游缓存误命中）
- 工具实现差异：Turborepo 把依赖包的输出 hash 并入下游指纹（automatic）；Nx 的 named inputs 显式声明
- 常见 bug：outputs 声明不全（build 产物里还生成 .ts 构建信息文件没声明）→ 缓存恢复缺文件 → 下游构建失败
- 联合优化：outputs 最小化声明 + 依赖包「发布型输出」（dts）单独任务，让类型变更不影响运行产物的缓存命中

```json
{
  "tasks": {
    "build": { "dependsOn": ["^build"], "outputs": ["dist/**", "!dist/**/*.map"] },
    "build-types": { "outputs": ["dist/index.d.ts"] }
  }
}
```
