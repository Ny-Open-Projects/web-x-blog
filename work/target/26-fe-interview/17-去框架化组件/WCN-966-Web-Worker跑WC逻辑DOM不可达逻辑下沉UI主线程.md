---
title: [WCN-966] Web Worker 里跑 WC 逻辑：DOM 不可达时怎么做到逻辑下沉、UI 留主线程
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-966：Web Worker 里跑 WC 逻辑：DOM 不可达时怎么做到逻辑下沉、UI 留主线程

**答**：
- 结论先行：Worker 没有 DOM，不能渲染 WC，但可以把「纯逻辑」（状态计算、格式化、 diff、排序过滤）下沉到 Worker，主线程只保留 DOM 操作与事件转发。
- 架构：主线程把「意图」（如 setFilter、sortBy）postMessage 给 Worker，Worker 算出「差异指令」或新快照回传，主线程据此做最小 DOM patch。
- 适用：计算密集型（大表格排序、富文本 diff、图表聚合）才值得下沉——通信开销可能超过收益，简单逻辑别进 Worker。
- 坑：Worker 不共享 DOM 事件与 signal，状态要显式序列化；用 SharedArrayBuffer + Atomics 可做低延迟共享但需 COOP/COEP 头。
- 追问钩子：面试官问「OffscreenCanvas 算不算 WC 在 Worker 渲染」——答：那是 canvas 在 Worker 绘制，属于特例（图表/游戏），通用 DOM 组件无法在 Worker 渲染，别混淆。

```javascript
// 主线程：转发意图 + 应用回传的最小 patch
const worker = new Worker('./logic.js');
worker.onmessage = e => {
  const { op, payload } = e.data;
  if (op === 'patch') payload.forEach(([sel, text]) =>
    document.querySelector(sel).textContent = text);
};
// 用户操作 -> 下发意图
document.querySelector('#sort').addEventListener('click', () =>
  worker.postMessage({ intent: 'sort', by: 'price' }));
// logic.js（Worker）：
// onmessage = e => {
//   if (e.data.intent === 'sort') {
//     const rows = sort(data, e.data.by);
//     postMessage({ op:'patch', payload: rows.map((r,i)=>[`#row${i}`, r.name]) });
//   }
// };
```
