---
title: [TST-264] SSR 阶段错误的测试（数据失败/组件抛错）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-264：SSR 阶段错误的测试（数据失败/组件抛错）？
**答**：
- 数据层失败：服务端 fetch 抛错时页面返回降级壳 + 状态码策略（503 或 200+客户端重试）。
- 组件级失败：SSR render 抛错不应拖垮整个响应（分段渲染时只影响该段）。
- 错误日志断言：SSR 错误被结构化捕获上报（含组件栈），不是裸 500。
- 重试与缓存：失败页短 TTL 缓存避免雪崩，恢复后自动恢复——集成测试验证。

```javascript
test('SSR 数据失败降级', async ({ request }) => {
  const res = await request.get('/product/404-page');
  expect(res.status()).toBe(200);                    // 降级壳而非 500
  expect(await res.text()).toContain('加载失败，请重试');
});
r
```
