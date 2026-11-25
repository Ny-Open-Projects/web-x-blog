---
title: [NODE-097] 静态资源服务与 CDN 回源如何配合？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-097：静态资源服务与 CDN 回源如何配合？
**答**：
- 静态资源链路：浏览器 → CDN 边缘 →（未命中）回源 Node/对象存储。Node 侧职责：**正确的缓存头**（`Cache-Control: max-age` 决定 CDN 与浏览器缓存时长、`ETag` 协商）、**回源鉴权**（URL 签名防盗链）、`Vary` 正确设置。
- 缓存头策略：带 contenthash 的资源 `max-age=31536000, immutable`；`index.html` 必须 `no-cache`（每次协商，保证发版即生效）；接口按需 `private`。
- 回源细节：CDN 回源会带 `If-None-Match`，命中 304 省带宽；`stale-while-revalidate` 让发版瞬间用户仍拿旧资源不阻塞；大文件支持 Range（NODE-028）。

```javascript
// Node 作为 CDN 回源站
const IMMUTABLE = 'public, max-age=31536000, immutable';
const NO_CACHE = 'no-cache';

router.get('/static/*', async (ctx) => {
  const filePath = ctx.path.replace('/static/', '');
  // 1. 指纹资源判断：含 hash 才允许长缓存，index.html 强协商
  const isFingerprinted = /\.[0-9a-f]{8,}\.[a-z]+$/.test(filePath);
  ctx.set('cache-control', isFingerprinted ? IMMUTABLE : NO_CACHE);

  const stat = await fs.stat(path.join(PUBLIC_DIR, filePath)).catch(() => null);
  if (!stat) { ctx.status = 404; return; }

  // 2. 协商缓存：CDN 回源带 If-None-Match
  const etag = `"${stat.size}-${stat.mtimeMs}"`;
  ctx.set('etag', etag);
  if (ctx.get('if-none-match') === etag) { ctx.status = 304; return; }   // 304：CDN 直接用缓存

  // 3. 防盗链：回源请求带 CDN 签名（URL 签名在 CDN 配置，回源时验证）
  const sign = ctx.get('x-cdn-sign');
  if (PROTECTED_PATHS.some((p) => filePath.startsWith(p)) && !verifyCdnSign(sign, ctx.path)) {
    ctx.status = 403; return;
  }

  ctx.type = mime(path.extname(filePath));
  ctx.body = fs.createReadStream(path.join(PUBLIC_DIR, filePath));       // 流式回源
});

// 发版配合：构建产物文件名带 hash + HTML 引用新 hash
// app.3f8a2b.js（immutable 一年） ← index.html（no-cache 每次协商）
// 发版后：CDN 缓存 index.html 过期回源拿新 HTML → 新 HTML 引用新 hash 资源 → 未命中回源拉取
```
