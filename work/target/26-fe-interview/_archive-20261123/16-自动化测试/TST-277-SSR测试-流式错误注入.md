---
title: [TST-277] 流式 SSR 中途错误的测试注入方法？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-277：流式 SSR 中途错误的测试注入方法？
**答**：
- mock 数据源在特定延迟后抛错（延迟到块已 flush 后），验证边界段降级输出。
- 断言：HTTP 已 200 无法改状态码——错误只能段内降级，客户端 error boundary 接管。
- 多次访问稳定性：失败块的缓存策略（不缓存失败段）。
- 监控对齐：SSR 段错误埋点结构化（含流位置），测试断言埋点触发。

```javascript
test('流中错误段降级', async ({ request }) => {
  mockData('/api/reviews', { delayMs: 300, error: new Error('db down') });
  const html = await (await request.get('/goods/1')).text();
  expect(html).toContain('skeleton-reviews');   // 该段 fallback
  expect(html).toContain('goods-card');         // 其他段正常
});
r
```
