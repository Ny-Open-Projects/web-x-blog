---
title: [MFW-899] 构建产物完整性怎么防缓存投毒（SRI 与哈希校验）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-899：构建产物完整性怎么防缓存投毒（SRI 与哈希校验）

**答**：
- 结论：产物若被 CDN 或构建链篡改会造成投毒；用子资源完整性（SRI）为每个产物生成哈希并写入 HTML，浏览器加载时校验，不匹配则拒绝执行。
- 落地：构建期为 bundle 生成 integrity 哈希，引用处加 integrity + crossorigin；配合确定性构建让哈希可预先固化。
- 追问钩子：动态内容（如个性化脚本）能用 SRI 吗？——不能，SRI 要求内容固定；动态脚本靠 CSP + 签名而非 SRI。

```javascript
// 构建期：为产物生成 SRI
function sri(content) {
  const h = crypto.createHash('sha384').update(content).digest('base64');
  return 'sha384-' + h;
}
function renderScriptTag(src, content) {
  return `<script src="${src}" integrity="${sri(content)}" crossorigin="anonymous"></script>`;
}
// HTML 中引用带 integrity：浏览器校验哈希，不符则不执行
// <script src="/a.8f3.js" integrity="sha384-..." crossorigin="anonymous">
// 配合确定性构建：同一源码 → 相同哈希 → integrity 可安全固化
```
