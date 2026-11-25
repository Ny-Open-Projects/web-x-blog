---
title: [PER-311] SRI 能覆盖动态 import 与 preload 吗？模块图完整性怎么做才不漏？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-311：SRI 能覆盖动态 import 与 preload 吗？模块图完整性怎么做才不漏？

**答**：
- 覆盖现状：`<script type=module src integrity>` 支持；`<link rel=preload as=script integrity>` 支持；**运行时动态 `import()` 的 chunk**——现代 Chrome/Firefox 支持对动态 import 应用 integrity 的前提是请求"可枚举"，实际上浏览器无法预知动态 URL，标准做法是**配合 importmap / 构建器注入**：把每个 chunk 的 URL+integrity 静态写入 manifest，动态 import 走封装函数查表补 integrity（fetch + Blob 或 importmap preload）。
- 漏洞形态：入口 script 有 integrity 但动态 chunk 没有任何校验 → 攻击者篡改 CDN 上的某个 lazy chunk 一样能执行任意代码——"只保护入口"是伪防护。
- 工程方案：构建期生成 `chunk-integrity.json`（构建器插件自动产出），运行时 loader：`dynamicImportWithSRI(chunkName)` 查表拿 integrity，用 `fetch(url, {integrity})` 校验后经 `URL.createObjectURL(blob)` 交给 import——校验发生在执行前。注意 blob import 会丢失相对 import 上下文，复杂模块图建议直接用 CSP（strict-dynamic + 信任链）与"CDN 独立域 + 探活"双保险。
- 取舍结论：SRI 管静态可枚举资源，动态模块图以"构建期完整性清单 + CDN 探活 + CSP 兜底"组合覆盖，单一手段都不完整。

```javascript
// 构建期产物 chunk-integrity.json：
// { "chunkA.9f2.js": "sha384-AAA...", "chunkB.1d7.js": "sha384-BBB..." }
const manifest = await fetch('/chunk-integrity.json').then(r => r.json());

async function dynamicImportWithSRI(chunkUrl) {
  const integrity = manifest[chunkUrl.split('/').pop()];
  if (!integrity) throw new Error(`chunk 不在完整性清单: ${chunkUrl}`);   // 白名单外拒绝
  const res = await fetch(chunkUrl, { integrity, cache: 'force-cache' });
  const blobUrl = URL.createObjectURL(await res.blob());
  try { return await import(blobUrl); }
  finally { URL.revokeObjectURL(blobUrl); }
}
// 取舍说明：blob import 对含相对 import 的复杂模块图不友好；
// 工程上常退化为：动态 import 不拦（走 CSP strict-dynamic），但 chunk-integrity.json 用于 CDN 探活与监控对账
```
