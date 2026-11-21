---
title: [MFW-167] SSR 层的缓存击穿、雪崩怎么治理？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-167：SSR 层的缓存击穿、雪崩怎么治理？
**答**：
- 击穿（热点 key 过期瞬间并发回源打爆下游）：解法是 **singleflight/互斥重建**——同一 key 只有一个请求真正回源，其余等待共享结果；配合热点 key 常驻（逻辑过期）。
- 雪崩（大量 key 同时过期）：解法是 **TTL 打散**（基础 TTL ± 随机抖动）+ 分层缓存（内存 L1 → Redis L2 → 源），任一层过期不会齐刷刷穿透。
- 穿透（查询不存在的 key 永远 miss）：空值缓存（短 TTL）+ 布隆过滤器挡明显非法 id。
- SSR 特有的放大效应：一个页面渲染要 N 个数据，缓存 miss 时延迟放大 N 倍且并发高——「页面级缓存优先于数据级缓存」（先挡住整页请求）。
- 兜底：回源失败返回 stale 旧值（stale-while-error）比报错强。

```ts
// 分层缓存 + 打散 + singleflight 的 SSR 数据层
class ResilientCache {
  private l1 = new Map<string, { value: unknown; exp: number; logicalExp: number }>();
  private inflight = new Map<string, Promise<unknown>>();

  async get<T>(key: string, loader: () => Promise<T>, baseTtlMs: number): Promise<T> {
    const hit = this.l1.get(key);
    const now = Date.now();

    // 热点常驻：物理过期但逻辑未过期 -> 先回旧值 + 后台刷新（防击穿）
    if (hit && now < hit.logicalExp) {
      if (now >= hit.exp) this.refresh(key, loader, baseTtlMs); // 异步，不阻塞
      return hit.value as T;
    }

    // singleflight：并发 miss 只回源一次（防击穿）
    if (this.inflight.has(key)) return this.inflight.get(key) as Promise<T>;
    const p = loader()
      .then((value) => {
        const jitter = baseTtlMs * (0.8 + Math.random() * 0.4);      // TTL ±20% 打散（防雪崩）
        this.l1.set(key, { value, exp: now + jitter, logicalExp: now + jitter * 2 });
        this.inflight.delete(key);
        return value;
      })
      .catch((e) => {
        this.inflight.delete(key);
        if (hit) return hit.value as T;   // stale-while-error：回源失败回旧值
        throw e;
      });
    this.inflight.set(key, p);
    return p as Promise<T>;
  }

  private refresh(key: string, loader: () => Promise<unknown>, ttl: number): void {
    loader().then((value) => {
      this.l1.set(key, { value, exp: Date.now() + ttl, logicalExp: Date.now() + ttl * 2 });
    }).catch(() => {});
  }
}
```
