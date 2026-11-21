---
title: [OPT-101] Comlink 的核心思想是什么？怎么用 RPC 化封装 Worker？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-101：Comlink 的核心思想是什么？怎么用 RPC 化封装 Worker？

**答**：
- Comlib/Comlink 思想：把 Worker 的 postMessage 协议抽象成 **ES Proxy + RPC**——Worker 暴露一个对象，主线程拿到"看起来同款"的代理，方法调用自动变成异步消息，业务代码不见一行 postMessage。
- 收益：通信协议（id 匹配、序列化、错误回传）全部收敛到库里，Worker 接口像本地模块一样用，团队不再各写各的消息格式。
- 核心约定：代理上的每个方法调用返回 Promise；参数与返回值仍走结构化克隆，**大 ArrayBuffer 记得用 transfer 包装**；回调通过 Comlink.proxy 反向暴露。
- 手写 20 行也能实现同样思想（理解原理 > 记 API）。

```javascript
// 一一对应：Comlink 用法 + 手写 mini 版（理解 RPC 化本质）
// 方式一：Comlink 现成库
// import * as Comlink from 'comlink';
// worker.js
// import * as Comlink from 'comlink';
// const api = {
//   async parseHugeJson(url) {
//     const res = await fetch(url);
//     return (await res.json()).items.slice(0, 100); // 只回小结果
//   },
//   process(buf) {
//     const arr = new Float32Array(buf);
//     arr.forEach((v, i, a) => (a[i] = v * 2));
//     return Comlink.transfer(arr.buffer, [arr.buffer]); // 显式声明转移
//   },
// };
// Comlink.expose(api);
// main.js
// const api = Comlink.wrap(new Worker('worker.js'));
// const items = await api.parseHugeJson('/data.json'); // 像本地异步函数一样调

// 方式二：手写 20 行 mini RPC（同一思想）
// worker.js
self.onmessage = async (e) => {
  const { id, method, args } = e.data;
  try {
    const result = await methods[method](...args);
    self.postMessage({ id, ok: true, result });
  } catch (err) {
    self.postMessage({ id, ok: false, error: err.message });
  }
};
const methods = {
  hash(text) { return [...text].reduce((h, c) => (h * 31 + c.charCodeAt(0)) | 0, 0); },
  sortBig(arr) { return arr.slice().sort((a, b) => a - b); },
};

// main.js —— Proxy 把方法调用转成消息
function rpcWorker(worker) {
  const pending = new Map();
  worker.onmessage = (e) => {
    const { id, ok, result, error } = e.data;
    pending.get(id)[ok ? 'resolve' : 'reject'](ok ? result : new Error(error));
    pending.delete(id);
  };
  return new Proxy({}, {
    get(_, method) {
      return (...args) => new Promise((resolve, reject) => {
        const id = crypto.randomUUID();
        pending.set(id, { resolve, reject });
        worker.postMessage({ id, method, args });
      });
    },
  });
}
// const api = rpcWorker(new Worker('worker.js'));
// await api.sortBig([3, 1, 2]); // 与本地调用无异
```
