---
title: [JS-170] Web Worker 消息协议如何封装？怎么做到类型安全与 Promise 化？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-170：Web Worker 消息协议如何封装？怎么做到类型安全与 Promise 化？

**答**：
- 原生 postMessage 是裸的回调，多任务并发时无法区分回复归属——协议里带自增 id，主线程用 Map<id, {resolve,reject}> 配对。
- 消息信封：请求 `{ id, type, payload }`，响应 `{ id, ok, data | error }`，worker 端按 type 分发到 handlers 表。
- Promise 化后 `await api.call('sort', arr)`，与普通异步函数无异；传大数组用 transfer 列表零拷贝转移。
- terminate 时要 reject 所有 pending 的 Promise，避免调用方永远挂起。
- TS 下给 call 泛型化 `call<K extends keyof Handlers>(type: K, payload: Parameters<Handlers[K]>[0])` 即得完整类型安全。

```javascript
// ---------- worker.js ----------
self.onmessage = ({ data: { id, type, payload } }) => {
  const handlers = {
    sum: (nums) => nums.reduce((a, b) => a + b, 0),
    sort: (nums) => [...nums].sort((a, b) => a - b),
  };
  try {
    if (!handlers[type]) throw new Error(`未知指令 ${type}`);
    self.postMessage({ id, ok: true, data: handlers[type](payload) });
  } catch (e) {
    self.postMessage({ id, ok: false, error: e.message });
  }
};

// ---------- 主线程：Promise 化客户端 ----------
function createWorkerClient(makeWorker) {
  const worker = makeWorker();
  const pending = new Map();               // id -> { resolve, reject }
  let seq = 0;
  worker.onmessage = ({ data: { id, ok, data, error } }) => {
    const p = pending.get(id);
    if (!p) return;
    pending.delete(id);                    // 一次性：处理完即删
    ok ? p.resolve(data) : p.reject(new Error(error));
  };
  return {
    call(type, payload, transfer = []) {
      const id = ++seq;
      return new Promise((resolve, reject) => {
        pending.set(id, { resolve, reject });
        worker.postMessage({ id, type, payload }, transfer);
      });
    },
    terminate() {                          // 终止时清空所有等待者
      worker.terminate();
      pending.forEach((p) => p.reject(new Error('worker 已终止')));
      pending.clear();
    },
  };
}

// 用法：百万级数组计算不阻塞主线程
const workerCode = document.currentScript?.textContent; // 生产环境用独立 worker.js
const api = createWorkerClient(() => new Worker('worker.js'));
const big = Array.from({ length: 1e6 }, (_, i) => 1e6 - i);
api.call('sort', big).then((sorted) => console.log('最小值：', sorted[0]));
// 大数组可用 transfer 零拷贝：api.call('sort', big, [big.buffer])
```
