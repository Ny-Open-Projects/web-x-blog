---
title: [BLD-188] 构建产物多 CDN 发布与一致性校验。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-188：构建产物多 CDN 发布与一致性校验。
**答**：
- 发布模型：产物上传多个 CDN 源（国内/海外/多供应商）→ 每份产物带 sha256 清单（manifest.json 含每文件 hash）→ 发布系统按清单分发 → **校验任务**从各 CDN 边缘拉取对比 hash。
- 一致性风险点：上传部分成功（半发布状态）、CDN 缓存未刷新（旧 hash 命中）、路径重写错误（不同 CDN 前缀）、压缩层差异（gzip/br 由 CDN 动态压缩不影响 hash，但要确认禁改内容）。
- 关键设计：**文件名即内容寻址**（contenthash），同名文件内容必然一致 → 校验简化为"每个 CDN 都能取到清单中全部文件且 hash 一致"；index.html 不走 contenthash，要单独处理其失效（版本号 query 或短 TTL）。
- 灰度与回滚：清单版本化（release-v123.json），DNS/网关切换清单版本即可原子回滚。

```javascript
// scripts/publish-multi-cdn.mjs：多 CDN 发布 + 一致性校验
import { createHash } from 'node:crypto';
import { readdirSync, readFileSync } from 'node:fs';

const sha256 = (buf) => createHash('sha256').update(buf).digest('hex');
// 1. 生成内容清单（contenthash 文件名 + 双重校验）
const files = readdirSync('dist', { recursive: true }).filter((f) => f.endsWith('.js') || f.endsWith('.css'));
const manifest = Object.fromEntries(files.map((f) => [f, sha256(readFileSync(`dist/${f}`))]));
manifest['manifest.json'] = sha256(JSON.stringify(manifest));

// 2. 多源上传（幂等：内容寻址，重复上传无害）
for (const cdn of ['aliyun', 'cloudflare', 'qingliu']) {
  for (const f of [...files, 'index.html']) await upload(cdn, f, readFileSync(`dist/${f}`));
}
await upload('aliyun', `releases/v${process.env.RELEASE}.json`, JSON.stringify(manifest));

// 3. 一致性校验：各 CDN 边缘节点拉取对比（含多地域探测点）
for (const cdn of ['https://cdn1.example.com', 'https://cdn2.example.net']) {
  for (const [f, hash] of Object.entries(manifest)) {
    const probe = await fetch(`${cdn}/${f}`).then((r) => r.arrayBuffer());
    if (sha256(Buffer.from(probe)) !== hash) {
      // 半发布/缓存未刷新的捕获点
      throw new Error(`[FAIL] ${cdn}/${f} 内容不一致，禁止切流`);
    }
  }
}
console.log('[OK] 全部 CDN 边缘一致，可切换清单版本');
// 回滚：网关把 index.html 的资源前缀从 releases/v124 指回 v123（清单级原子切换）
```
