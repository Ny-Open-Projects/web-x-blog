---
title: [XP-092] JSBridge 的性能优化怎么做？高频通信与批量调用怎么设计？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-092：JSBridge 的性能优化怎么做？高频通信与批量调用怎么设计？
**答**：
- 先量化瓶颈：单次桥调用成本 = 序列化（JSON）+ 线程切换 + messageHandler 分发，P95 通常 2-10ms；高频场景（滚动埋点、输入回显）每帧调用会打爆桥。
- **批量合并**：JS 侧把同一 tick 内的调用聚合成数组，microtask/16ms 窗口 flush 一次，N 次桥调用变 1 次；原生批量处理后一次性回包。
- **payload 瘦身**：埋点字段裁剪与字典表编码（枚举用短码）、图片/文件等大数据不走桥（用 `postMessage` 之外的 Blob/文件路径传递）、避免深层嵌套大对象。
- **优先级队列**：交互类调用（弹窗/支付）高优先级直通，日志类低优先级攒批+空闲时发送，避免低优任务饿死高优交互。
- 协议层配套：调用 id 关联请求响应（多路复用）、超时与重试、原生处理分线程（IO 类下后台线程）；监控桥 P95/P99 进 XP-069 看板，超阈值自动降频。

```javascript
// bridge/optimizer.js —— JSBridge 批量合并 + 优先级队列
class BridgeOptimizer {
  constructor(bridge) {
    this.bridge = bridge;
    this.batches = { high: [], low: [] };
    this.seq = 0; this.pending = new Map();
  }
  call(method, params, { priority = 'high' } = {}) {
    const id = ++this.seq;
    this.batches[priority].push({ id, method, params });   // 攒批：不立即过桥
    if (priority === 'high') this.flush();                  // 高优：当 tick 直通
    else scheduleIdle(() => this.flush());                  // 低优：空闲时统一 flush
    return new Promise((resolve, reject) => this.pending.set(id, { resolve, reject }));
  }
  flush() {
    const items = [...this.batches.high.splice(0), ...this.batches.low.splice(0)];
    if (!items.length) return;
    // N 次调用合并成 1 次原生调用：序列化与线程切换成本降一个数量级
    this.bridge.callNative('__batch__', { items });
  }
  onNativeMessage({ results }) {
    for (const r of results) {
      const p = this.pending.get(r.id);
      p && (r.ok ? p.resolve(r.data) : p.reject(r.error));
      this.pending.delete(r.id);
    }
  }
}
// 埋点场景：track() 走 low 优先级攒批，每 50ms 或满 20 条 flush
// 大数据：图片以本地文件路径传给原生（原生侧读文件），绝不 base64 过桥
// 监控：原生侧回传每批耗时，桥 P95 > 5ms 时 track 自动降采样（XP-069 口径）
```
