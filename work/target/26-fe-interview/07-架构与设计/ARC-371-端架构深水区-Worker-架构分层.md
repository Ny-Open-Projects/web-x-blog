---
title: [ARC-371] Web Worker 的架构分层如何设计？主线程与 Worker 的职责划分
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-371：Web Worker 的架构分层如何设计？
**答**：
- 职责划分原则：主线程只做 UI 渲染与用户交互，一切 > 16ms 的 CPU 密集任务（数据转换/加解密/搜索索引/大 JSON 解析）下沉 Worker。
- 架构上把 Worker 包装为"异步服务层"：主线程通过 RPC 协议（请求 ID + Promise）调用，业务代码无感；Worker 内部可再分"计算模块 + 缓存模块"。
- 生命周期：常驻 Worker（缓存可复用）vs 按需创建（省内存）；页面隐藏时休眠，避免空转内存。
- 数据传输：结构化克隆有成本，大数据用 Transferable（ArrayBuffer）零拷贝转移，或 SharedArrayBuffer + Atomics（需 COOP/COEP 头）。
- 失败处理：Worker 崩溃自动重启 + 任务重放；不支持 Worker 的环境（老 WebView）降级主线程执行 + 性能降级提示。
```javascript
// Worker RPC 封装
class WorkerClient {
  constructor(worker) { this.w = worker; this.seq = 0; this.pending = new Map();
    worker.onmessage = ({ data }) => {
      const p = this.pending.get(data.id); if (!p) return;
      data.error ? p.reject(data.error) : p.resolve(data.result);
      this.pending.delete(data.id);
    };
  }
  call(method, payload, transfer = []) {
    const id = ++this.seq;
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      this.w.postMessage({ id, method, payload }, transfer);
    });
  }
}
// 业务侧：await client.call('parseCsv', buffer, [buffer])  // 零拷贝
```
