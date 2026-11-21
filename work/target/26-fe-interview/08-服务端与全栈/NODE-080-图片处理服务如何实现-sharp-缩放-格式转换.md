---
title: [NODE-080] 图片处理服务如何实现（sharp 缩放、格式转换、水印）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-080：图片处理服务如何实现（sharp 缩放、格式转换、水印）？
**答**：
- sharp 基于 libvips（C），性能远超 ImageMagick，**部分操作走线程池**（zlib/编码），CPU 密集场景要限并发（p-limit）防止打满。
- URL 即参数设计：`/img/{fileId}?w=200&h=200&fit=cover&fmt=webp&q=80`——网关鉴权 + 参数白名单 + sharp 处理 + **强缓存头**（内容寻址，处理结果不变）+ CDN 缓存派生图。
- 安全：限制输入大小（zip 炸弹/解压炸弹）、禁止超大分辨率（像素上限）、只允许白名单格式；处理结果落 OSS 后 301/302 重定向，避免服务反复计算。

```javascript
const sharp = require('sharp');
const pLimit = require('p-limit');
const limit = pLimit(8);   // 隔离舱：最多 8 个并发图片处理（防 CPU 打满）

// 参数白名单
const PARAMS_SCHEMA = {
  w: { type: 'int', max: 4096 }, h: { type: 'int', max: 4096 },
  fit: { enum: ['cover', 'contain', 'inside'] },
  fmt: { enum: ['webp', 'avif', 'jpeg', 'png'] },
  q: { type: 'int', min: 10, max: 100 },
};

router.get('/img/:fileId', async (ctx) => {
  const params = sanitize(ctx.query, PARAMS_SCHEMA);        // 非法参数直接 400
  const cacheKey = `img:${ctx.params.fileId}:${JSON.stringify(params)}`;

  // 1. 派生图缓存：同参数直接命中 OSS/Redis
  const cached = await redis.get(cacheKey);
  if (cached) { ctx.redirect(302, cached); return; }

  const source = await ossDownload(`${ctx.params.fileId}.png`);
  const pipeline = sharp(source, { limitInputPixels: 10000 * 10000 })  // 防解压炸弹
    .resize(params.w ?? null, params.h ?? null, { fit: params.fit ?? 'cover', withoutEnlargement: true });

  const format = params.fmt ?? 'webp';
  const buf = await limit(() =>
    pipeline.toFormat(format, { quality: params.q ?? 80 }).toBuffer()); // 受限并发

  const url = await ossUploadBuffer(buf, cacheKey, { contentType: `image/${format}` });
  await redis.setex(cacheKey, 86400 * 7, url);
  ctx.type = `image/${format}`;
  ctx.body = buf;
});

// 水印：合成一层
async function addWatermark(inputBuf) {
  const wm = Buffer.from(`<svg width="200" height="40">
    <text x="10" y="28" font-size="24" fill="rgba(255,255,255,0.6)">@ example.com</text></svg>`);
  return sharp(inputBuf)
    .composite([{ input: wm, gravity: 'southeast' }])
    .toBuffer();
}
```
