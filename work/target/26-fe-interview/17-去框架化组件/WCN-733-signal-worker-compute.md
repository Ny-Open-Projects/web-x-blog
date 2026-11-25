---
title: [WCN-733] 响应式计算下沉到 Web Worker 的通信与同步怎么设计？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-733：响应式计算下沉到 Web Worker 的通信与同步怎么设计？

**答**：
- 结论：把纯计算的 computed 图移到 Worker，主线程只保留 signal 的读写代理；输入变化通过 postMessage 传增量值，Worker 算完回传结果并写回主线程 signal。
- 注意结构化克隆开销——只传变化的数据而非全量状态；用 transferable（ArrayBuffer）传大数组；维护 requestId 处理异步乱序。
- 追问钩子：Worker 里的 computed 依赖了 DOM 相关值（如 window.innerWidth）怎么办？考察「把外部输入显式化为主线程 signal」

```javascript
// 主线程
const worker = new Worker('/compute.js');
const input = signal(0), output = signal(0);
let seq = 0;
input.subscribe?.(() => {});
worker.onmessage = (e) => {
  if (e.data.id === seq) output.value = e.data.result; // 只接受最新
};
function update(v) {
  input.value = v;
  worker.postMessage({ id: ++seq, value: v });
}
// Worker 内 (compute.js)
self.onmessage = (e) => {
  const result = heavyCompute(e.data.value);          // 纯计算
  self.postMessage({ id: e.data.id, result });
};
function heavyCompute(v) { return v * v; }
```
