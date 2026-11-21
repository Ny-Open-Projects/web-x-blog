---
title: [AGT-476] 笔试题——实现工具并发控制（信号量+下游保护+优先级插队）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-476：手写并发控制：每工具信号量、下游限流联动、高优插队、超时释放

**需求与边界**：
- 输入：工具调用请求、每工具并发配置；输出：受控执行。
- 边界要求：① 每工具独立信号量（防单工具打爆下游）；② 全局并发上限；③ 高优任务插队（不违反已授权执行的公平性）；④ 持锁超时强制释放（防泄漏死锁）。

**答**：
```javascript
class ConcurrencyGuard {
  constructor({ limits, global = 20, holdTimeout = 60e3 }) {
    this.limits = limits;                 // { web_search: 5, db: 3 }
    this.global = global;
    this.holdTimeout = holdTimeout;
    this.counts = new Map();              // 工具级
    this.globalCount = 0;
    this.waiting = [];                    // [{resolve, priority, ts}]
  }
  async acquire(tool, priority = 'normal') {
    const limit = this.limits[tool] ?? 5;
    // 快路径：有余量直接拿
    if (this.tryTake(tool, limit)) return this.wrap(tool);
    // 排队：按优先级插入（高优插队）
    return new Promise(resolve => {
      const item = { resolve: () => {
        if (this.tryTake(tool, limit)) resolve(this.wrap(tool));
      }, priority, ts: Date.now(), tool, limit };
      if (priority === 'high')
        this.waiting.unshift(item);
      else this.waiting.push(item);
      this.pump();                        // 尝试唤醒
    });
  }
  tryTake(tool, limit) {
    const c = this.counts.get(tool) ?? 0;
    if (c >= limit || this.globalCount >= this.global) return false;
    this.counts.set(tool, c + 1); this.globalCount++;
    return true;
  }
  wrap(tool) {
    const release = () => {
      this.counts.set(tool, this.counts.get(tool) - 1);
      this.globalCount--;
      this.pump();                        // 释放后唤醒等待者
    };
    // 持锁超时强制释放（防泄漏）
    const timer = setTimeout(() => {
      alert('HOLD_TIMEOUT', { tool }); release();
    }, this.holdTimeout);
    return { release: () => { clearTimeout(timer); release(); } };
  }
  pump() { this.waiting = this.waiting.filter(w =>
    (w.resolve(), !this.tryTake(w.tool, w.limit))); }
}
```

**评分点**:
- 工具级+全局双层信号量（下游保护）。
- 高优插队入队策略；释放时 pump 唤醒等待者（不泄漏唤醒机会）。
- 持锁超时强制释放（防死锁泄漏），带告警。
- 快路径避免无竞争时排队开销。
