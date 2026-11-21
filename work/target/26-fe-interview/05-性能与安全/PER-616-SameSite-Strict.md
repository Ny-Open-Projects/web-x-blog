---
title: [PER-616] SameSite=Strict/Lax 在真实业务里为什么经常配了但没用？排查思路是什么？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-616：SameSite=Strict/Lax 在真实业务里为什么经常配了但没用？排查思路是什么？

**答**：
- 常见失效原因：**页面跳转发起的顶级导航 GET**（Lax 放行链接跳转的顶级 GET，攻击用 `a href` 就能带 cookie）、**cookie 属性被后端覆盖**（网关/框架重新 Set-Cookie 没带 SameSite）、**旧浏览器忽略 SameSite**（需 CSRF Token 双保险）、**子域 cookie 冲突**（domain=.example.com 的 cookie 在任何子域都带）、**SameParty/第三方上下文**（iframe 里全是 cross-site，Lax 也不带）。
- 排查路径：DevTools Application 面板看 cookie 实际属性（是否真写上了）-> 网络面板看跨站请求的 Cookie 头是否携带（实测而不是推理）-> 分场景测试（顶级导航 GET / iframe 内 XHR / form POST）-> 检查响应的 Set-Cookie 链路是否有中间层覆盖。
- 结论：SameSite 是纵深一层不是唯一防线，CSRF Token 必须并存；对链接跳转 GET 带副作用的接口（点赞/关注用 GET）要改成 POST，这是业务侧最常见的洞。

```javascript

// 排查清单脚本化：分场景验证 SameSite 是否生效
async function sameSiteAudit(targetUrl, actionUrl) {
  const scenarios = [
    { name: '顶级导航 GET（Lax 放行）', how: () => location.href = actionUrl, expect: '带 cookie' },
    { name: 'iframe 内 XHR（cross-site）', how: () => fetch(actionUrl, { mode: 'no-cors' }), expect: 'Lax 不带' },
    { name: 'form POST', how: () => submitForm(actionUrl), expect: 'Lax 不带' },
  ];
  for (const s of scenarios) {
    // 在攻击者域（测试环境）的页面里执行 how()，抓包看 Cookie 头
    console.log(s.name, '->', await captureCookieHeader(targetUrl, s.how),
      '期望:', s.expect);
  }
  // DevTools 检查项：
  // 1) Application > Cookies: SameSite 属性是否真的存在（防网关覆盖）
  // 2) Set-Cookie 响应链：网关/框架是否重写丢失 SameSite
  // 3) domain 是否过宽（.example.com 导致子域全带）
}
```
