---
title: [PER-1025] 资源压缩与传输优化的取舍：br/zstd/gzip 如何选
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1025：资源压缩与传输优化的取舍：br/zstd/gzip 如何选

**答**：
- 压缩率：zstd ≈ brotli > gzip；brotli 浏览器支持广（需要 HTTPS），zstd 新兴且编解码都快。
- 取舍核心：压缩级别与 CPU 成本——静态资源预压缩（构建期生成 .br/.gz）随便用高级别；动态响应只能在线压缩，级别要保守。
- 正确配置：Accept-Encoding 协商、可压缩类型白名单（文本类），图片/视频本身已压缩不再二次压缩。
- 体积与速度：同级别下 brotli 比 gzip 再省 15%~20% 传输量，首屏 JS 收益直接体现在下载时间。

```javascript
// 构建期预压缩脚本
import { gzipSync, constants } from 'node:zlib';
import { brotliCompressSync } from 'node:zlib';
import fs from 'node:fs';
function precompress(dir) {
  for (const f of fs.readdirSync(dir)) {
    if (!/\.(js|css|html|svg)$/.test(f)) continue;
    const buf = fs.readFileSync(`${dir}/${f}`);
    fs.writeFileSync(`${dir}/${f}.gz`, gzipSync(buf, { level: 9 }));
    fs.writeFileSync(`${dir}/${f}.br`, brotliCompressSync(buf, {
      params: { [constants.BROTLI_PARAM_QUALITY]: 11 } }));   // 静态资源最高级
  }
}
// 服务端按 Accept-Encoding 返回 .br/.gz，CPU 零成本
```
