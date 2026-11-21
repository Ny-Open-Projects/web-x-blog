---
title: [TST-265] SSR 页面缓存（边缘/内存）的测试要点？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-265：SSR 页面缓存（边缘/内存）的测试要点？
**答**：
- 缓存键正确性：同 URL 不同 Vary 头（cookie/设备）不串缓存。
- 失效机制：数据更新后对应 tag 失效，下次请求拿到新内容。
- TTL 行为：过期后回源、期内命中（响应头 x-cache: HIT/MISS 断言）。
- 缓存穿透与雪崩防护：不存在页/热点页的防护行为测试。

```javascript
test('缓存失效联动', async ({ request }) => {
  expect((await request.get('/goods/1')).headers()['x-cache']).toBe('MISS');
  expect((await request.get('/goods/1')).headers()['x-cache']).toBe('HIT');
  await adminPatchGoods(1);                          // 更新 → tag 失效
  expect((await request.get('/goods/1')).headers()['x-cache']).toBe('MISS');
});
r
```
