---
title: [HW-332] 手写一个 Feature Flag SDK：本地求值与事件流更新
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-332：手写一个 Feature Flag SDK：本地求值与事件流更新

**答**：
- 需求：实现 FlagsSDK：flags 定义 {key, default, rules: [{if: {attr}, value}]}；evaluate(key, userCtx) 本地求值（规则按序首个命中）；更新通道：轮询配置 + SSE 事件流（变更即时推送）；变更订阅回调；评估埋点（记录评估结果用于分析）。
- 边界：SSE 断线重连（退避）+ 轮询兜底双通道去重（版本号防旧覆盖新）；规则属性匹配（eq/in/exists）；评估缓存（同 ctx 5s 内复用）。
- 评分点：双通道版本去重；本地求值；评估埋点。

```javascript
class FlagsSDK {
  constructor(flags) { this.flags = new Map(Object.entries(flags)); this.subs = new Set(); this.cache = new Map(); }
  evaluate(key, userCtx = {}) {
    const ck = key + JSON.stringify(userCtx);
    const c = this.cache.get(ck);
    if (c && Date.now() - c.t < 5000) return c.v;            // 评估缓存
    const def = this.flags.get(key);
    let value = def?.default;
    for (const rule of def?.rules ?? []) {                   // 按序首个命中
      if (matchRule(rule.if, userCtx)) { value = rule.value; break; }
    }
    this.cache.set(ck, { v: value, t: Date.now() });
    track('flag-eval', { key, value });                      // 评估埋点
    return value;
  }
  onUpdate(fn) { this.subs.add(fn); return () => this.subs.delete(fn); }
  startChannels() {
    this.sse = new EventSource('/flags/stream');              // 通道一：SSE
    this.sse.onmessage = e => this.apply(JSON.parse(e.data));
    this.sse.onerror = () => { this.sse.close(); this.fails = (this.fails ?? 0) + 1;
      setTimeout(() => this.startChannels(), Math.min(1000 * 2 ** this.fails, 30000)); };
    this.poll = setInterval(async () => {                     // 通道二：轮询兜底
      const flags = await fetchFlags();
      this.apply(flags);
    }, 60000);
  }
  apply(flags) {
    for (const [k, v] of Object.entries(flags)) {
      const cur = this.flags.get(k);
      if (cur && cur.version >= v.version) continue;         // 版本号防旧覆盖新
      this.flags.set(k, v);
      this.cache.clear();
      this.subs.forEach(fn => fn(k, v.default));
    }
  }
}
function matchRule(cond, ctx) { return Object.entries(cond ?? {}).every(([k, v]) =>
  Array.isArray(v) ? v.includes(ctx[k]) : ctx[k] === v); }
```
