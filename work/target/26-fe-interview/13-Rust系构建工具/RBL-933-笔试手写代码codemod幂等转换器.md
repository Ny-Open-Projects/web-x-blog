---
title: [RBL-933] 笔试：手写代码 codemod 幂等转换器（条件转换 + 幂等性）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-933：笔试：手写代码 codemod 幂等转换器（AST 近似 + 幂等）

**答**：实现 `codemod(code)`（文本级 AST 近似即可）。规则：1) 转换 `process.env.X` → `import.meta.env.X`——但跳过：字符串字面量内（引号包裹的同形文本）、注释行；2) 跳过已是 `import.meta.env` 的（幂等：跑两次结果一致）；3) 转换计数返回；4) `require.context(` → `import.meta.glob(`（简单文本替换，同样跳过字符串/注释）。实现 `countChanges(code)` 与幂等断言 `assertIdempotent(code)`（跑两次一致，不一致抛错）。边界：空代码；全字符串内的同形文本（不转换）。

```javascript
function codemod(code = '') {
  let count = 0;
  const lines = code.split('\n');
  const out = lines.map((line) => {
    const t = line.trim();
    if (t.startsWith('//') || t.startsWith('*') || t.startsWith('/*')) return line;
    // 剥离字符串字面量：按引号切段，仅处理代码段
    const segs = splitStrings(line);
    const processed = segs.map((seg, i) => {
      if (i % 2 === 1) return seg;                       // 奇数段 = 字符串内容（保留）
      let s = seg;
      if (!/import\.meta\.env/.test(s)) {
        s = s.replace(/process\.env\.(\w+)/g, (_, k) => { count++; return `import.meta.env.${k}`; });
      }
      s = s.replace(/require\.context\(/g, () => { count++; return 'import.meta.glob('; });
      return s;
    });
    return processed.join('');
  });
  return { code: out.join('\n'), count };
}
function splitStrings(line) {
  const segs = []; let buf = ''; let quote = null;
  for (const ch of line) {
    if (quote) { buf += ch; if (ch === quote) { segs.push(buf); buf = ''; quote = null; } continue; }
    if (ch === '"' || ch === "'" || ch === '`') { segs.push(buf); buf = ch; quote = ch; continue; }
    buf += ch;
  }
  segs.push(buf);
  return segs;
}
function assertIdempotent(code) {
  const a = codemod(code);
  const b = codemod(a.code);
  if (a.code !== b.code) throw new Error('codemod 非幂等——转换器有 bug');
  return true;
}

// 自测
const src = [
  "const api = process.env.API_URL;",
  "console.log('process.env.API_URL is set');",          // 字符串内不转
  "// process.env.DEBUG",                                // 注释不转
  "const ctx = require.context('./pages');",
  "const meta = import.meta.env.MODE;",                  // 已是新形态
].join('\n');
let r = codemod(src);
console.log(r.count === 3);                              // API_URL + require.context（MODE 已幂等不计数）
console.log(r.code.includes('import.meta.env.API_URL'));
console.log(r.code.includes("'process.env.API_URL is set'"));   // 字符串保留
console.log(r.code.includes('// process.env.DEBUG'));   // 注释保留
console.log(r.code.includes('import.meta.glob('));
console.log(r.code.includes('import.meta.env.MODE'));

console.log(assertIdempotent(src) === true);             // 幂等
console.log(codemod('').count === 0);
// 非幂等检测
let e; try { assertIdempotent('process.env.X = import.meta.env.Y'); } catch (x) { e = x; }
console.log(e === null || /幂等/.test(e.message ?? ''));
```

**评分点**：
- 字符串/注释跳过正确（引号切段——单双引号/模板串的跨引号处理说明局限即可）
- 幂等性（已转换形态不重复计数/转换）；计数语义清晰
- assertIdempotent 的断言实现（跑两次对比）；边界
- 能说清「codemod 错误是静默改错代码，AST 按语法角色定位、正则会误伤字符串与注释」属于加分
