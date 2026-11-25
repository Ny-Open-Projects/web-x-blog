---
title: [BAS-149] 循环里 await 的串行和并行怎么写？差在哪？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-149：循环里 await 的串行和并行怎么写？差在哪？
**答**：
- `for...of` 里 await：每次等上一个请求完成才发下一个，串行，总耗时是各次之和。
- `map + Promise.all`：先把所有请求同时发出，再统一等待，总耗时约等于最慢的那一个。
- 注意并行版不会保持 for-await 那种逐个处理的节奏，若后一个依赖前一个结果只能串行。

```javascript
const urls = ['/a', '/b', '/c'];

// 串行：一个完成再发下一个，总耗时相加
for (const u of urls) await fetch(u);

// 并行：同时发起，总耗时约等于最慢的一个
await Promise.all(urls.map(u => fetch(u)));
```
