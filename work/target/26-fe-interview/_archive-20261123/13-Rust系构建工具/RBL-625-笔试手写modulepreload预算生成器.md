---
title: [RBL-625] 笔试：手写 modulepreload 生成器（深度截断 + 字节预算）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-625：笔试：手写 modulepreload 生成器（深度截断 + 字节预算）

**需求**：实现 `genPreloads(entry, manifest, { maxDepth, budgetKB })`。entry 为 chunk id；manifest: `get(id) -> { url, sizeKB, staticImports: id[] }`。从 entry 出发沿 staticImports 递归生成 `<link rel="modulepreload" href="url">` 列表（entry 自身不生成链接）。约束：1) 深度 > maxDepth 停止；2) 累计字节数（含当前候选）> budgetKB 时跳过该节点但**继续尝试兄弟分支**（贪心：兄弟更小仍可进）；3) 同一 chunk 只生成一次；4) 循环引用不死循环；5) 返回 `{ links: string[], usedKB, skipped: string[] }`（skipped 记录因预算/深度被跳过的 chunk id）。

```javascript
function genPreloads(entry, manifest, { maxDepth = 2, budgetKB = 100 } = {}) {
  const links = [], skipped = [], seen = new Set();
  let usedKB = 0;
  (function walk(id, depth, stack) {
    if (seen.has(id)) return;                            // 循环引用/去重
    seen.add(id);
    const node = manifest.get(id);
    if (!node) return;
    if (depth > maxDepth) { skipped.push(id); return; }  // 深度截断
    if (usedKB + node.sizeKB > budgetKB) {               // 预算：跳过本节点，兄弟继续
      skipped.push(id);
      return;
    }
    usedKB += node.sizeKB;
    for (const dep of node.staticImports) walk(dep, depth + 1, [...stack, id]);
    if (id !== entry) links.push(`<link rel="modulepreload" href="${node.url}">`);
  })(entry, 0, []);
  return { links, usedKB, skipped: [...new Set(skipped)] };
}

// 自测
const manifest = new Map([
  ['entry', { url: '/e.js', sizeKB: 10, staticImports: ['a', 'b'] }],
  ['a', { url: '/a.js', sizeKB: 60, staticImports: ['c'] }],
  ['b', { url: '/b.js', sizeKB: 20, staticImports: [] }],
  ['c', { url: '/c.js', sizeKB: 50, staticImports: ['a'] }],   // 引用回 a：循环
]);
const r = genPreloads('entry', manifest, { maxDepth: 3, budgetKB: 100 });
// 遍历：a(60 进，used=60) -> c(50 超 100 预算 skip) ；b(20 进，used=80)
// links: ['/a.js', '/b.js']（entry 排除），skipped 含 'c'
console.log(r.links.join(' '));
console.log(r.usedKB === 80 && r.skipped.includes('c'));
console.log(r.links.length === 2);

// 深度截断
const r2 = genPreloads('entry', manifest, { maxDepth: 1, budgetKB: 1000 });
// depth>1 的 c 被 skip；a、b 进
console.log(r2.links.length === 2 && r2.skipped.includes('c'));

// 兄弟贪心：大块超预算后兄弟仍进
const m2 = new Map([
  ['root', { url: '/r.js', sizeKB: 0, staticImports: ['big', 'small'] }],
  ['big', { url: '/big.js', sizeKB: 120, staticImports: [] }],
  ['small', { url: '/small.js', sizeKB: 30, staticImports: [] }],
]);
const r3 = genPreloads('root', m2, { maxDepth: 2, budgetKB: 50 });
console.log(r3.links.some(l => l.includes('small')) && !r3.links.some(l => l.includes('big')));
```

**评分点**：
- 预算语义正确：超预算跳过当前节点但兄弟分支继续（贪心而非整体截断）
- 深度截断与去重（循环引用不死循环）；entry 自身不生成链接
- usedKB 累计含被接受的节点；skipped 记录原因可追溯（去重后）
- 能说明「modulepreload 递归语义 vs 预算截断的显式列出」差异属于加分
