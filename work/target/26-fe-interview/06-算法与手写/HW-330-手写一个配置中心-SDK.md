---
title: [HW-330] 手写一个配置中心 SDK：拉取、订阅、灰度与四级容错
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-330：手写一个配置中心 SDK：拉取、订阅、灰度与四级容错

**答**：
- 需求：实现 ConfigSDK：init 拉取全量配置（带 etag 304 复用）；订阅变更（轮询 etag 或长轮询）；按用户灰度（配置分群体）；四级容错：远程 → 本地缓存 → 内置默认 → 兜底空对象；get(path) 点路径取值。
- 边界：304 判断走 etag 存储；缓存版本化（远程版本与本地不一致才覆盖）；轮询退避（连续失败拉长间隔）；配置 schema 校验（非法配置拒绝应用并告警）。
- 评分点：etag 复用；四级容错链；轮询退避。

```javascript
class ConfigSDK {
  constructor(defaults, { pollMs = 30000 } = {}) {
    this.defaults = defaults; this.pollMs = pollMs;
    this.fails = 0; this.cache = null;
  }
  async init() {
    for (const source of [this.fetchRemote, this.readCache, () => this.defaults]) {
      try {
        const cfg = await source();
        if (cfg) { this.apply(cfg); return cfg; }
      } catch { /* 继续下一级 */ }
    }
    this.apply({});                                          // 兜底空对象
    return {};
  }
  async fetchRemote() {
    const res = await fetch('/config', { headers: { 'If-None-Match': this.etag ?? '' } });
    if (res.status === 304) return this.cache;               // 未变复用
    if (!res.ok) throw new Error('cfg-fetch-fail');
    this.etag = res.headers.get('etag');
    const cfg = await res.json();
    localStorage.setItem('cfg', JSON.stringify({ etag: this.etag, cfg, ts: Date.now() }));
    return cfg;
  }
  readCache() {
    const raw = localStorage.getItem('cfg');
    if (!raw) return null;
    const { etag, cfg } = JSON.parse(raw);
    this.etag = etag;
    return cfg;
  }
  apply(cfg) {
    if (this.validate && !this.validate(cfg)) { warnBadConfig(); return; }   // schema 校验
    this.cfg = cfg;
    this.subs?.forEach(fn => fn(cfg));
    this.schedulePoll();
  }
  schedulePoll() {
    clearTimeout(this.timer);
    const ms = this.pollMs * Math.min(2 ** this.fails, 8);   // 轮询退避
    this.timer = setTimeout(async () => {
      try { const c = await this.fetchRemote(); this.fails = 0; if (c) this.apply(c); }
      catch { this.fails++; this.schedulePoll(); }
    }, ms);
  }
  get(path) { return path.split('.').reduce((o, k) => o?.[k], this.cfg ?? {}); }
}
```
