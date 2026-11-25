---
title: [RBL-647] 笔试：手写 isolatedModules 违规诊断器
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-647: 笔试：手写 isolatedModules 违规诊断器

**需求**：实现 `diagnoseIsolated(code)`。输入一段 TS 源码，检测三类 strip 模式下会静默出错的模式，返回诊断数组 `{ code, severity, message, hint, line }`：1) `ISOL1001`：`export { T } from './x'` 且 T 是类型（参数 typeNames 提供）但未标 type——应 `export type { T }`；2) `ISOL1002`：`import { T } from './x'` 且 T 是类型但未用 `import type`——strip 后变成运行时导入；3) `ISOL1003`：`const enum`——isolatedModules 下禁止（无法单文件展开）；4) 混合导入 `import { a, T } from` 中类型成员未拆分也报 1002（列出成员）。行号 1-based 精确。无违规返回空数组。

```javascript
function diagnoseIsolated(code, typeNames = []) {
  const types = new Set(typeNames);
  const lines = code.split('\n');
  const diags = [];
  lines.forEach((line, i) => {
    const n = i + 1;
    // 1) export { T } 未标 type
    let m = /^\s*export\s*\{([^}]+)\}\s*from/.exec(line);
    if (m) {
      const members = m[1].split(',').map(s => s.trim()).filter(Boolean);
      const bad = members.filter(s => types.has(s) && !s.startsWith('type '));
      if (bad.length) diags.push({
        code: 'ISOL1001', severity: 'error', line: n,
        message: `导出 ${bad.join(', ')} 是类型但未标 type`,
        hint: `改为 export type { ${bad.join(', ')} } from ...`,
      });
    }
    // 2) import { a, T } 类型成员未拆
    m = /^\s*import\s*\{([^}]+)\}\s*from/.exec(line);
    if (m) {
      const members = m[1].split(',').map(s => s.trim()).filter(Boolean);
      const bad = members.filter(s => types.has(s) && !s.startsWith('type '));
      if (bad.length) diags.push({
        code: 'ISOL1002', severity: 'error', line: n,
        message: `导入 ${bad.join(', ')} 是类型但未用 import type`,
        hint: `拆分：import type { ${bad.join(', ')} } from ...`,
      });
    }
    // 3) const enum
    if (/^\s*const\s+enum\b/.test(line)) diags.push({
      code: 'ISOL1003', severity: 'error', line: n,
      message: 'const enum 在 isolatedModules 下不可用',
      hint: '改用普通 enum 或 const 对象 + as const',
    });
  });
  return diags;
}

// 自测
const code = [
  "import { util, WidgetProps } from './widget';",        // 1002: WidgetProps
  "import type { Config } from './config';",              // ok
  "export { util } from './widget';",                     // ok（非类型）
  "export { WidgetProps } from './widget';",              // 1001
  "const enum Color { Red }",                             // 1003
  "enum Kind { A }",                                      // ok
].join('\n');
const d = diagnoseIsolated(code, ['WidgetProps', 'Config', 'Color']);
console.log(d.map(x => x.code).join(','));                // ISOL1002,ISOL1001,ISOL1003
console.log(d[0].line === 1 && d[1].line === 4 && d[2].line === 5);
console.log(d[0].hint.includes('import type'));

// 混合导入多成员
const d2 = diagnoseIsolated("import { a, T1, T2 } from './m';", ['T1', 'T2']);
console.log(d2.length === 1 && d2[0].message.includes('T1, T2'));

console.log(diagnoseIsolated('const a = 1;', []).length === 0);
```

**评分点**：
- 三类违规检测齐全（未标 type 的 export/import、const enum），行号准确
- 混合导入成员级检测（只报类型成员，不误伤值导入）；import type 显式豁免
- 诊断结构含 severity/message/hint（可操作修复建议）
- 能说清「这些违规在 strip 模式下是静默运行时错误，诊断是构建器对 tsc 的补位」属于加分
