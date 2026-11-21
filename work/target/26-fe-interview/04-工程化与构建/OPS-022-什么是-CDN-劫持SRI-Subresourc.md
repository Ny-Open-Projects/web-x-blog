---
title: [OPS-022] 什么是 CDN 劫持？SRI（Subresource Integrity）怎么防？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-022：什么是 CDN 劫持？SRI（Subresource Integrity）怎么防？
**答**：
- 劫持：中间节点（不规范的 ISP 缓存/恶意代理）篡改返回的 JS 内容，插入广告或窃取数据，特征是代码在源站不存在。
- SRI：给 script/link 加 integrity 属性（内容 hash），浏览器校验失败直接拒绝执行，从客户端兜底防篡改。
- 构建期用 webpack/vite 插件自动给产物注入 integrity，注意版本更新后 hash 会变，html 与 SRI 要同源发布。
- SRI 会让"CDN 回源重新压缩"类操作失败，要求 CDN 对该资源原样返回；同时配合 CSP report-uri 上报被篡改的样本。

```javascript
// build/sri-loader.js：构建后为 index.html 注入 SRI，并提供运行时被劫持上报
import { createHash } from 'node:crypto';
import { readFileSync, writeFileSync } from 'node:fs';

function sri(file) {
  const buf = readFileSync(file);
  const b64 = createHash('sha384').update(buf).digest('base64');
  return `sha384-${b64}`;
}

// 构建后处理：index.html 中本地 script 注入 integrity + crossorigin
export function injectSri(distDir) {
  let html = readFileSync(`${distDir}/index.html`, 'utf8');
  html = html.replace(/<script src="(\/assets\/[^"]+\.js)"/g, (_, p) => {
    const hash = sri(`${distDir}${p}`);
    return `<script src="${p}" integrity="${hash}" crossorigin="anonymous"`;
  });
  writeFileSync(`${distDir}/index.html`, html);
  console.log('SRI injected');
}

// 运行时：脚本加载失败时区分被篡改与网络问题，上报样本用于追责
export function reportIntegrityFailure() {
  window.addEventListener('error', (e) => {
    const el = e.target;
    if (el?.tagName === 'SCRIPT' && el.integrity) {
      // eslint-disable-next-line no-new-func
      fetch(el.src).then(r => r.text()).then(body => {
        navigator.sendBeacon('/report/hijack', JSON.stringify({
          src: el.src, sample: body.slice(0, 500),
        }));
      }).catch(() => {});
    }
  }, true);
}
```
