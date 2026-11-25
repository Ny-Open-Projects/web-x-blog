---
title: [TST-274] 服务端状态序列化到客户端（__INITIAL_STATE）的测试要点？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-274：服务端状态序列化到客户端（__INITIAL_STATE）的测试要点？
**答**：
- 序列化安全：状态中含 </script> 字符串时需转义（防 XSS 断言）。
- 体积预算：初始状态大小断言（> 200KB 告警，防整页数据下发）。
- 循环引用/不可序列化值在开发期即失败（fail-fast 测试）。
- 客户端反序列化后与服务端状态深度相等（对账断言）。

```javascript
test('初始状态安全与一致', async ({ request }) => {
  const html = await (await request.get('/page-with-state')).text();
  expect(html).not.toMatch(/<\/script>\s*<script>alert/);   // 转义
  const state = extractState(html);
  expect(state.goods.title).toBe('X<Y');
});
r
```
