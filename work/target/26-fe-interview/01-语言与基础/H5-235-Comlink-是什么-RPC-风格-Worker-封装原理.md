---
title: [H5-235] Comlink 是什么，RPC 风格 Worker 封装原理
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Worker]
type: 面试题
---

## H5-235：Comlink 是什么，RPC 风格 Worker 封装原理

**答**：
- Comlink：Google 出的 Worker RPC 封装——把「postMessage 协议」抽象成「直接调用远程对象」，主线程 `proxy.add(1,2)` 像本地方法一样
- 原理：基于 Proxy 拦截属性访问与方法调用 → 序列化为消息 → Worker 端执行 → 结果回传 Promise
- 价值：消灭手写消息协议（type 字符串、payload 结构、错误传播）的样板与心智负担
- 高级用法：`Comlink.transfer` 标记零拷贝参数、回调也能作为参数传（反向 RPC）、异步迭代支持
- 取舍：Proxy 层有微小开销，且调试堆栈跨线程不直观——简单任务手写 postMessage，复杂接口面用 Comlink

```javascript
// worker.js
importScripts('https://unpkg.com/comlink/dist/umd/comlink.js');
const api = {
  async sort(bigArrayBuffer) { /* ... */ return sorted; },
};
Comlink.expose(api);
// main.js
const api = Comlink.wrap(new Worker('worker.js'));
const sorted = await api.sort(await Comlink.transfer(buf, [buf])); // 像本地调用
```
