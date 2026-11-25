---
title: [PER-226] bfcache（往返缓存）如何影响 Web Vitals 采样？pageshow persisted 后要处理什么？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-226：bfcache（往返缓存）如何影响 Web Vitals 采样？pageshow persisted 后要处理什么？

**答**：
- bfcache 是浏览器把离开页面的完整快照（JS 堆、DOM）存内存，后退时毫秒级恢复。CrUX 会把 back_forward 导航单独统计，其 LCP/INP 普遍极好，混入全量会拉低分位数、掩盖真实体验。
- 采样污染点：恢复页的 PerformanceObserver 会带着旧 buffer 继续上报，LCP/CLS 可能重复或沿用旧值；unload/visibilitychange 状态残留；过期轮询定时器恢复后立刻触发。
- 正确处理：`pageshow` 事件里检查 `event.persisted`；为 true 时——重新初始化指标采集（重置 observer 与累计值）、恢复轮询定时器、重连 WebSocket；`pagehide`（而不是 unload）做卸载前上报（bfcache 页不触发 unload）。
- 逃生口：页面确实不希望被缓存（如计时敏感），可发 `Cache-Control: no-store`，但这是性能自杀行为，应避免；正确姿势是适配 bfcache。

```javascript
addEventListener('pageshow', (e) => {
  if (e.persisted) {                       // bfcache 恢复
    resetVitalsTrackers();                 // 1. 重置 LCP/CLS/INP 采集（旧值已上报过）
    startPolling();                        // 2. 重启被冻结的轮询定时器
    reconnectWS();                         // 3. 重连长连接
    document.title = document.title;       // 4. 触发一次 UI 状态刷新
  }
});
addEventListener('pagehide', (e) => {      // 用 pagehide 而非 unload（bfcache 兼容）
  if (!e.persisted) flushBeacons();        // 真正卸载才 flush；进入缓存则什么都不做
});
```
