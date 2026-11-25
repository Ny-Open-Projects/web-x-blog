---
title: [RBL-547] 文件 watcher 的事件合并与忽略规则：变更流的正确性
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-547：文件 watcher 的事件合并与忽略规则：变更流的正确性

**答**：
- watcher（文件监听）的三个正确性要点：
- 1) **事件合并**：编辑器保存会产生多个事件（rename+change 或多次 change）——防抖窗口（如 100ms）合并同一文件的连续事件；**跨文件合并**（一次保存动到多个文件：git checkout）→ 批量触发一次增量编译（而非 N 次）。
- 2) **忽略规则**：node_modules/.git/产物目录的变更要忽略——忽略规则与「依赖图是否包含」一致（产物目录在依赖图外）——**watcher 忽略了但依赖图包含**（或反之）是「该重建没重建」的幽灵 bug。
- 3) **事件语义归一**：不同平台的 watcher 事件差异（macOS FSEvent 的目录级事件 vs inotify 文件级）——归一为 add/change/unlink 三语义 + 目录事件的展开。
- watcher 的性能陷阱：大仓（10 万文件）的全量 watch 成本——分而治之：只 watch 依赖图内的文件 + 原生递归 watch 目录（比逐文件 watch 高效）。
- 追问钩子：watcher 丢失事件的兜底——FSEvent/inotify 偶发丢事件（内核缓冲溢出）——定期全量校验（mtime 扫描 diff，低频后台）作为安全网——「事件驱动 + 周期对账」双保险。

```javascript
// watcher 正确性三要点
const WATCHER = {
  事件合并: {
    同文件: '防抖 100ms 合并（rename+change 连发）',
    跨文件: 'git checkout 多文件 → 批量一次增量编译（非 N 次）',
  },
  忽略规则: 'node_modules/.git/产物目录忽略——忽略集合与依赖图必须一致（否则幽灵 bug：该重建没重建）',
  语义归一: 'FSEvent 目录级 vs inotify 文件级 → add/change/unlink 三语义归一',
  性能: '大仓只 watch 依赖图内文件 + 原生递归目录 watch（非逐文件）',
  丢事件兜底: '低频 mtime 全量扫描 diff 对账——「事件驱动+周期对账」双保险',
}
```
