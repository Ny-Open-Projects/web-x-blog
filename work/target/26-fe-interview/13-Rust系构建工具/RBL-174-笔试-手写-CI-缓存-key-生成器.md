---
title: [RBL-174] 笔试：手写 CI 缓存 key 生成器（lockfile + 源码 + 配置）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-174：笔试：手写 CI 缓存 key 生成器（lockfile + 源码 + 配置）

**答**：写 cache-key.mjs：1) 输入工作目录与配置（排除 glob、环境变量白名单）；2) 生成缓存 key：`{prefix}-{os}-{lockhash}-{srchash}-{version}`；3) lockhash = 所有 lock 文件内容 hash；srchash = 排除后源码文件的"相对路径+内容"排序 hash；4) 环境变量按白名单键名排序后加入 hash；5) 提供 --print-diff 模式：对比两个目录的 key 并输出首个造成差异的文件路径。

```javascript
// cache-key.mjs
import { createHash } from 'node:crypto';
import { readdirSync, readFileSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';

function collect(dir, ignores, base = dir, acc = []) {
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, e.name), rel = relative(base, p);
    if (ignores.some(g => rel.startsWith(g.replace('**/', '')))) continue; // 简化 glob 前缀匹配
    if (e.isDirectory()) collect(p, ignores, base, acc);
    else acc.push(rel);
  }
  return acc;
}
function hashFiles(dir, files, base) {
  const h = createHash('sha256');
  for (const rel of files.sort()) {
    h.update(rel); h.update('\0'); h.update(readFileSync(join(base, rel)));
  }
  return h.digest('hex').slice(0, 16);
}

export function cacheKey(root, { prefix = 'build', ignores = ['node_modules', 'dist'],
  envKeys = [], version = 'v1', lockfiles = ['pnpm-lock.yaml'] } = {}) {
  const all = collect(root, ignores);
  const lockH = hashFiles(root, lockfiles.filter(f => all.includes(f)), root);
  const srcH = hashFiles(root, all.filter(f => !lockfiles.includes(f)), root);
  const envH = createHash('sha256')
    .update(envKeys.sort().map(k => `${k}=${process.env[k] ?? ''}`).join('\n'))
    .digest('hex').slice(0, 8);
  return `${prefix}-${process.platform}-${lockH}-${srcH}-${envH}-${version}`;
}
console.log(cacheKey(process.argv[2] ?? '.'));
// --print-diff：分别对两个目录 collect 后按 rel 找到内容不同的第一个文件
// → 定位"为什么今天缓存全 miss"，输出该文件相对路径。
```
**评分点**：
- key 结构分段可定位（lock/src/env/version 分开，diff 才有信息量）。
- 排序保证遍历顺序稳定（跨机器 hash 一致）。
- 排除目录在收集阶段剪枝。
- env 白名单显式声明（隐藏输入进 hash 是事故源）。
- version 段支持一键 bump 全局失效。
