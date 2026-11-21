---
title: [WCN-195] 笔试：手写组件产物体积分析器（按 tag 汇总 gzip 体积 + 预算判定）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-195：笔试：手写组件产物体积分析器

**题目**：Node 脚本：① 扫描 `dist/**/*.js`（组件产物命名 `{tag}.js`）；② 计算每个文件的 raw 与 gzip 体积；③ 解析产物中的 import 语句，统计共享依赖被几个组件引用；④ 生成报告：按 gzip 排序的组件表 + 超预算组件（单组件 >8KB）+ 共享依赖体积摊销表；⑤ 输出 exit code：超预算非零（CI 阻断）。

**答**：

```javascript
// analyze-size.mjs
import { glob } from 'node:fs/promises';
import { gzipSync } from 'node:zlib';
import { readFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';

const BUDGET = 8 * 1024;
const SHARED = new Set(['signals-core', 'lit', 'runtime']);

const rows = [];
const sharedRefs = new Map();   // 依赖名 -> Set<组件>

for await (const file of glob('dist/**/*.js')) {
  const raw = readFileSync(file);
  const gzip = gzipSync(raw).length;
  const tag = file.split('/').pop().replace(/\.js$/, '');
  const code = raw.toString();
  for (const m of code.matchAll(/from\s+['"]([^'"]+)['"]/g)) {
    const dep = m[1];
    if (SHARED.has(dep)) {
      if (!sharedRefs.has(dep)) sharedRefs.set(dep, new Set());
      sharedRefs.get(dep).add(tag);
    }
  }
  rows.push({ tag, raw: raw.length, gzip, over: gzip > BUDGET });
}

rows.sort((a, b) => b.gzip - a.gzip);
console.table(rows.map((r) => ({ tag: r.tag, gzip: `${(r.gzip / 1024).toFixed(1)}KB`,
  raw: `${(r.raw / 1024).toFixed(1)}KB`, budget: r.over ? 'OVER' : 'ok' })));

for (const [dep, tags] of sharedRefs) {
  console.log(`${dep}: 被 ${tags.size} 个组件引用（体积摊销 ${(SHARED_SIZE[dep] / tags.size / 1024).toFixed(1)}KB/组件）`);
}

const over = rows.filter((r) => r.over);
if (over.length) { console.error(`超预算组件: ${over.map((r) => r.tag).join(', ')}`); process.exit(1); }
```

**评分点**：
- gzip 体积口径（CDN 传输真实口径）与 raw 双列。
- import 解析统计共享依赖引用数 + 摊销计算（体积治理核心洞察）。
- 预算判定 + process.exit(1)（CI 阻断）。
- glob 扫描与 tag 提取约定一致。
