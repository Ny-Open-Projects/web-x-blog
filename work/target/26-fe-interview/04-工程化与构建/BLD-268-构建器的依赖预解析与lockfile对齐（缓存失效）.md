---
title: [BLD-268] 依赖预解析与 lockfile 对齐（缓存失效）怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-268：依赖对齐与缓存失效怎么做？
**答**：
- 对齐目标：构建时解析到的依赖版本 = lockfile 锁定版本 = 运行时加载版本——三者不一致（幽灵 hoisting/条件解析）是「本地好使 CI 挂」的根源（SCN-ENG-208）。
- lockfile 进缓存键：依赖版本变化 → 全部依赖相关缓存失效（SCN-ENG-287 buildDependencies）——粒度问题：lockfile 任一变更失效全部（粗但安全），优化是按依赖子树失效（细）。
- 漂移检测：构建时解析的版本快照 vs lockfile diff——不一致告警（pnpm frozen-lockfile 的构建层补充）。
- 追问钩子：为什么 lockfile 缓存键「粗粒度失效」先于「细粒度优化」——细粒度（按依赖子树失效）的收益是「无关依赖变更不失效」，但它要求精确的「子树→缓存条目」映射（任一边缘遗漏就是脏缓存）；先粗后细的路径：先保证正确性（粗），再在命中率数据（SCN-ENG-311）证明收益后渐进细化。

```javascript
// 构建时解析快照 vs lockfile
const resolved = snapshotResolvedDeps();               // 构建实际解析版本
const drift = diff(resolved, lockfileVersions());
if (drift.length) warn(`解析漂移: ${drift}`);           // 三方对齐检查
// 缓存键
buildDependencies: ['pnpm-lock.yaml']                  // 粗粒度（安全优先）
```
