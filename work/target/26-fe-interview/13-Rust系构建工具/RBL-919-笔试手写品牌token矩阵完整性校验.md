---
title: [RBL-919] 笔试：手写品牌 token 矩阵完整性校验（缺项回退 + JS 消费审计）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-919：笔试：手写品牌 token 矩阵完整性校验（缺项 + JS 审计）

**答**：实现两部分。1) `verifyBrands(tokens, brands)`：tokens: `Record<name, { value, shared?: boolean, brands?: Record<b, string> }>`。规则：非 shared 且某品牌缺 brands 覆盖 → missing `{ brand, tokens: string[] }`（warn——回退默认 value 但要可见）；brands 覆盖的值与 value 全同且名字含 color/bg → 'not-adapted'（RBL-778 未适配语义）；2) `auditJsTokenUsage(code)`：检测 JS 固化消费：`const X = tokens.yyy` / `import { primary } from tokens` 模式 → warn 'frozen-token'（应实时读变量）；`getComputedStyle(...).getPropertyValue('--` → ok。返回 `{ missing: Array, notAdapted: Array, frozen: Array<{ line }>, ok }`。边界：无 brands 参数（单品牌跳过）；无 JS 消费。

```javascript
function verifyBrands(tokens, brands = []) {
  const missing = [], notAdapted = [];
  if (!brands.length) return { missing, notAdapted };
  for (const [name, def] of Object.entries(tokens)) {
    if (def.shared) continue;
    const gap = brands.filter(b => def.brands?.[b] === undefined);
    if (gap.length) missing.push({ brand: gap.join(','), tokens: [name] });
    const same = brands.filter(b =>
      def.brands?.[b] === def.value && /color|bg/i.test(name));
    if (same.length === brands.length) notAdapted.push(name);   // 全品牌未适配
  }
  return { missing, notAdapted };
}

function auditJsTokenUsage(code = '') {
  const frozen = [];
  (code ?? '').split('\n').forEach((line, i) => {
    if (/const\s+\w+\s*=\s*tokens\.\w+/.test(line) ||
        /import\s*\{[^}]*\}\s*from\s*['"]tokens['"]/.test(line))
      frozen.push({ line: i + 1, snippet: line.trim().slice(0, 40) });
  });
  return { frozen };
}

// 自测
const tokens = {
  primary: { value: '#3b82f6', brands: { a: '#3b82f6', b: '#f59e0b' } },
  bg: { value: '#ffffff', brands: { a: '#ffffff', b: '#ffffff' } },     // b 未适配
  spacing: { value: '8px', shared: true },               // 共享豁免
  font: { value: 'sans' },                               // b 缺项
};
let r = verifyBrands(tokens, ['a', 'b']);
console.log(r.missing.some(m => m.brand === 'b' && m.tokens[0] === 'font'));
console.log(r.notAdapted.join(',') === 'bg');
console.log(r.missing.every(m => !m.tokens.includes('spacing')));   // shared 豁免

console.log(verifyBrands(tokens, []).missing.length === 0);   // 单品牌跳过

// JS 固化审计
const code = [
  "const C = tokens.primary;",                           // frozen
  "import { primary } from 'tokens';",                   // frozen
  "const c = getComputedStyle(el).getPropertyValue('--primary');",  // ok
];
console.log(auditJsTokenUsage(code.join('\n')).frozen.length === 2);
console.log(auditJsTokenUsage('const a = 1;').frozen.length === 0);
```

**评分点**：
- 缺项检测（非 shared 才查）与未适配检测（颜色全同 base）语义区分；单品牌跳过
- JS 固化消费检测（const = tokens.x / import tokens）——「CSS 层完整 ≠ 全局完整」的双轨一致防线
- 边界：空 brands、无 JS 消费
- 能说清「热切换的隐形破坏者是 JS 侧 token 固化——token 完整性必须覆盖所有消费点」属于加分
