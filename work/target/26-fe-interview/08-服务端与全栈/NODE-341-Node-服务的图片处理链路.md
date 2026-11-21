---
title: [NODE-341] Node 服务的图片处理链路（缩略图/水印/格式）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-341：Node 服务的图片处理链路
**答**:
- 架构选择：能不自己算就不算——云存储内置处理参数（OSS x-oss-process / CDN 图像处理）按需实时生成 + 缓存；自建用 sharp（libvips，多线程，比 ImageMagick 快数倍）在 Worker/独立服务跑，不占请求进程。
- 预生成 vs 实时生成：固定尺寸列表（封面 3 档）预生成（上传时异步任务）；任意尺寸场景实时生成 + CDN 缓存首次结果；参数白名单（防任意参数打爆 CPU：尺寸上限/格式白名单）。
- 格式策略：源图保留原图，分发按 Accept 协商（AVIF/WebP 优先，JPEG 兜底）；渐进式 JPEG 与占位（LQIP base64 内联）。
- 水印与安全：EXIF 剥离（GPS 隐私）、用户水印叠加、上传时图片炸弹防护（解压后尺寸上限检测）。
- 可观测：处理耗时分布、CDN 命中率、各格式占比（AVIF 覆盖率）。
```javascript
// sharp 处理流水线（Worker 内）
const sharp = require('sharp');
async function processImage(buf, { w, h, fmt = 'webp', watermark }) {
  const img = sharp(buf, { limitInputPixels: 1e8 })            // 图片炸弹防护
    .resize(w, h, { fit: 'cover', withoutEnlargement: true })
    .toFormat(fmt, { quality: 80, effort: 4 });
  if (watermark) img.composite([{ input: wmBuf, gravity: 'southeast', blend: 'over' }]);
  return img.toBuffer();
}
```
