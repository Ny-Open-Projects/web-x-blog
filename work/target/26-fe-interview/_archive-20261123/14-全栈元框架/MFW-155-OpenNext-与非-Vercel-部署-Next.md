---
title: [MFW-155] OpenNext 是什么？怎么把 Next.js 部署到非 Vercel 平台？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-155：OpenNext 是什么？怎么把 Next.js 部署到非 Vercel 平台？
**答**：
- Next 的运行时行为（ISR 再验证、Image 优化、Cache API、Middleware）深耦合 Vercel 基础设施；OpenNext 是社区适配层：把 Next 的 server 产物转换为目标平台的格式（AWS Lambda/SST、Cloudflare Workers、Netlify 等），尽量还原语义。
- 已知语义损耗要心里有数：ISR/按需 revalidate 用平台 KV 模拟（有最终一致延迟）、`Cache-Control` 行为有差异、某些 next/image 优化管道需自建 loader；`unstable_*` API 支持不全。
- 自托管备选：Docker standalone（行为 100% 还原、自己管扩缩容）、Cloudflare adapter（边缘全球但语义损耗最多）。选型 = 语义还原度 vs 运维成本 vs 延迟分布。
- 生产建议：非 Vercel 部署后必须补一套「缓存一致性 + 监控」自测（revalidateTag 生效性、ISR stale 时长、Web Vitals 基线）。

```js
// OpenNext Cloudflare adapter 示例
// open-next.config.ts
import { defineCloudflareConfig } from '@opennextjs/cloudflare';
import kvIncrementalCache from './incremental-cache';

export default defineCloudflareConfig({
  incrementalCache: kvIncrementalCache, // ISR 页面缓存用 Workers KV 模拟
  // queue: ...                          // revalidate 队列（DO/Queue）
});
```

```json
// wrangler.jsonc
// {
//   "name": "next-on-cf",
//   "main": ".open-next/worker.js",
//   "assets": { "directory": ".open-next/assets", "binding": "ASSETS" },
//   "kv_namespaces": [{ "binding": "NEXT_INC_CACHE_KV", "id": "..." }]
// }
// 部署：npm run build && open-next-cloudflare && wrangler deploy
```

```bash
# 自托管对照：Docker standalone（语义 100% 还原）
# docker build -t next-app . && docker run -p 3000:3000 next-app
# k8s Deployment 探针：GET /api/health -> 200
```
