---
title: [MFM-438→MFW-438] 笔试：手写 SSR 渲染对象池与请求上下文清理
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-438：MFM→438：渲染池清理
**答**：实现 `pooledRender(fn, { poolSize = 8 } = {})`：1) 池化目标：贵重初始化（模板编译/序列化器/样式引擎实例）——创建一次复用 N 请求；2) 出借即隔离：请求上下文（ALS store/临时 Map）必须 per-checkout 新建——禁止池化对象携带上请求残渣（串数据最高危）；3) 归还审计：checkIn 时脏检查（对象上出现非白名单新键 → 告警+丢弃该实例不回池——防污染扩散）；4) 崩溃隔离：渲染抛错 → 该实例销毁重建（React 流中断后内部状态不可信）；5) 指标 { waitMs(池等待——扩容信号), reuseRate, discardCount }。

```javascript
export function createRenderPool(make, reset, { size = 8 } = {}) {
  const idle = [], waiters = []
  let made = 0, discarded = 0
  return {
    async checkout() {
      let inst = idle.pop()
      if (!inst) { if (made < size) { inst = make(); made++ } else return await enqueue() }
      const ctx = freshRequestScope()                        // 上下文必新建——残渣防线
      return { inst, ctx, done: () => checkIn(inst, ctx) }
    },
    function checkIn(inst, ctx) {
      const dirt = detectForeignKeys(inst, ctx)              // 白名单外新键？
      if (dirt.length || ctx.aborted) { made--; discardCount++; replacements.push(make()) }  // 丢弃重建
      else idle.push(inst)
      drainWaiters()
    },
  }
}
```
**评分点**：
- 上下文 per-checkout 新建（池化最大风险=串数据——结构性预防）
- 脏检查丢弃（污染实例不回池扩散——而非默默清洗）
- 崩溃销毁重建（流中断状态不可信）
- waitMs 池等待指标（扩容信号——池太小用户在排队）
