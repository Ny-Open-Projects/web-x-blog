---
title: [417] 笔试手写：实现依赖预构建的 CommonJS 到 ESM 转换器
date: 2026-11-17
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, 预构建, CJS-ESM]
type: 笔试题
---

## RBL-417：笔试手写——实现依赖预构建的 CommonJS 到 ESM 转换器

**答**：输入 CJS 模块源码（简化为三类语句：`module.exports = expr`、`exports.name = expr`、`const x = require('dep')`），转换为 ESM：默认导出（module.exports）、命名导出（exports.name）、import 语句（require 去重、命名导入 `import { x } from` 或默认导入）。保持语句顺序（import 提到最前，其余保持原序）。未识别行原样保留。

```js
function cjsToEsm(src) {
  const imports = [], namedExports = [], body = [];
  let defaultExport = null;
  const imported = new Map();      // dep -> Set<names>，去重
  for (const line of src.split('\n')) {
    let m;
    if ((m = line.match(/const\s+(\w+)\s*=\s*require\(['"]([^'"]+)['"]\)/))) {
      const [, varName, dep] = m;
      const names = imported.get(dep) ?? imported.set(dep, new Set()).get(dep);
      if (!names.has(varName)) names.add(varName);       // 同 dep 去重
      continue;                                          // require 行转 import，不进 body
    }
    if ((m = line.match(/module\.exports\s*=\s*(.+)/))) {
      defaultExport = m[1]; continue;
    }
    if ((m = line.match(/exports\.(\w+)\s*=\s*(.+)/))) {
      namedExports.push(`export const ${m[1]} = ${m[2]}`); continue;
    }
    body.push(line);                                     // 未识别行原样保留
  }
  for (const [dep, names] of imported) {
    imports.push(`import { ${[...names].join(', ')} } from '${dep}';`);
  }
  if (defaultExport) namedExports.push(`export default ${defaultExport}`);
  return [...imports, ...namedExports, ...body].join('\n');
}
const src = [
  "const path = require('path');",
  "const path2 = require('path');",
  "exports.format = path.join;",
  "module.exports = { version: 1 };",
].join('\n');
console.log(cjsToEsm(src));
// import { path, path2 } from 'path';
// export const format = path.join;
// export default { version: 1 };
```

**评分点**：
- require 去重合并（同 dep 多次 require 合并为一条 import——预构建的核心收益）
- 三类语句的正则覆盖与未识别行原样保留（不吞代码）
- import 提前、其余保持原序（ESM 语法约束：import 必须顶层前置）
- 能讨论：真实预构建的复杂度（esbuild 转换整个依赖图、interop 默认导出、动态 require 无法静态转换）
