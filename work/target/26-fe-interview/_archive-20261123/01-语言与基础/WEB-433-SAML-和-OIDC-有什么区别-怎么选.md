---
title: [WEB-433] SAML 和 OIDC 有什么区别，怎么选
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 鉴权]
type: 面试题
---

## WEB-433：SAML 和 OIDC 有什么区别，怎么选

**答**：
- SAML：基于 XML 的老协议，企业级 IdP（ADFS、SAP）广泛存在；断言用 XML 签名，报文重、调试痛苦
- OIDC：基于 JSON/JWT 的现代协议，移动端与 SPA 友好，SDK 生态成熟
- 选择逻辑：对接传统企业/政企客户（他们只有 SAML IdP）就用 SAML；自建或新型 SaaS 选 OIDC
- 网关层可做协议转换（SAML↔OIDC），让业务侧统一只接 OIDC，前端只认 access_token
- 前端关联：SAML 的断言经浏览器 POST 传递，回跳页常出现「页面刷新一次才登录」的现象，属于协议流程而非 bug

```javascript
// 协议转换后的前端统一处理：只看登录态，不关心背后是 SAML 还是 OIDC
const res = await fetch('/api/me', { credentials: 'include' });
if (res.status === 401) {
  const { loginUrl } = await res.json(); // 网关返回统一登录入口
  location.href = loginUrl;
}
```
