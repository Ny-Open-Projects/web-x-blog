---
title: [WEB-243] CDN 刷新与预热：发版后如何让用户立刻拿到新资源？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, CDN]
type: 面试题
---

## WEB-243：CDN 刷新与预热：发版后如何让用户立刻拿到新资源？

**答**：
- 刷新（purge）：清除边缘节点上的指定 URL/目录缓存，用户下次请求回源拿新内容。适合纠错、下架内容。
- 预热（prefetch/warm）：主动把新资源推到边缘节点，用户首次访问即命中。适合大促前预热热点文件。
- 最佳实践其实是「绕过刷新」：文件名带 content hash（非覆盖式），新版本就是新 URL，HTML 引用更新后天然全量生效，只需刷新 HTML 的缓存。
- 刷新配额：CDN 一般限制每日刷新条数，全量刷新目录代价高；预热大文件要提前（预热完才算完）。

```javascript
// 发版脚本（CI 中）
async function deploy() {
  await upload(`dist/app.${hash}.js`);            // 非覆盖上传新文件
  await cdn.refreshUrls([`${CDN}/index.html`]);   // 只刷新 HTML
  await cdn.prefetchUrls([`${CDN}/app.${hash}.js`, ...]); // 大促预热
}
```
