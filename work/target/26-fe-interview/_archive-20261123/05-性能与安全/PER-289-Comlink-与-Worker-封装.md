---
title: [PER-289] 直接写 Worker 通信代码太繁琐，Comlink 类 RPC 封装的原理是什么？要注意什么？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-289：直接写 Worker 通信代码太繁琐，Comlink 类 RPC 封装的原理是什么？要注意什么？

**答**：
- 原理：postMessage/onmessage 之上包一层 Promise RPC——调用方 `proxy.method(args)` 返回 Promise，内部把调用序列化成 `{type:'CALL', path, args, id}` 消息，worker 端解析路径调用真实方法，结果按 id 回传 resolve。用 Proxy 拦截属性访问实现"像本地对象一样调用"。
- 要注意：① 参数与返回值仍受 structured clone 限制（函数/DOM 传不了，需 transferable 或暴露句柄）；② 每次调用都是真实消息往返（几 ms 延迟），细粒度循环调用会把收益吃光——批量接口优于逐条调用；③ 回调无法直接传，Comlink.proxy 把主线程回调包装成可跨线程调用的代理（每个调用仍是异步）。
- 何时值得：计算 > 10ms 且数据可序列化；否则主线程直接算。封装后要保留 transfer 逃生门（大 buffer 用 transfer 显式传，避免 clone）。

```javascript
// 极简 RPC 封装（Comlink 思想）
function expose(api) {
  self.onmessage = async ({ data: { id, path, args } }) => {
    try {
      const fn = path.split('.').reduce((o, k) => o[k], api);
      const result = await fn(...args);
      self.postMessage({ id, result });          // 结构化返回（大 buffer 建议 transfer）
    } catch (e) { self.postMessage({ id, error: String(e) }); }
  };
}
function wrap(worker) {
  const pending = new Map(); let seq = 0;
  worker.onmessage = ({ data }) => {
    const p = pending.get(data.id); pending.delete(data.id);
    data.error ? p.reject(new Error(data.error)) : p.resolve(data.result);
  };
  return new Proxy({}, { get: (_, path) => (...args) =>
    new Promise((resolve, reject) => {
      const id = ++seq; pending.set(id, { resolve, reject });
      worker.postMessage({ id, path, args });
    }) });
}
// 主线程：const api = wrap(new Worker('calc.js')); const sorted = await api.sort(bigArr);
```
