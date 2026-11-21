---
title: [DP-097] 监控系统 SDK 用了哪些模式？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-097：监控系统 SDK 用了哪些模式？（高频）
**答**：
- **外观**：`SDK.init/report/user()` 一个入口，内部封装采集器、上报队列、存储。
- **职责链 + 策略**：上报数据经过"过滤→脱敏→采样→压缩"流水线；采样策略（全量/百分比/错误必采）可配置。
- **享元/对象池**：事件对象复用、批量合并上报（队列 + 定时 flush）减少请求数。
- **观察者**：劫持 `window.onerror/unhandledrejection/fetch/XHR` 把全局异常"广播"进 SDK；**备忘录**：用户行为栈快照随错误一起上报。

```javascript
// 监控 SDK 骨架：外观 + 职责链 + 策略 + 享元
class MonitorSDK {
  #queue = [];                          // 上报队列（批量 = 享元思想：合并小请求）
  #pipeline = [];                       // 职责链：数据加工流水线
  #config = { sampleRate: 1, flushInterval: 5000, maxBatch: 10 };
  init(config = {}) {                   // 外观入口1
    Object.assign(this.#config, config);
    this.#installGlobalHandlers();      // 观察者：劫持全局错误源
    setInterval(() => this.#flush(), this.#config.flushInterval);
    return this;
  }
  use(fn) { this.#pipeline.push(fn); return this; }  // 注册流水线节点（插件式扩展）
  report(event) {                       // 外观入口2
    const ctx = { event, ts: Date.now(), dropped: false };
    for (const fn of this.#pipeline) {  // 职责链：过滤->脱敏->采样
      fn(ctx);
      if (ctx.dropped) return;
    }
    this.#queue.push(ctx);
    if (this.#queue.length >= this.#config.maxBatch) this.#flush(); // 攒批
  }
  #installGlobalHandlers() {
    window.addEventListener('error', (e) => this.report({
      type: 'js_error', msg: e.message, stack: e.error?.stack, // 备忘录：行为栈随错误上报
      breadcrumbs: this.#breadcrumbs.slice(-10),
    }), true);
    window.addEventListener('unhandledrejection', (e) => this.report({ type: 'promise_error', msg: String(e.reason) }));
    const rawFetch = window.fetch;
    window.fetch = async (...args) => {              // 代理：劫持网络请求
      const start = performance.now();
      try {
        const res = await rawFetch(...args);
        this.report({ type: 'api', url: String(args[0]), status: res.status, cost: performance.now() - start });
        return res;
      } catch (err) {
        this.report({ type: 'api_error', url: String(args[0]), msg: String(err) });
        throw err;
      }
    };
  }
  #breadcrumbs = [];
  trackBreadcrumb(action) { this.#breadcrumbs.push({ action, at: Date.now() }); }
  #flush() {                            // 批量上报（减少请求数）
    if (!this.#queue.length) return;
    const batch = this.#queue.splice(0);
    navigator.sendBeacon?.('/collect', JSON.stringify(batch)) ?? fetch('/collect', { body: JSON.stringify(batch), method: 'POST' });
  }
}
// 使用：链式装配流水线
const sdk = new MonitorSDK()
  .use((ctx) => {                                    // 节点1：脱敏
    if (ctx.event.url) ctx.event.url = ctx.event.url.replace(/token=[^&]+/, 'token=***');
  })
  .use((ctx) => {                                    // 节点2：采样策略（错误必采，普通日志按比例）
    if (ctx.event.type !== 'js_error' && Math.random() > 0.1) ctx.dropped = true;
  })
  .init({ sampleRate: 0.1 });
sdk.trackBreadcrumb('click 提交按钮');
window.dispatchEvent(new ErrorEvent('error', { message: 'boom' }));
// [采集] js_error 入队 —— 行为栈 + 异常一起上报
```
