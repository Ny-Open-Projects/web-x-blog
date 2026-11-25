---
title: [WEB-304] HSTS 是什么？max-age 和 preload 各起什么作用？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-304：HSTS 是什么？max-age 和 preload 各起什么作用？
**答**：
- HSTS（Strict-Transport-Security）让浏览器记住"该域名必须用 HTTPS"，期间用户输入 http:// 也内部转 https，拒绝无效证书且不给"继续访问"按钮。
- max-age 是记住时长；includeSubDomains 覆盖子域；preload 申请进入浏览器内置列表，首次访问前就强制 HTTPS（否则第一次请求仍可被劫持）。
- 上线姿势：先短 max-age 观察，确认全站（含子域）HTTPS 后再延长时间、最后才申请 preload（退出成本极高）。

```javascript
// 响应头：Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
const hsts = { maxAge: 31536000, subdomains: true, preload: true };
function visit(url, hsts) {
  const isHttps = url.startsWith('https://');
  if (!isHttps && hsts.maxAge > 0) return { url: url.replace('http', 'https'), forced: true };
  return { url, forced: false };
}
console.log(visit('http://example.com/a', hsts));
```
