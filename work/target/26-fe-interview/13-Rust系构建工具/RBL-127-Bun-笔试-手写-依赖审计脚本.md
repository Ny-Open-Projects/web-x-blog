---
title: [RBL-127] 笔试：手写依赖审计脚本（幽灵依赖检测）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-127：笔试：手写依赖审计脚本（幽灵依赖检测）
**题目**：写 audit-deps.ts：1) 扫描 src 下所有 import 语句提取裸导入包名；2) 读取 package.json 的 dependencies + devDependencies 声明集合；3) 报告「代码用了但未声明」的幽灵依赖；4) 报告「声明了但未使用」的死依赖；5) scope 包归并正确（@scope/name 取两段）。

```typescript
// audit-deps.ts
import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const pkg = JSON.parse(readFileSync('./package.json', 'utf8'));
const declared = new Set([
  ...Object.keys(pkg.dependencies ?? {}),
  ...Object.keys(pkg.devDependencies ?? {}),
]);
const used = new Set<string>();

function scan(dir: string) {
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) { if (e.name !== 'node_modules') scan(p); continue; }
    if (!/\.(ts|tsx|js|jsx)$/.test(e.name)) continue;
    const code = readFileSync(p, 'utf8');
    for (const m of code.matchAll(/(?:import[^'"]*from\s*|require\()\s*['"]([^'"]+)['"]/g)) {
      const spec = m[1];
      if (spec.startsWith('.') || spec.startsWith('/')) continue;
      const name = spec.startsWith('@')
        ? spec.split('/').slice(0, 2).join('/')
        : spec.split('/')[0];
      used.add(name);
    }
  }
}
scan('./src');

const ghosts = [...used].filter(d => !declared.has(d));
const dead = [...declared].filter(d => !used.has(d));
if (ghosts.length) console.error('幽灵依赖（未声明但被使用）:', ghosts);
if (dead.length) console.log('死依赖（声明但未使用）:', dead);
process.exit(ghosts.length ? 1 : 0); // 幽灵依赖进 CI 门禁
```
**评分点**：
- 裸导入/相对导入分界判定。
- scope 包名归并取两段（细节分）。
- 双向报告（幽灵 + 死依赖）。
- 幽灵依赖 exit 1 进 CI（门禁语义），死依赖仅警告。
- node_modules 排除（扫描剪枝）。
