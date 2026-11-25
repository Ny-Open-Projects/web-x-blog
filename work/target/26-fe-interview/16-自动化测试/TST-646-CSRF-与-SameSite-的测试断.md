---
title: [TST-646] CSRF 与 SameSite 的测试断言怎么设计？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-646：CSRF 与 SameSite 的测试断言怎么设计？

**答**：
- 结论：从「跨站能否带上凭证并发起状态变更」入手——断言无 token 的请求被拒、SameSite=Lax/Strict 下跨站不携带 Cookie。
- 用两个不同源的页面模拟攻击：A 站表单 POST 到 B 站，检查 B 站是否拒绝。
- 同时测 token 缺失、过期、复用三种失败路径。
- 追问钩子：SameSite=None 的第三方嵌入场景，你怎么防 CSRF？

```javascript
function csrfChecks(client) {
  return [
    { name: 'no-token', run: () => client.post('/transfer', { amount: 1 }),
      expect: 403 },
    { name: 'expired-token', run: () => client.post('/transfer',
      { token: 'expired' }), expect: 403 },
    { name: 'same-site-lax', run: () => client.crossSitePost('/transfer'),
      expect: 401 },
  ];
}
async function runChecks(checks) {
  const out = [];
  for (const c of checks) {
    const res = await c.run();
    out.push({ name: c.name, ok: res.status === c.expect });
  }
  return out;
}
```
