---
title: [TST-269] SSR 特有的安全问题测试（注入/数据泄漏）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-269：SSR 特有的安全问题测试（注入/数据泄漏）？
**答**：
- XSS：服务端插入用户数据必须转义——测试用含 <script> 的数据验证输出已转义。
- 数据泄漏：服务端获取的全量数据不应整包序列化到 window.__INITIAL__（只下发页面所需）。
- 注入头/cookie：SSR 直接拼 header 的位置做注入测试。
- CSRF 与双端会话：服务端渲染的表单 token 正确下发与校验。

```javascript
test('服务端转义', async ({ request }) => {
  await createGoods({ name: '<script>alert(1)</script>商品' });
  const html = await (await request.get(`/goods/${id}`)).text();
  expect(html).not.toContain('<script>alert(1)</script>');   // 已转义
  expect(html).toContain('&lt;script&gt;');
});
r
```
