---
title: [TST-275] 流式 SSR 下 SEO（爬虫拿不全内容）的测试与保障？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-275：流式 SSR 下 SEO（爬虫拿不全内容）的测试与保障？
**答**：
- 爬虫 UA 分流：对 bot 返回完整等待渲染（或动态渲染）而非流式骨架——UA 模拟测试。
- 关键内容必须在「无 JS 纯 HTML」中可获取——curl 快照断言核心字段。
- 流式超时上限：爬虫等待窗口内（如 5s）关键块必须到达——延迟预算断言。
- 监控真实爬虫抓取成功率（Search Console/日志）作为线上回归信号。

```javascript
test('爬虫可获取完整内容', async ({ request }) => {
  const res = await request.get('/goods/1', { headers: { 'user-agent': 'Googlebot' } });
  const html = await res.text();
  expect(html).toContain('商品核心标题');          // bot 路径非骨架
});
r
```
