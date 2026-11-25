---
title: [HW-111] 手写多定时器管理器——命名定时器、统一暂停/恢复（visibilitychange）与泄漏防护
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-111：手写多定时器管理器——命名定时器、统一暂停/恢复（visibilitychange）与泄漏防护
**答**：轮询/时间轴/动画常需多个定时器，散落管理易泄漏。管理器：按 key 注册（重复注册自动替换旧实例）；页面 hidden 统一暂停、visible 恢复（移动端省电）；destroy 全量清理；执行回调 try-catch 防一个回调炸掉整个循环。

```javascript
class TimerHub {
  constructor({ pauseOnHidden = true } = {}) {
    this.timers = new Map();                          // key -> {id, ms, fn, paused}
    if (pauseOnHidden) document.addEventListener('visibilitychange', () => {
      document.visibilityState === 'hidden' ? this.pauseAll() : this.resumeAll();
    });
  }
  set(key, fn, ms) {
    this.clear(key);                                  // 重复 key：替换旧定时器
    const t = { fn, ms, id: setInterval(() => {
      try { fn(); } catch (e) { console.error(`[timer:${key}]`, e); }   // 单回调失败不炸循环
    }, ms), paused: false };
    this.timers.set(key, t);
    return () => this.clear(key);
  }
  clear(key) { const t = this.timers.get(key); if (t) { clearInterval(t.id); this.timers.delete(key); } }
  pauseAll() { for (const [, t] of this.timers) { clearInterval(t.id); t.paused = true; } }
  resumeAll() { for (const [, t] of this.timers) {
    if (t.paused) { t.id = setInterval(() => { try { t.fn(); } catch (e) { console.error(e); } }, t.ms); t.paused = false; } } }
  destroy() { for (const [, t] of this.timers) clearInterval(t.id); this.timers.clear(); }
}
// 用法：轮询 + 时间轴统一管理
const hub = new TimerHub();
hub.set('poll-orders', pollOrders, 5000);
hub.set('timeline', updateTimeline, 1000);
// 页面 hidden 自动全部暂停；destroy() 供 SPA 路由卸载调用 —— 无泄漏
// 反例：到处 setInterval 不清 —— 长驻 SPA 定时器堆积 + hidden 时空转耗电
```

**评分点**：
- key 注册 + 重复注册替换（防重复轮询——双倍轮询是常见 bug）。
- visibilitychange 统一暂停/恢复（hidden 空转耗电问题）。
- 单回调 try-catch 隔离；destroy 全量清理。
- 返回取消函数的 API 设计（调用方可自主清理）。
