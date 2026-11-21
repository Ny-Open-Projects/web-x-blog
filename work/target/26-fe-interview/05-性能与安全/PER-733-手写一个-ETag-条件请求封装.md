---
title: [PER-733] 手写一个 ETag 条件请求封装：If-None-Match 协商缓存与 304 处理，弱网下省流量验证
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-733：手写一个 ETag 条件请求封装：If-None-Match 协商缓存与 304 处理，弱网下省流量验证

**答**：
- 实现：响应缓存时保存 ETag；下次请求带 `If-None-Match`；304 时复用本地缓存数据（配合 731 的 H5 层缓存）；200 时更新缓存与新 ETag。
- 要点：ETag 存储与数据绑定（同 key 一致更新，避免数据新 ETag 旧的错位）；304 处理要在 fetch 封装层透明完成（业务拿到的永远是数据）；弱网收益验证（304 比例、传输字节对比）。
- 边界：服务端不强一致（ETag 碰撞场景可忽略）；no-store 响应不缓存；HEAD 探测不适用（要 GET）。
- 评分点：ETag 与数据一致性绑定。

```javascript

class EtagFetch {
  constructor(store) { this.store = store; this.stats = { hit304: 0, full: 0 }; }
  async get(url) {
    const cached = await this.store.get(url);                   // {data, etag, ts}
    const headers = cached ? { 'If-None-Match': cached.etag } : {};
    const res = await fetch(url, { headers, cache: 'no-cache' }); // 协商缓存
    if (res.status === 304 && cached) {
      this.stats.hit304++;
      return cached.data;                                       // 透明复用本地数据
    }
    this.stats.full++;
    const etag = res.headers.get('ETag');
    const data = await res.json();
    if (etag) await this.store.set(url, { data, etag, ts: Date.now() }); // ETag 与数据绑定更新
    else if (cached) await this.store.set(url, { data, etag: '', ts: Date.now() });
    return data;
  }
  report() { // 304 比例高 = 协商缓存生效，弱网流量显著下降
    const { hit304, full } = this.stats;
    return { hit304Rate: +(hit304 / Math.max(1, hit304 + full) * 100).toFixed(0) + '%' };
  }
}
```
