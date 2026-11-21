---
title: [DP-216] 源码识别：前端监控 SDK 源码中的代理与职责链？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-216：源码识别：前端监控 SDK 源码中的代理与职责链？
**答**：
- 代理：劫持 fetch/XHR/promise rejection/console.error——全局对象的代理包装，采集而不改变原语义；PerformanceObserver 是浏览器原生的观察者（订阅性能事件）。
- 职责链：采集 → 处理（采样/脱敏/去重）→ 批量 → 上报，各环节独立注册（ARC-076 埋点管线），处理管道化。
- 单例+配置：SDK 全局单例（window 下唯一），init options 合并默认值（builder 风格）。
- 识别要点：劫持源码的关键细节——保留原函数引用、返回原返回值、错误时降级不抛（劫持失败不影响业务）。

```javascript
// SDK 劫持：代理模式（保留原语义）
function wrapFetch(report) {
  const orig = window.fetch;
  window.fetch = async function (input, init) {
    const start = performance.now();
    try {
      const res = await orig.call(this, input, init);
      report({ url: String(input), ok: res.ok, ms: performance.now() - start });
      return res;                                    // 语义不变
    } catch (e) {
      report({ url: String(input), ok: false, err: String(e) });
      throw e;                                       // 错误原样上抛，不吞
    }
  };
}
// 管道：处理链
const pipeline = [sampleFilter, maskPII, dedupeByFingerprint, batch(50, 5000)];
function report(ev) { pipeline.reduce((data, stage) => stage(data), ev); }   // 职责链加工
```
