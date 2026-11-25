---
title: [RBL-753] 笔试：手写 CSS-in-JS 静态化分析器（动态插值判定 + 迁移建议）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-753：笔试：手写 CSS-in-JS 静态化分析器（动态判定 + 迁移建议）

**答**：实现 `analyze(code)`：提取所有 `` styled.xxx`...` `` 与 `` css`...` `` 模板块，分类：1) 静态（无 `${...}`）；2) 半动态（有插值但不含 props/functions 引用——如 `${size}` 引用外层常量可构建期内联）；3) 动态（含 `props.`/`=>` 引用，必须运行时）。返回 `{ blocks: Array<{ css, kind }>, ratio, advice }`——ratio = 动态块 / 总块；advice 按阈值（<0.2 'full-static'、<0.6 'hybrid'、else 'runtime'）。空块返回 ratio 0 / advice 'none'。

```javascript
function analyze(code) {
  const blocks = [...code.matchAll(/(?:styled\.\w+|css)`([^`]*)`/g)].map(m => m[1]);
  if (!blocks.length) return { blocks: [], ratio: 0, advice: 'none' };
  const classified = blocks.map(css => {
    if (!/\$\{/.test(css)) return { css, kind: 'static' };
    if (/\$\{[^}]*\b(props\.|=>|\$\{props)/.test(css)) return { css, kind: 'dynamic' };
    return { css, kind: 'semi' };                        // 常量插值可构建期内联
  });
  const dynamic = classified.filter(b => b.kind === 'dynamic').length;
  const ratio = +(dynamic / classified.length).toFixed(2);
  const advice = ratio < 0.2 ? 'full-static'
    : ratio < 0.6 ? 'hybrid' : 'runtime';
  return { blocks: classified, ratio, advice };
}

// 自测
let r = analyze(`
const Btn = styled.button\`color: red; padding: 8px;\`;
const Card = styled.div\`border: 1px solid \${props => props.theme.border};\`;
`);
console.log(r.blocks[0].kind === 'static');
console.log(r.blocks[1].kind === 'dynamic');
console.log(r.ratio === 0.5 && r.advice === 'hybrid');

r = analyze(`
const A = styled.div\`margin: 0;\`;
const B = styled.div\`padding: \${SPACING}px;\`;        // 常量插值
const C = css\`font-weight: bold;\`;
`);
console.log(r.blocks[1].kind === 'semi');
console.log(r.ratio === 0 && r.advice === 'full-static');

r = analyze(`
const X = styled.div\`color: \${props => props.color}\`;
const Y = styled.div\`bg: \${p => p.bg}\`;
`);
console.log(r.ratio === 1 && r.advice === 'runtime');

console.log(analyze('const a = 1;').advice === 'none');
```

**评分点**：
- 三分类判定正确：static（无插值）/ semi（常量插值）/ dynamic（props/函数引用——必须运行时）
- ratio 与阈值建议三档；空代码 'none'
- 能说清「semi 类可在构建期内联（构建器持有常量表），dynamic 才是运行时的真实残余」属于加分
