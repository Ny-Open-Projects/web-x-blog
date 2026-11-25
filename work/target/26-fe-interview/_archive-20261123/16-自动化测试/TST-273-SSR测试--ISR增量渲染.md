---
title: [TST-273] ISR/增量再生的测试设计？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-273：ISR/增量再生的测试设计？
**答**：
- 再生触发：revalidate 到期后下次请求触发后台再生（首请求回旧、二请求得新）。
- on-demand revalidation：管理接口触发后立即生效（secret 校验）。
- 再生失败保留旧内容（stale-while-error）断言。
- 缓存键与路径参数（fallback 阻塞模式）行为：首访阻塞生成 vs 返回骨架。

```javascript
test('按需再生', async ({ request }) => {
  await request.post(`/api/revalidate?path=/goods/1&secret=${SECRET}`);
  const html = await (await request.get('/goods/1')).text();
  expect(html).toContain('更新后的标题');
});
r
```
