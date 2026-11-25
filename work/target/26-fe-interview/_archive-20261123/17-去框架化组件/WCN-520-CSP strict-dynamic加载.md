---
title: [WCN-520] 企业安全合规：WCN 组件在 CSP strict-dynamic 下的加载策略与 nonce 传递怎么做？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-520：企业安全合规：WCN 组件在 CSP strict-dynamic 下的加载策略与 nonce 传递怎么做？

**答**：
- 结论：strict-dynamic 下白名单 URL 失效，靠 nonce/hash 授信启动脚本，后续动态 import 自动继承信任。
- 入口 script 带服务端下发的 nonce（每次请求唯一），动态 import 的元素 chunk 由已被信任脚本发起，无需再带 nonce。
- 样式：adoptedStyleSheets 内联规避 style-src 外链限制；如用 <link> 需带 nonce。
- 追问：nonce 泄露风险如何控制？（答：一次性、短时效、与响应绑定，不缓存 HTML）

```javascript
// 服务端渲染：每次请求生成新 nonce
const nonce = crypto.randomBytes(16).toString('base64');
res.setHeader('Content-Security-Policy',
  `script-src 'strict-dynamic' 'nonce-${nonce}'; object-src 'none'`);
res.end(`<script nonce="${nonce}" type="module">
  import('https://cdn/ds/v3/core.js').then(m => m.bootstrap());
</script>`);
// 由带 nonce 的脚本发起的 import 自动受信，chunk 无需 nonce

// nonce 必须来自服务端且每次响应唯一，切勿缓存 HTML
res.setHeader('Cache-Control', 'no-store');
```
