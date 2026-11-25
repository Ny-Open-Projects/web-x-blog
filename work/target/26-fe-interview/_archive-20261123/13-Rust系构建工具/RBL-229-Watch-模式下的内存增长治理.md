---
title: [RBL-229] Watch 模式长时间运行的内存增长怎么治理
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-229：Watch 模式长时间运行的内存增长怎么治理

**答**:
- 增长来源：模块图累积（被删除文件未清理）、sourcemap 缓存（每次增量新 map 未释放）、插件闭包持有（tap 里引用大对象）、缓存条目无上限
- 治理：watch 模式下「删除模块的图清理」（工具侧）、map 缓存 LRU、插件审计（禁在钩子里累积全局 state）、缓存上限
- 检测：watch 进程长跑 + 定期 heap snapshot diff（1h vs 起点），增长曲线分类（锯齿=正常 GC / 单调=泄漏）
- 兜底策略：watch 进程定期自愈重启（如每 4h 或内存超阈值），开发者无感（重启窗口 <3s 时可接受）

```javascript
// 自愈守护（外层脚本）
setInterval(() => {
  const mem = process.memoryUsage().heapUsed
  if (mem > 4 * 1024 ** 3) { log('watch restart: mem'); process.exit(1) }   // 守护进程拉起
}, 5 * 60_000)
```
