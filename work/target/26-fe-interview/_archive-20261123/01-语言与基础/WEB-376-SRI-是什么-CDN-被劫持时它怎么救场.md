---
title: [WEB-376] SRI 是什么？CDN 被劫持时它怎么救场？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-376：SRI 是什么？CDN 被劫持时它怎么救场？
**答**：
- Subresource Integrity：script/link 带 integrity="sha384-xxx"，浏览器下载后校验哈希，不符即拒绝执行——CDN 或代理被篡改内容直接失效。
- 注意：integrity 只适用于静态资源，且 CDN 内容更新时 hash 必须同步；跨域资源需 crossorigin 属性。
- 组合拳：SRI + CSP（限定来源域名）+ HTTPS，三层兜住第三方脚本供应链。

```javascript
<script src="https://cdn.example.com/vue.js"
  integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwET8j"
  crossorigin="anonymous"></script>
// CDN 被注入 1 字节 → hash 不匹配 → 拒绝执行
const verify = (content, expected) => sha384(content) === expected;
console.log('SRI = 对第三方脚本的内容级校验');
```
