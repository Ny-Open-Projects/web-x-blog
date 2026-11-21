---
title: [WCN-243] batch() 的事务语义：内部多次写如何只触发一次下游？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-243：batch() 的事务语义：内部多次写如何只触发一次下游？
**答**：
- batch 把 flush 推迟到 batch 结束（嵌套 batch 计数器，最外层才 flush）。
- 语义上等价于一个事务：中间态不可见，effect 看到的永远是「某个完整写入序列后」的值。
- 自动 batch：事件处理器内的多次写自动合并（各实现默认行为差异要注意）。
- async 陷阱：batch 内 await 后再写不会被打包（同步边界）——需要显式再包一层。

```javascript
let batchDepth = 0;
export function batch(fn) {
  batchDepth++;
  try { return fn(); }
  finally { if (--batchDepth === 0) flushNow(); }   // 只在最外层 flush
}
// 陷阱：batch(async () => { set(a,1); await x; set(b,2); }) → b 的写不在事务内
r
```
