---
title: [ARC-077] JSBridge 如何设计（协议/回调表/兼容）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-077：JSBridge 如何设计（协议/回调表/兼容）？
**答**：
- 协议三要素：方法命名空间（`app.getGPS`）、参数与回调约定（JSON 序列化）、版本协商（能力探测）。
- 回调实现：每次调用生成 callbackId 存入回调表，Native 回来时按 id 取出并执行后删除，解决"多次调用交错返回"。
- 通道兼容：iOS 用 `messageHandlers`/scheme 拦截，Android 用 `addJavascriptInterface`，统一封装成同一套 API。

```typescript
// JSBridge 核心实现：协议 + 回调表
interface BridgeMessage { id: string; method: string; params: unknown; }

class JSBridge {
  private seq = 0;
  private callbacks = new Map<string, { resolve: (v: unknown) => void; timer: number }>();

  invoke<T>(method: string, params: unknown, timeout = 10_000): Promise<T> {
    const id = `cb_${++this.seq}`;
    return new Promise<T>((resolve, reject) => {
      this.callbacks.set(id, { resolve: resolve as (v: unknown) => void, timer: 0 });
      const msg: BridgeMessage = { id, method, params };
      if (/(iPhone|iPad)/.test(navigator.userAgent))
        (window as any).webkit.messageHandlers.corpBridge.postMessage(JSON.stringify(msg)); // iOS 通道
      else
        (window as any).corpBridge?.postMessage(JSON.stringify(msg))                        // Android 通道
        ?? location.href = `corpscheme://bridge?d=${encodeURIComponent(JSON.stringify(msg))}`; // 兜底 scheme
      this.callbacks.get(id)!.timer = window.setTimeout(() => {
        this.callbacks.delete(id); reject(new Error(`${method} bridge timeout`));           // 超时防泄漏
      }, timeout);
    });
  }
  // Native 回调入口：window.__corpBridgeCallback__(id, result)
  handleNative(id: string, result: unknown) {
    const cb = this.callbacks.get(id);
    if (!cb) return;
    clearTimeout(cb.timer); this.callbacks.delete(id);
    cb.resolve(typeof result === 'string' ? JSON.parse(result) : result);
  }
}
// 能力协商：const can = await bridge.invoke<boolean>('app.hasCapability', { name: 'pay' });
```
