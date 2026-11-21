---
title: [RBL-170] 产物上传与 sourcemap 处理：怎么不拖慢构建主流程
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-170：产物上传与 sourcemap 处理：怎么不拖慢构建主流程

**答**：
- 问题：产物上传（CDN/对象存储）+ sourcemap 上报（监控平台）是 IO 密集，串在主流程里会显著拉长 CI 时长，尤其 map 文件可达产物 2~5 倍体积。
- 解耦：构建 job 只产出 dist 并 upload-artifact；上传 CDN、上报 sourcemap 用独立下游 job 并行跑（needs: build），失败可重试不阻塞主流程结论。
- sourcemap 策略：生产 map 不进 CDN 公网目录（安全），单独传监控平台并打 release 标；版本号 = 构建指纹（RBL-165），保证 map 与 chunk 对齐。
- 并行化上传：分批并发上传（限流 p-limit），大目录先压缩（tar+zstd）再传。
- 追问钩子：sourcemap 泄露是安全题（源码可还原），要能顺带答"公网 404 校验 map 路径 + Referer 控制或干脆不部署 map"。

```javascript
// scripts/upload-artifacts.mjs —— 下游 job：并发上传 + map 分离
import { readdirSync, readFileSync } from 'node:fs';
import { join, extname } from 'node:path';
import pLimit from 'p-limit';

const dist = 'apps/web/dist';
const limit = pLimit(8); // 并发限流，防止打爆 CDN 接口

async function upload(file, url) {
  const r = await fetch(url, { method: 'PUT', body: readFileSync(file),
    headers: { authorization: `Bearer ${process.env.UPLOAD_TOKEN}` } });
  if (!r.ok) throw new Error(`${file}: ${r.status}`);
}
const files = readdirSync(dist, { recursive: true }).map(f => join(dist, f));
const chunks = files.filter(f => extname(f) !== '.map');
const maps = files.filter(f => extname(f) === '.map');

const cdnBase = `${process.env.CDN_URL}/${process.env.RELEASE}`;
await Promise.all(chunks.map(f => limit(() => upload(f, `${cdnBase}/${f.slice(dist.length + 1)}`))));
await Promise.all(maps.map(f => limit(() => upload(f, `${process.env.SENTRY_URL}/${f.slice(dist.length + 1)}`))));
console.log(`chunks=${chunks.length} maps=${maps.length} release=${process.env.RELEASE}`);
```
