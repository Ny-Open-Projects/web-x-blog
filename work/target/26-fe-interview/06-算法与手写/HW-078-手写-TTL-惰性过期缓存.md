---
title: [HW-078] 手写 TTL 缓存——惰性过期 + 后台清理 + 过期回调
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-078：手写 TTL 缓存——惰性过期 + 后台清理 + 过期回调
**答**：TTL 缓存两种过期方式：惰性（get 时检查，省 CPU 但过期项占内存）与后台定期清理（省内存但有延迟）；生产实现两者结合。要点：过期时间覆盖（set 覆盖 TTL）、过期回调（onExpire 便于埋点/降级）、清理用最小堆或按到期时间排序批量删。

```javascript
class TTLCache {
  constructor({ ttl = 60000, max = 1000, sweepInterval = 30000, onExpire } = {}) {
    Object.assign(this, { ttl, max, onExpire });
    this.map = new Map();                                  // key -> {val, exp, insertedAt}
    this.sweep = setInterval(() => this.#sweep(), sweepInterval);
    this.sweep.unref?.();                                  // Node 下不阻止进程退出
  }
  set(key, val, ttl = this.ttl) {
    if (this.map.size >= this.max && !this.map.has(key)) { // 容量兜底：先删最旧
      const oldestKey = this.map.keys().next().value;
      this.#delete(oldestKey, 'evicted');
    }
    this.map.set(key, { val, exp: Date.now() + ttl });
  }
  get(key) {
    const item = this.map.get(key);
    if (!item) return undefined;
    if (Date.now() > item.exp) { this.#delete(key, 'lazy'); return undefined; }  // 惰性过期
    return item.val;
  }
  #sweep() {                                               // 后台批量清理
    const now = Date.now();
    for (const [k, item] of this.map) if (now > item.exp) this.#delete(k, 'sweep');
  }
  #delete(key, reason) {
    const item = this.map.get(key);
    this.map.delete(key);
    if (item && this.onExpire && reason !== 'lazy' && reason !== 'evicted') this.onExpire(key, reason);
    else if (item && this.onExpire && reason === 'evicted') this.onExpire(key, reason);
  }
  destroy() { clearInterval(this.sweep); this.map.clear(); }   // 长驻页面必备
}
// 用法：验证码缓存 5 分钟过期
const codes = new TTLCache({ ttl: 5 * 60000, sweepInterval: 10000 });
codes.set('user1', '123456');
codes.get('user1');   // 5 分钟内有效，过期后惰性判定 undefined
```

**评分点**：
- 惰性 + 后台双通道过期，两者职责说清（省 CPU vs 控内存）。
- 容量兜底（max + 最旧淘汰）防止只依赖 TTL 时堆积。
- destroy 清定时器（长驻页面/测试环境必备）。
- 过期回调 reason 区分（lazy/sweep/evicted）。
