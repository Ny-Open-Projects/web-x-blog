---
title: [PER-1051] HTTP 语义的正确使用如何影响性能与缓存
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1051：HTTP 语义的正确使用如何影响性能与缓存

**答**：
- 幂等与缓存联动：GET 可缓存、PUT/DELETE 幂等可重试、POST 不可重试——语义正确才能安全套用重试/缓存策略。
- 状态码精确：304 走协商缓存、206 分片、425 Too Early（0-RTT 重放）、409 冲突——错误码语义化让客户端策略正确。
- 头语义：Location 最终地址、Retry-After 限流恢复时间（客户端按它退避，比盲目重试好）。
- 反例盘点：POST 查询（不可缓存）、200 包裹错误码（客户端无法分类）、PUT 携带服务端生成字段。

```javascript
// 用 Retry-After 驱动退避
async function fetchWith429(url, init) {
  const r = await fetch(url, init);
  if (r.status === 429) {
    const ra = +r.headers.get('Retry-After') || 1;   // 服务端权威建议
    await new Promise(res => setTimeout(res, ra * 1000));
    return fetch(url, init);                          // 按建议重试
  }
  return r;
}
// 配合限流响应头 X-RateLimit-Remaining 提前降速，而非撞墙重试
```
