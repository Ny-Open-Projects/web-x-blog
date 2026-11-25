---
title: [WEB-603] 笔试：手写主线程与 Worker 的消息协议（transferable + 回调 id）
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 浏览器架构]
type: 笔试题
---

## WEB-603：笔试：手写主线程与 Worker 的消息协议

**答**：实现 `WorkerClient`（主线程侧）：① `invoke(method, payload, transfer)` 返回 Promise，消息带自增 `reqId`，Worker 回 `resId` 关联；② ArrayBuffer/TypedArray 放进 transfer 列表零拷贝转移；③ 支持超时（默认 30s，超时 reject 且后续迟到响应被忽略）；④ 支持并发调用（reqId 池）；⑤ terminate() 清空所有 pending。写出主线程侧实现与 Worker 侧路由骨架。

```javascript
class WorkerClient {
  constructor(worker, timeout = 30_000) {
    this.worker = worker; this.timeout = timeout;
    this.pending = new Map(); this.seq = 0;
    worker.onmessage = ({ data: { resId, ok, result } }) => {
      const p = this.pending.get(resId);
      if (!p) return;                     // 超时后迟到的响应忽略
      clearTimeout(p.timer); this.pending.delete(resId);
      ok ? p.resolve(result) : p.reject(new Error(result));
    };
  }
  invoke(method, payload, transfer = []) {
    const reqId = ++this.seq;
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        this.pending.delete(reqId);
        reject(new Error(`worker timeout: ${method}`));
      }, this.timeout);
      this.pending.set(reqId, { resolve, reject, timer });
      this.worker.postMessage({ reqId, method, payload }, transfer);
    });
  }
  terminate() {
    for (const { reject, timer } of this.pending.values()) { clearTimeout(timer); reject(new Error('terminated')); }
    this.pending.clear();
    this.worker.terminate();
  }
}
// worker.js 路由骨架:
// self.onmessage = async ({ data: { reqId, method, payload } }) => {
//   try { self.postMessage({ resId: reqId, ok: true, result: await handlers[method](payload) }); }
//   catch (e) { self.postMessage({ resId: reqId, ok: false, result: String(e) }); }
// };
```

**评分点**：
- reqId 关联 + 并发 pending 池结构正确
- transferable 列表透传 postMessage 第二参数
- 超时 reject 且迟到响应被忽略（防 resolve 二次）
- terminate 清理全部 pending，无悬挂 Promise
