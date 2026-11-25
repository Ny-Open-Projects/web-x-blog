---
title: [WCN-541] Signals 与 Web Worker：把纯计算信号图放到 Worker，主线程只保留视图信号的架构边界在哪里？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-541：Signals 与 Web Worker：把纯计算信号图放到 Worker，主线程只保留视图信号的架构边界在哪里？

**答**：
- 结论：边界是「计算图 vs 视图图」——纯派生/重计算放 Worker，DOM 相关信号（hover/scroll）留主线程。
- 主线程写原始信号 → 批量 postMessage 到 Worker；Worker 算出派生值 → 回传更新视图信号。
- 消息用版本号丢弃过期结果，避免竞态；可用 SharedArrayBuffer 减少拷贝（需 COOP/COEP）。
- 追问：Worker 里没有 DOM，computed 依赖的 time/random 如何处理？（答：由主线程注入时间戳作为信号）

```javascript
// main
const input = signal(0), view = signal(0); let ver = 0;
input.subscribe(v => worker.postMessage({ type: 'set', v, ver: ++ver }));
worker.onmessage = ({ data }) => { if (data.ver >= ver) view.set(data.result); };
// worker
let graph = createGraph();
onmessage = ({ data }) => {
  if (data.type === 'set') { graph.set(data.v); postMessage({ result: graph.compute(), ver: data.ver }); }
};
```
