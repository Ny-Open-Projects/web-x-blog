---
title: [RBL-186] 笔试：手写构建产物 manifest 生成器（含缓存复用校验）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-186：笔试：手写构建产物 manifest 生成器（含缓存复用完整性校验）

**题目**：写 gen-manifest.mjs：1) 扫描 dist 目录（递归）；2) 生成 manifest：每个文件记录 {path, size, gzipSize, hash(sha256 前 16)}，含 HTML 内引用的资源关联（script/link 标签解析）；3) 输出 manifest.json 按 path 排序；4) 提供 verify(manifest, dist)：校验 manifest 与实际目录一致（无缺文件、hash 对上），缓存恢复场景用（防"缓存命中但产物目录不完整"）；5) HTML 引用缺失资源（引用了不存在的 chunk）要报错。

```javascript
// gen-manifest.mjs
import { createHash } from 'node:crypto';
import { readdirSync, readFileSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';
import { gzipSync } from 'node:zlib';

export function buildManifest(dist) {
  const files = [];
  (function walk(dir) {
    for (const e of readdirSync(dir, { withFileTypes: true })) {
      const p = join(dir, e.name);
      if (e.isDirectory()) walk(p);
      else {
        const raw = readFileSync(p);
        files.push({
          path: relative(dist, p).split('\\').join('/'),
          size: raw.length,
          gzipSize: gzipSync(raw, { level: 6 }).length,
          hash: createHash('sha256').update(raw).digest('hex').slice(0, 16),
        });
      }
    }
  })(dist);
  files.sort((a, b) => a.path.localeCompare(b.path));

  // HTML 引用完整性：script/link src 必须存在于 manifest
  const paths = new Set(files.map(f => f.path));
  for (const f of files.filter(f => f.path.endsWith('.html'))) {
    const html = readFileSync(join(dist, f.path), 'utf8');
    for (const m of html.matchAll(/(?:src|href)="([^"]+\.(?:js|css))"/g)) {
      if (!paths.has(m[1].replace(/^\.?\//, '')))
        throw new Error(`HTML 引用缺失: ${m[1]} (in ${f.path})`); // 缓存半恢复典型症状
    }
  }
  return files;
}

export function verify(manifest, dist) {
  const errs = [];
  const seen = new Set(buildManifest(dist).map(f => f.path)); // 重扫目录比对
  for (const f of manifest) {
    if (!seen.has(f.path)) { errs.push(`missing: ${f.path}`); continue; }
    const raw = readFileSync(join(dist, f.path));
    const h = createHash('sha256').update(raw).digest('hex').slice(0, 16);
    if (h !== f.hash) errs.push(`hash mismatch: ${f.path}`);
  }
  return { ok: errs.length === 0, errs };
}
```
**评分点**：
- 三元数据齐全：size/gzip/hash（hash 用于完整性校验）。
- HTML 引用完整性校验（缓存恢复不完整的典型检测点）。
- verify 双向：manifest 里的都在目录 + hash 一致。
- gzip 真实计算 level 6（与 CDN 大致一致）。
- 排序稳定保证 manifest 可 diff。
