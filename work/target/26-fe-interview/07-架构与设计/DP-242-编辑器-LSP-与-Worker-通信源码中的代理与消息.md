---
title: [DP-242] 源码识别：Monaco/Worker 通信源码中的代理与命令？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-242：源码识别：Monaco/Worker 通信源码中的代理与命令？
**答**:
- 代理模式（RPC 桩）：Worker/主线程跨线程调用被包装成同步 API（`editor.getModel()` 底层是 postMessage + 回执）——调用方无感跨线程；Monaco 的 language worker 全是这种桩。
- 命令+关联表：消息带递增 id，pending Map 存 { resolve, reject, timer }，回执按 id 配对——超时 reject 防悬挂。
- 观察者：事件类消息（onDidChangeContent）与请求类消息分流：事件走 emitter，请求走 pending。
- 识别要点：能默写"双通道封装"（req/res 带序号 + event 广播），并说清 transferable（postMessage 拷贝成本 → ArrayBuffer transfer / SharedArrayBuffer）。

```javascript
// Worker RPC 代理（源码级简化）
function createWorkerProxy(worker, methods) {
  const pending = new Map();
  let seq = 0;
  worker.onmessage = ({ data }) => {
    if (data.event) return emitter.emit(data.event, data.payload);   // 事件通道
    const p = pending.get(data.id);
    if (!p) return;
    pending.delete(data.id);
    data.error ? p.reject(data.error) : p.resolve(data.result);      // 回执配对
  };
  const proxy = {};
  for (const m of methods) {
    proxy[m] = (...args) => new Promise((resolve, reject) => {
      const id = ++seq;
      pending.set(id, { resolve, reject,
        timer: setTimeout(() => { pending.delete(id); reject(new TimeoutError(m)); }, 10_000) });
      worker.postMessage({ id, method: m, args });
    });
  }
  return proxy;
}
// 主线程：const lint = proxy('lintCode'); const issues = await lintCode(source)  —— 同步感 API
```
