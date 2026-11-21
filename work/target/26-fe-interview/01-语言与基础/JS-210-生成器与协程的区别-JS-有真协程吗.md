---
title: [JS-210] 生成器与协程的区别：JS 有真协程吗
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 生成器]
type: 面试题
---

## JS-210：生成器与协程的区别：JS 有真协程吗

**答**：
- 协程（coroutine）：可双向跳转的控制流——任意协程可 yield 到任意协程；生成器是「半协程」：只能 yield 回调用者
- JS 现状：没有原生对称协程；生成器 + 驱动器（co）模拟了「调用方与生成器交替执行」，但控制权始终在驱动器手里
- 亲缘对比：Go 的 goroutine、Python 的 asyncio.coroutine、Lua 的 coroutine.yield 是真协程/对称协程体系
- 实用结论：面试答「JS 有半协程（生成器），await 语义即建立在它之上」即可
- 延伸：structured concurrency 提案与 Effect 式框架在 JS 社区探索协程式控制流

```javascript
// 半协程：生成器只能把控制权交回「直接调用者」
function* inner() { yield 'inner'; }
function* outer() { yield* inner(); } // 控制权经 outer 中转
const g = outer();
g.next(); // { value: 'inner' } —— 值穿透，但栈帧仍是 outer↔调用者
```
