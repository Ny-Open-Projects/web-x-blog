---
title: [PER-569] 手写一个上报失败重试队列：IndexedDB 暂存失败包，指数退避补发并限制总量
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-569：手写一个上报失败重试队列：IndexedDB 暂存失败包，指数退避补发并限制总量

**答**：
- 比上一题更完整：重试要有**指数退避 + 次数上限**（失败 3 次放弃防死循环）、**总量上限**（队列超 200 条丢最旧，防存储膨胀）、**补发节流**（启动后空闲时段补发，不抢首屏）。
- 要点：`visibilitychange` 到 hidden 时 flush；同一包不被并发补发（状态标记）；msgId 保证服务端幂等。
- 边界：IndexedDB 不可用（隐私模式）降级内存队列，接受丢失。
- 评分点：退避/上限/幂等三要素。

```javascript

class RetryReporter {
  constructor(max = 200, maxRetry = 3) { this.max = max; this.maxRetry = maxRetry; this.mem = []; }
  async enqueue(body, attempt = 0) {
    const item = { body, attempt, ts: Date.now() };
    try {
      const db = await this.db();
      const tx = db.transaction('q', 'readwrite');
      const store = tx.objectStore('q');
      store.add(item);
      store.count().onsuccess = ({ target }) => {          // 总量上限：丢最旧
        if (target.result > this.max) store.openCursor().onsuccess = ({ result }) =>
          result && result.delete(result.primaryKey);
      };
    } catch { this.mem.push(item); }                      // 隐私模式降级内存
  }
  send(payload) {
    const body = JSON.stringify({ id: crypto.randomUUID(), clientTs: Date.now(), ...payload });
    if (!navigator.sendBeacon('/collect', body)) this.enqueue(body);
  }
  async replay() {                                        // 空闲时补发，指数退避
    const run = async () => {
      const db = await this.db();
      const all = await new Promise(r => { const q = db.transaction('q').objectStore('q').getAll();
        q.onsuccess = () => r(q.result); });
      for (const it of all) {
        const delay = 2 ** it.attempt * 1000;
        await new Promise(r => setTimeout(r, delay));
        if (navigator.sendBeacon('/collect', it.body)) this.drop(it);
        else if (it.attempt >= this.maxRetry) this.drop(it);   // 放弃并计数
        else { this.drop(it); this.enqueue(it.body, it.attempt + 1); }
      }
    };
    ('requestIdleCallback' in window) ? requestIdleCallback(run) : setTimeout(run, 5000);
  }
  async drop(it) { const db = await this.db();
    db.transaction('q', 'readwrite').objectStore('q').delete(it.body.id ?? it.ts); }
  db() { return new Promise((res, rej) => { const r = indexedDB.open('rq', 1);
    r.onupgradeneeded = () => r.result.createObjectStore('q');
    r.onsuccess = () => res(r.result); r.onerror = rej; }); }
}
```
