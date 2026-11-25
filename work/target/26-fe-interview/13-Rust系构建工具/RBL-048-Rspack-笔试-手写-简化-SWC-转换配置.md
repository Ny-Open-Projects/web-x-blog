---
title: [RBL-048] 笔试：手写简化 AST 转换器（识别 import 并重写目标语法）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-048：笔试：手写简化 AST 转换器（识别 import 并重写目标语法）
**答**：实现 transform(code, options)：1) 把 `import x from 'y'` 转换为 CommonJS `const x = require('y')`（默认导出）；2) 处理命名导入 `import { a, b as c } from 'y'`；3) options.dropConsole 为真时删除 console.* 语句；4) 保留代码其余部分不变；5) 说明为什么生产级实现必须走 AST 而不是正则。

```javascript
function transform(code, { dropConsole = false } = {}) {
  let out = code;

  // 1) 默认导入
  out = out.replace(
    /import\s+(\w+)\s+from\s+(['"])([^'"]+)\2;?/g,
    (_m, local, _q, spec) => `const ${local} = require(${JSON.stringify(spec)});`
  );

  // 2) 命名导入（含 as 重命名）
  out = out.replace(
    /import\s*\{([^}]+)\}\s*from\s*(['"])([^'"]+)\2;?/g,
    (_m, specifiers, _q, spec) => {
      const req = `require(${JSON.stringify(spec)})`;
      const parts = specifiers.split(',').map(s => s.trim()).filter(Boolean)
        .map(s => {
          const [imported, local = imported] = s.split(/\s+as\s+/).map(x => x.trim());
          return `const ${local} = ${req}.${imported};`;
        });
      return parts.join('\n');
    }
  );

  // 3) 删除 console 调用（简化：单行语句形式）
  if (dropConsole) out = out.replace(/^\s*console\.[\w]+\([^;]*\);?\s*$/gm, '');

  return out;
}
module.exports = { transform };
// 测试
console.log(transform(`import React from 'react';
import { useState as us, useMemo } from 'react';
console.log(1); const a = 2;`, { dropConsole: true }));
```
**评分点**：
- 命名导入的 as 重命名处理（细节分）。
- 默认导入与命名导入两种 pattern 都覆盖。
- dropConsole 只删整条语句不误伤（正则用行级锚点）。
- 能说出正则方案的缺陷：字符串/注释/模板字面量中的伪 import 会被误改，AST 才能区分上下文——这是 SWC/esbuild 用真 AST 的原因。
