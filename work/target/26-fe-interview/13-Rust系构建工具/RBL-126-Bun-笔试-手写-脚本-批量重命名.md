---
title: [RBL-126] 笔试：手写 TS 构建辅助脚本（批量资源重命名 + manifest）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-126：笔试：手写 TS 构建辅助脚本（批量资源重命名 + manifest）
**题目**：用 Bun 写 rename-assets.ts：1) 扫描 dist/img 下所有 png/jpg；2) 计算内容 hash 前 8 位并重命名 name.<hash>.ext；3) 生成 manifest.json（原名→新名映射）；4) 幂等：已带 hash 的文件跳过；5) 空目录/无匹配文件时正常结束不报错。

```typescript
// rename-assets.ts —— bun rename-assets.ts
import { readdirSync, renameSync, writeFileSync } from 'node:fs';
import { join, extname, basename } from 'node:path';
import crypto from 'node:crypto';

const DIR = './dist/img';
const manifest: Record<string, string> = {};

if (!readdirSyncSafe(DIR)) {
  console.log('[assets] 目录不存在，跳过');
  process.exit(0);
}
function readdirSyncSafe(dir: string): string[] | null {
  try { return readdirSync(dir); } catch { return null; }
}

for (const name of readdirSyncSafe(DIR) ?? []) {
  if (!/\.(png|jpe?g)$/i.test(name)) continue;
  // 幂等：name.<8hex>.ext 已处理过则跳过
  if (/(\.[0-9a-f]{8})\.(png|jpe?g)$/i.test(name)) continue;

  const full = join(DIR, name);
  const hash = crypto.createHash('sha256')
    .update(await Bun.file(full).arrayBuffer())
    .digest('hex').slice(0, 8);
  const ext = extname(name);
  const newName = `${basename(name, ext)}.${hash}${ext}`;
  renameSync(full, join(DIR, newName));
  manifest[name] = newName;
}

writeFileSync(join(DIR, 'manifest.json'), JSON.stringify(manifest, null, 2));
console.log(`[assets] 重命名 ${Object.keys(manifest).length} 个文件`);
```
**评分点**：
- 幂等判定（已带 hash 跳过）。
- 目录不存在/空目录优雅退出（边界）。
- manifest 输出（供 HTML/CSS 引用替换）。
- hash 用内容而非文件名。
- Top-level await 直跑 TS（体现 bun 工具链特点）。
