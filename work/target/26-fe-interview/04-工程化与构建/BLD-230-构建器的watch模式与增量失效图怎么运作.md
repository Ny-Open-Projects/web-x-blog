---
title: [BLD-230] 构建器的 watch 模式与增量失效图怎么运作？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-230：watch 模式怎么运作？
**答**：
- 失效图：文件变更 → 标记失效模块 → 沿「反向依赖边」传播（谁 import 了它）→ 重新转换失效闭包 → 增量 emit（SCN-ENG-266）。
- 失效传播的深度：改 utils.ts → 依赖它的所有模块重转换（不是重打包全部——产物级增量按 chunk 影响范围）。
- watch 陷阱：动态路径（glob import）、符号链接、外部文件（css @import url）未进监听 → 改动不触发（SCN-ENG-266 一致性）。
- 大仓 watch 的优化：只监听受影响包（filtered watch）+ 忽略规则（node_modules/.git）。
- 追问钩子：为什么「改动不触发更新」比「全量重建」更需要治理——全量重建慢但正确；漏监听导致开发者看到旧产物，开始不信任工具（重启/清缓存），DevEx 崩塌且掩盖真实 bug——失效图完整性（动态路径/外部依赖进监听）是 watch 模式的生命线。

```javascript
// 失效传播
fileChanged('utils.ts')
  → invalidate('utils.ts')
  → propagate(revDeps['utils.ts'])   // 反向依赖闭包全部失效
  → retransform(closure)
  → emit(chunksAffected)
// watch 监听范围
watchOptions: { ignored: /node_modules|\.git/,
  followSymlinks: true }                             // symlink 陷阱
```
