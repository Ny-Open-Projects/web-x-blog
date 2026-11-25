---
title: [RBL-073] 笔试：手写依赖预构建扫描器（Vite optimizeDeps 扫描逻辑）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-073：笔试：手写依赖预构建扫描器（Vite optimizeDeps 扫描逻辑）
**题目**：实现 scanDeps(root)：1) 从 index.html 或入口 js 出发，收集所有源码 import；2) 区分裸导入（bare import，进预构建清单）与相对/绝对路径导入（业务源码，继续递归）；3) 裸导入再去掉子路径归并到包名（lodash/debounce → lodash）；4) 排除 node_modules 递归（依赖内部 import 不再扫描，由预构建产物自带）；5) 输出去重后的依赖名清单。

```javascript
const fs = require('fs'), path = require('path');

function scanDeps(root) {
  const entry = path.join(root, 'src/index.js');
  const deps = new Set();
  const visited = new Set();

  function visit(file) {
    if (visited.has(file)) return;
    visited.add(file);
    if (!fs.existsSync(file)) return;
    const code = fs.readFileSync(file, 'utf8');
    for (const m of code.matchAll(
      /(?:import\s+[^'"]*?from\s*|import\s*|require\()\s*['"]([^'"]+)['"]/g)) {
      const spec = m[1];
      if (spec.startsWith('.') || spec.startsWith('/')) {
        // 相对路径：解析后继续递归业务源码
        let p = path.resolve(path.dirname(file), spec);
        for (const ext of ['.js', '.ts', '.jsx', '.tsx', '/index.js']) {
          if (fs.existsSync(p + ext)) { visit(p + ext); break; }
          if (fs.existsSync(p) && fs.statSync(p).isDirectory()
              && fs.existsSync(path.join(p, 'index.js'))) {
            visit(path.join(p, 'index.js')); break;
          }
        }
      } else if (!spec.startsWith('\0')) {
        // 裸导入：归并到包名（scope 包保留 @scope/name）
        const pkgName = spec.startsWith('@')
          ? spec.split('/').slice(0, 2).join('/')
          : spec.split('/')[0];
        deps.add(pkgName); // 不进 node_modules 递归
      }
    }
  }
  visit(entry);
  return [...deps];
}
module.exports = { scanDeps };
```
**评分点**：
- bare import 判定（不以 . / / 开头）是分界线。
- 子路径归并：非 scope 包取第一段，@scope 包取两段（细节分）。
- 相对导入递归但不进 node_modules（扫描终止条件）。
- visited 去重防环。
- 能讲出预构建的目的：CJS→ESM + 合并散装文件减少请求数。
