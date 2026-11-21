---
title: [WEB-366] CSRF token 的双提交 Cookie 模式是什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 笔试题
---

## WEB-366：CSRF token 的双提交 Cookie 模式是什么？
**答**：
- 前端从 Cookie 读出 csrf token（非 HttpOnly 的随机值），复制到请求头 X-CSRF-Token；服务端比较两者是否一致。
- 原理：攻击者站点读不到本站 Cookie（同源策略），无法同时改两个位置，二者不一致即拒绝。
- 前提：Cookie 本身未被 XSS 偷走；配合 SameSite=Lax 后双提交可简化；注意 token 不放 URL、不进日志。

```javascript
function getCookie(name) {
  return document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'))?.[1];
}
fetch('/api/transfer', {
  method: 'POST',
  headers: { 'X-CSRF-Token': getCookie('csrf') },   // 双提交
  credentials: 'include',
});
// 服务端: req.headers['x-csrf-token'] === req.cookies.csrf ? next() : 403
console.log('Cookie 读出 + Header 带上 + 服务端比对');
```

**评分点**：
- 结论先行，机制一句话讲透
- 覆盖攻击面/异常分支与边界条件
- 代码可运行、命名清晰、有防御性处理
- 主动给出工程取舍与常见坑
