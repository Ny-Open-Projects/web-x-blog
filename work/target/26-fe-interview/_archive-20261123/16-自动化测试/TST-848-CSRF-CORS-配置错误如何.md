---
title: [TST-848] CSRF / CORS 配置错误如何用测试覆盖？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-848：CSRF / CORS 配置错误如何用测试覆盖？
**答**：
- 结论：CSRF/CORS 是配置问题，测试要「主动构造跨域/跨站请求」验证服务端是否正确拒绝——不能只看前端代码。
- CSRF 测试：构造不带 token 的跨站 POST 请求，验证被拒绝；带有效 token 才通过；检查 SameSite Cookie 属性。
- CORS 测试：用恶意 Origin 发请求，验证 Access-Control-Allow-Origin 不是 '*'（带凭证时）且不在白名单外；预检 OPTIONS 行为正确。
- 自动化：在接口测试套件里加「安全用例」，伪造 Origin/Referer 头断言响应头与状态码。
- 追问钩子：CORS 配成 '*' 但接口不带 Cookie，还算漏洞吗？如何判断风险等级？

```javascript
// CORS 配置错误检测：伪造恶意 Origin
async function checkCORS(fetch, url) {
  const resp = await fetch(url, { headers: { Origin: 'https://evil.example' } });
  const allow = resp.headers.get('Access-Control-Allow-Origin');
  const creds = resp.headers.get('Access-Control-Allow-Credentials');
  return {
    reflected: allow === 'https://evil.example',
    wildcardWithCreds: allow === '*' && creds === 'true',
    safe: allow !== 'https://evil.example' && !(allow === '*' && creds === 'true'),
  };
}
// 期望：恶意 Origin 不被反射，且 wildcard+credentials 不同时出现
checkCORS(mockFetch, '/api/user').then(console.log);
```
