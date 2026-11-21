---
title: [HW-199] 手写带 transfer 的 RPC——Comlink 风格封装 + 大 buffer 自动 transfer + 参数校验
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：HW-289 RPC 的 transfer 增强：调用参数中 ArrayBuffer 自动识别进 transfer 列表（零拷贝）；返回值同理（worker 端标记 transfer）；参数校验（函数/DOM 不可传——clone 会抛错，提前报错提示）；调用池复用 worker（HW-270 回压）。

```javascript
function collectTransferables(value, out = new Set()) {   // 递归收集 ArrayBuffer
  if (value instanceof ArrayBuffer || value.buffer instanceof ArrayBuffer) out.add(value);
  else if (Array.isArray(value)) value.forEach((v) => collectTransferables(v, out));
  else if (value && typeof value === 'object') {
    if (value instanceof Map || value instanceof Set) [...value.values()].forEach((v) => collectTransferables(v, out));
    else Object.values(value).forEach((v) => collectTransferables(v, out));
  }
  return [...out];
}
function rpc(worker) {
  const pending = new Map(); let seq = 0;
  worker.onmessage = ({ data }) => {
    const p = pending.get(data.id);
    pending.delete(data.id);
    data.error ? p.reject(new Error(data.error)) : p.resolve(data.result);
  };
  return (path, args, { returnsTransferables = true } = {}) => new Promise((resolve, reject) => {
    for (const a of args) if (typeof a === 'function' || a instanceof HTMLElement)
      return reject(new TypeError(`不可序列化参数: ${path}`));    // 提前报错（比 clone 运行时错误友好）
    const id = ++seq;
    pending.set(id, { resolve, reject });
    const transfer = collectTransferables(args);           // 自动收集大 buffer
    worker.postMessage({ id, path, args }, transfer);      // 零拷贝传大块
  });
}
// worker 端返回大 buffer：结果包装 { result, transfer: [buf] } → 主线程 postMessage(msg.result, msg.transfer)
// 收益：10MB buffer clone 100ms → transfer 0ms（PER-386 判定公式的执行层）
// 注意：transfer 后主线程原 buffer byteLength=0（所有权转移语义，调用方不可再读原值——文档必须写明）
```

**评分点**：
- collectTransferables 递归收集（ArrayBuffer/TypedArray/Map/Set 嵌套）。
- 不可序列化参数提前报错（函数/DOM）——比 clone 抛错友好。
- transfer 所有权语义警告（原 buffer 失效）——本题核心。
- 与回压池（HW-270）组合的完整形态。
