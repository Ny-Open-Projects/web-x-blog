---
title: [RBL-098] 笔试：手写多 target 编译分流器（client/server/edge）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-098：笔试：手写多 target 编译分流器（client/server/edge）
**答**：实现 multiTargetCompile(code, target)：1) client：保留 console、注入 hydration 辅助；2) server：剥离所有 DOM 访问行（window/document 开头的语句）、保留 console；3) edge：剥离 DOM 且剥离 console（无调试）；4) 'use client' 文件在 server target 下输出为引用占位（export default '__CLIENT_REF__'）；5) 返回 { code, target, clientRef } 结构。

```javascript
function multiTargetCompile(code, target) {
  const isClientComponent = /^['"]use client['"];/m.test(code);
  const result = { target, code, clientRef: null };

  // 'use client' 边界：server/edge 侧只留引用占位
  if (isClientComponent && target !== 'client') {
    result.clientRef = '__CLIENT_REF__';
    result.code = code.match(/export\s+(?:default\s+)?(\w+)/)?.[1]
      ? `export default '__CLIENT_REF__';`
      : `export {};`;
    return result;
  }

  let out = code;
  // DOM 剥离（server/edge）：整行删除 window./document. 开头的语句（简化）
  if (target !== 'client') {
    out = out.replace(/^\s*(window|document)\..*;?\s*$/gm, '');
  }
  // edge：无 console
  if (target === 'edge') {
    out = out.replace(/^\s*console\..*;?\s*$/gm, '');
  }
  // client：注入 hydration 辅助
  if (target === 'client') {
    out = `import { registerHydration } from 'runtime/hydration';\nregisterHydration(module);\n${out}`;
  }
  result.code = out;
  return result;
}
module.exports = { multiTargetCompile };

// 测试
// multiTargetCompile(`'use client';
// export default function Btn(){}`, 'server')
// → { target:'server', clientRef:'__CLIENT_REF__', code:"export default '__CLIENT_REF__';" }
```
**评分点**：
- 'use client' 指令识别与边界产物语义（server 侧占位引用）。
- target 差异化处理（DOM 剥离范围：server 保留 console、edge 全剥）。
- client 注入运行时辅助（体现 per-target 变换）。
- clientRef 字段供上层编排（占位可被替换）。
- 能讲出真实编译器中 DOM 访问通过 AST 判定，正则只是简化。
