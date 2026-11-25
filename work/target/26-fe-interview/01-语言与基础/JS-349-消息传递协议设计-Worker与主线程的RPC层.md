---
title: [JS-349] 消息传递协议设计：Worker 与主线程的 RPC 层
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-349：消息传递协议设计：Worker 与主线程的 RPC 层

**答**：
- 裸 postMessage 的问题：回调地狱（事件里判断是谁的回复）、无超时、无类型安全——工程做法是封装 RPC 层：reqId 关联、Promise 化、超时/取消、错误序列化
- 协议字段设计：`{ id, method, payload }` 请求 / `{ id, ok, result|error }` 响应 / `{ event, data }` 推送——三类消息显式区分
- 错误序列化：Error 对象跨线程只剩 message（clone 丢失 stack）——协议里显式传 `{ name, message, stack }` 重建
- 双向对称：Worker 也可以主动调主线程（回调接口，如进度上报 event 消息）——进度用 event 流（多次推送），结果用响应
- TypeScript 增益：接口定义共享类型（`WorkerAPI` 接口），主线程 client 与 worker handler 编译期校验——消息协议类型安全是长期维护关键

```typescript
// 共享协议定义
interface WorkerAPI {
  hash(data: ArrayBuffer): string;
  compress(data: Uint8Array): Uint8Array;
}
// 主线程 client
class WorkerClient {
  private seq = 0;
  private pending = new Map<number, { res: (v: any) => void; rej: (e: Error) => void; timer: number }>();
  constructor(private w: Worker) {
    w.onmessage = ({ data }) => this._on(data);
  }
  call<K extends keyof WorkerAPI>(method: K, ...args: any[]): Promise<WorkerAPI[K]> {
    const id = ++this.seq;
    return new Promise((res, rej) => {
      const timer = setTimeout(() => { this.pending.delete(id); rej(new Error('timeout')); }, 30_000);
      this.pending.set(id, { res, rej, timer });
      this.w.postMessage({ id, method, payload: args });
    });
  }
  private _on(data: any) {
    const p = this.pending.get(data.id);
    if (!p) return;
    clearTimeout(p.timer); this.pending.delete(data.id);
    data.ok ? p.res(data.result) : p.rej(new Error(data.error?.message ?? 'worker error'));
  }
}
```
