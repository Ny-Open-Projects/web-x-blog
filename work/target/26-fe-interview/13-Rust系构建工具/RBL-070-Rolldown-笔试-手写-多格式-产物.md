---
title: [RBL-070] 笔试：手写库打包产物 exports 映射生成器
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-070：笔试：手写库打包产物 exports 映射生成器
**答**：给定 dist 目录文件清单与 package.json，生成合法的 exports 字段：1) 对 src 下每个 .ts 入口（index.ts、utils/format.ts）生成对应的 "." "./utils/format" 条目；2) 每条目含 import（.mjs）、require（.cjs）、types（.d.ts）三种条件；3) 条件顺序 types 在前（TS moduleResolution 惯例）；4) 无对应产物时跳过并警告；5) 写回 package.json 保持其他字段不变。

```javascript
const fs = require('fs'), path = require('path');

function genExports(pkgRoot, dist = 'dist') {
  const srcDir = path.join(pkgRoot, 'src');
  const distDir = path.join(pkgRoot, dist);
  const exports = {};

  function walk(dir, rel = '') {
    for (const f of fs.readdirSync(dir, { withFileTypes: true })) {
      if (f.isDirectory()) walk(path.join(dir, f.name), `${rel}/${f.name}`);
      else if (f.name.endsWith('.ts') && !f.name.endsWith('.d.ts')) {
        const key = rel === '' ? '.' : `.${rel}`;
        const base = `${dist}${rel}/${f.name.replace(/\.ts$/, '')}`;
        const mjs = `${base}.mjs`, cjs = `${base}.cjs`, dts = `${base}.d.ts`;
        if (!fs.existsSync(path.join(pkgRoot, mjs))) {
          console.warn(`[exports] 缺产物: ${mjs}，跳过 ${key}`);
          continue;
        }
        exports[key] = {
          types: `./${dts}`,
          import: `./${mjs}`,
          require: `./${cjs}`,
        };
      }
    }
  }
  walk(srcDir);

  const pkgPath = path.join(pkgRoot, 'package.json');
  const pkg = JSON.parse(fs.readFileSync(pkgPath, 'utf8'));
  pkg.exports = exports;
  fs.writeFileSync(pkgPath, JSON.stringify(pkg, null, 2) + '\n');
  return exports;
}
module.exports = { genExports };
```
**评分点**：
- types 条件放最前（TS 消费顺序敏感）。
- 产物存在性校验 + 警告（不静默生成死链接）。
- 目录递归映射 src→exports key（"." 特判）。
- 不覆盖 package.json 其他字段（读改写而非重建）。
- 能说出 exports 的副作用：未列入的子路径被封禁（防 deep import 事故）。
