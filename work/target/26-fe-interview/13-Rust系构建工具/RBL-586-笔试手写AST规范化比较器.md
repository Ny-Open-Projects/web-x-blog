---
title: [RBL-586] 笔试：手写产物 AST 规范化比较器（忽略命名与格式）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-586：笔试：手写产物 AST 规范化比较器（忽略命名与格式）

**答**：实现 `normalizeAst(code)` 与 `expectSameAst(code1, code2)`。给定一个极简 JS 子集的 parser（题目提供 `parse(code)` 返回形如 `{ type, name?, op?, left?, right?, value? }` 的 AST，仅支持 var 声明、二元运算、字面量、标识符引用），normalize 需做到：1) 忽略空白与分号差异；2) **标识符重命名归一**（按「首次出现顺序」把所有标识符映射为 `v1,v2,...`——alpha 重命名等价的两个程序视为相同）；3) 交换律二元运算（`+` `*`）在两侧均为「非常量标识符」时排序左右子树。`expectSameAst` 不等时抛出含「首个分歧节点路径」的错误。边界：空程序；嵌套深度大（递归改显式栈可加分）。

```javascript
// 题目提供
const parse = (code) => globalThis.__parse(code);

function normalize(node) {
  const names = new Map();                       // 原名 -> v1/v2...
  const rename = (n) => {
    if (n.name && !names.has(n.name)) names.set(n.name, `v${names.size + 1}`);
    return n.name ? names.get(n.name) : undefined;
  };
  const walk = (n) => {
    const out = { type: n.type };
    for (const k of Object.keys(n)) {
      if (k === 'type') continue;
      const v = n[k];
      if (v && typeof v === 'object' && v.type) out[k] = walk(v);
      else if (k === 'name') out[k] = rename(n);
      else out[k] = v;
    }
    // 交换律归一：+ / * 且左右都是非字面量时排序
    if ((n.op === '+' || n.op === '*') && out.left && out.right &&
        !('value' in out.left) && !('value' in out.right) &&
        JSON.stringify(out.left) > JSON.stringify(out.right))
      [out.left, out.right] = [out.right, out.left];
    return out;
  };
  if (node.type === 'Program' && !(node.body || []).length) return { type: 'Program', body: [] };
  return { type: node.type, body: (node.body || []).map(walk) };
}

function expectSameAst(a, b) {
  const na = normalizeAst(a), nb = normalizeAst(b);
  const path = [];
  const diffAt = (x, y, p) => JSON.stringify(x) !== JSON.stringify(y) ? p : null;
  const eq = (x, y, p = '') => {
    const d = diffAt(x, y, p || '/');
    if (d !== null && (x.type !== y.type)) return d;
    for (const k of new Set([...Object.keys(x || {}), ...Object.keys(y || {})])) {
      const r = eq(x[k], y[k], p + '/' + k);
      if (r) return r;
    }
    return null;
  };
  const bad = eq(na, nb);
  if (bad) throw new Error(`AST 不一致，首个分歧路径: ${bad}`);
  return true;
}
const normalizeAst = normalize;

// 自测：alpha 等价 + 交换律 + 空程序
// 代码 A: var total = base + extra;  代码 B: var sum = extra2 + base2;  —— 语义同构
console.log(normalizeAst(globalThis.__parse('var total = base + extra')).body[0].id); // v1
console.log(expectSameAst('var total = base + extra', 'var sum = extra2 + base2'));   // true
console.log(expectSameAst('var x = 1 + y', 'var x = y + 1'));   // 左侧含字面量，不排序 -> 可能不等
console.log(normalizeAst({ type: 'Program', body: [] }).body.length === 0);
```

**评分点**：
- 标识符按首次出现顺序归一（alpha 等价判定正确），名字映射作用域全局处理（子集语言无块级作用域可接受，能说明即可）
- 交换律归一只在两侧均非常量时生效（字面量不参与排序，避免 1+y 与 y+1 误等）
- 空程序/缺失字段边界不崩；比较失败给出首个分歧路径（诊断体验）
- 递归深度意识（大产物的栈风险）与可改写为显式栈属于加分
