---
title: [RBL-076] 笔试：手写 preserveModules 产物路径映射器
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-076：笔试：手写 preserveModules 产物路径映射器
**答**：实现 mapPreserveModules(entries, rootDir)：1) 每个源文件对应一个产物文件（保留目录结构）；2) 路径基于 rootDir 相对化（src/components/Button.tsx → dist/components/Button.js）；3) rootDir 之外的文件（如 node_modules 被保留时）提升到 dist 的 _external/ 前缀避免路径逃逸；4) index 文件对应目录名产物（src/index.ts → dist/index.js）；5) 输出 Map<源路径, 产物路径>。

```javascript
const path = require('path');

function mapPreserveModules(files, rootDir, outDir = 'dist') {
  const result = new Map();
  const root = path.resolve(rootDir);
  for (const file of files) {
    const abs = path.resolve(file);
    const rel = path.relative(root, abs);          // 相对 rootDir
    if (rel.startsWith('..')) {
      // root 外：提升进 _external，防产物逃逸出 outDir
      const safe = '_external/' + path.basename(abs);
      result.set(abs, path.join(outDir, safe));
      continue;
    }
    let out = rel.replace(/\.(ts|tsx|jsx)$/, '.js'); // 扩展名归一
    // index 归一：src/utils/index.ts → dist/utils.js（与 index.ts → index.js 对齐）
    out = out.replace(/(^|\/)index\.js$/, (_m, p) => `${p || ''}index.js`.replace(/^\/?/, (p ? '' : '')) ? out.replace(/index\.js$/, 'index.js') : out);
    // 上面保持 index.js；若要目录名风格：utils/index.ts → utils.js：
    out = out.endsWith('index.js') && path.dirname(rel) !== '.'
      ? path.join(path.dirname(rel), 'index.js')
      : out;
    result.set(abs, path.join(outDir, out));
  }
  return result;
}
module.exports = { mapPreserveModules };

// 测试
// files: ['src/index.ts','src/components/Button.tsx','../lib/other.js']
// → { 'src/index.ts': 'dist/index.js',
//     'src/components/Button.tsx': 'dist/components/Button.js',
//     '../lib/other.js': 'dist/_external/other.js' }
```
**评分点**：
- 相对化以 rootDir 为基准（而不是 cwd）。
- 逃逸路径防护（.. 开头进 _external 前缀）。
- 扩展名归一（ts/tsx→js）。
- index 文件语义说明（保留 index.js 或折叠为目录名，讲清任一约定即可）。
- 能联系 rollup preserveModules 的实际用途：tree shaking 消费方友好 + 调试产物对源。
