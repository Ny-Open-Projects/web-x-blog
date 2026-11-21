---
title: [NODE-269] BFF 的 HTTP 请求收敛与缓存？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-269：BFF 的 HTTP 请求收敛与缓存？
**答**:
- 收敛三招：合批（同接口多 id → batch 接口，DataLoader 模式）、去重（请求内同 URL 去重 promise 单飞）、裁剪（下游支持 fields 参数时只拉需要字段）。
- 跨请求缓存：下游响应按 (url+关键头) 缓存短 TTL——商品详情类读多写少接口收益大；写接口绝不缓存。
- 缓存失效：下游带版本/事件通知（NODE-265 同款）或保守 TTL；命中率进监控（NODE-38x 指标）。
- 请求预算：每请求设置"下游调用数上限"（如 10 次）防失控扇出。

```typescript
// 请求收敛器
class Downloader {
  #inflight = new Map<string, Promise<unknown>>();
  #cache = new Map<string, { body: unknown; ts: number }>();
  async get<T>(url: string, { ttl = 10_000 } = {}): Promise<T> {
    const cached = this.#cache.get(url);
    if (cached && Date.now() - cached.ts < ttl) return cached.body as T;   // 缓存
    if (this.#inflight.has(url)) return this.#inflight.get(url) as Promise<T>;   // 单飞
    const p = fetch(url).then(r => r.json()).then(body => {
      this.#cache.set(url, { body, ts: Date.now() });
      this.#inflight.delete(url);
      return body;
    });
    this.#inflight.set(url, p);
    return p;
  }
}
```
