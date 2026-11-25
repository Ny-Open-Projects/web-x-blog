---
title: [RBL-225] 文件监听的原理与坑（chokidar 与 FSEvents）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-225：文件监听的原理与坑（chokidar 与 FSEvents）

**答**:
- 原理两层：OS 原生事件（macOS FSEvents/Linux inotify/Windows ReadDirectoryChangesW）vs 轮询兜底（网络盘/大目录降级）
- 坑一：inotify watch 上限（默认 8192）——大型 monorepo 需调 fs.inotify.max_user_watches；坑二：编辑器原子写（vim/swap）触发多重事件需防抖；坑三：rename 被拆成 delete+add
- chokidar 的封装价值：统一三平台差异 + awaitWriteFinish（防读到半截文件）
- 工程实践：监听范围最小化（只监听 src 与配置）、忽略目录（node_modules/dist/.git）——监听面是 watch 冷启动的关键

```javascript
chokidar.watch(['src/**/*', 'config/*.ts'], {
  ignore: ['**/node_modules/**', 'dist/**'],
  awaitWriteFinish: { stabilityThreshold: 100 },   // 防半截文件
  usePolling: process.env.CI === 'true',           // CI 网络盘兜底
})
```
