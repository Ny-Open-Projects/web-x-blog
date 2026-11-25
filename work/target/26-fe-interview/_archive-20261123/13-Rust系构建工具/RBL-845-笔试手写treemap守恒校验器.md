---
title: [RBL-845] 笔试：手写 treemap 守恒校验器（叶子聚合断言 + 未归因字节定位）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-845：笔试：手写 treemap 守恒校验器（聚合断言 + 归因缺口）

**需求**：实现 `verifyConservation(tree)`。tree 为层级树 `{ name, size?, children? }`。规则：1) 有 children 的节点：size 应等于叶子 size 之和——偏差超过 max(size × 2%, 64B) → violation `{ node: name, declared, sum, gap }`；2) 无 size 声明的父节点（size 缺失）→ 用叶子和回填并在结果标注 `filled: true`；3) **归因缺口总账**：所有 violation 的 gap 之和 = unaccounted（丢失字节总量）；4) 返回 `{ violations, filled: string[], unaccounted }`。边界：全叶子树（无 violation）；children 为空数组（size 即自身）。

```javascript
function verifyConservation(tree) {
  const violations = [], filled = [];
  const walk = (node, path) => {
    if (!node.children?.length) return node.size ?? 0;   // 叶子
    let sum = 0;
    for (const c of node.children) sum += walk(c, `${path}/${c.name}`);
    const declared = node.size ?? sum;
    if (node.size == null) filled.push(path);
    const gap = declared - sum;
    const tol = Math.max(declared * 0.02, 64);
    if (Math.abs(gap) > tol)
      violations.push({ node: path, declared, sum, gap });
    return declared;
  };
  walk(tree, tree.name);
  const unaccounted = violations.reduce((s, v) => s + v.gap, 0);
  return { violations, filled, unaccounted };
}

// 自测
// 1) 守恒
let tree = { name: 'root', size: 300, children: [
  { name: 'a.js', size: 200, children: [
    { name: 'm1', size: 150 }, { name: 'm2', size: 50 } ] },
  { name: 'b.js', size: 100, children: [ { name: 'm3', size: 100 } ] },
] };
let r = verifyConservation(tree);
console.log(r.violations.length === 0 && r.unaccounted === 0);

// 2) 缺口：a.js 声明 220 但叶子 200
tree = { name: 'root', size: 320, children: [
  { name: 'a.js', size: 220, children: [ { name: 'm1', size: 150 }, { name: 'm2', size: 50 } ] },
  { name: 'b.js', size: 100, children: [ { name: 'm3', size: 100 } ] },
] };
r = verifyConservation(tree);
console.log(r.violations[0].node === 'root/a.js' && r.violations[0].gap === 20);
console.log(r.unaccounted === 20);

// 3) size 缺失回填
tree = { name: 'root', children: [
  { name: 'a.js', children: [ { name: 'm1', size: 150 } ] },
] };
r = verifyConservation(tree);
console.log(r.filled.join(',') === 'root,root/a.js');
console.log(r.violations.length === 0);

// 4) 容差内不报
tree = { name: 'root', size: 1050, children: [ { name: 'a', size: 1040, children: [ { name: 'x', size: 1040 } ] } ] };
console.log(verifyConservation(tree).violations.length === 0);   // gap 10 < 64B 容差

// 全叶子
console.log(verifyConservation({ name: 'x', size: 5 }).violations.length === 0);
console.log(verifyConservation({ name: 'e', children: [] }).violations.length === 0);
```

**评分点**：
- 递归守恒校验（叶子求和 vs 声明）；容差规则（max(2%, 64B)——小文件容差不过敏）
- size 缺失回填标注（filled）；归因缺口总账 unaccounted（「丢失的字节」可量化）
- 边界：全叶子/空 children/容差内
- 能说清「聚合不一致会误导优化决策，凭空消失的字节恰是最该发现的（polyfill/运行时）」属于加分
