---
title: [ALG-423] 手写 AC 自动机构建：多敏感词匹配
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-423：手写 AC 自动机构建：多敏感词匹配

**答**：
- 题目：内容安全需要一次扫描同时匹配数千个敏感词（单个 KMP 要跑几千遍）。AC 自动机：Trie + fail 指针，一次扫描匹配全部模式。
- 思路：① 建 Trie；② BFS 建 fail（根的 fail=根，节点 u 的孩子 c 的 fail = fail(u) 的孩子 c，不存在则沿 fail 链回退）；③ 扫描：无转移沿 fail 回退，命中词尾收集输出（含 fail 链上的所有词尾）。
- 评分点：fail 指针 BFS 构建；扫描时沿 fail 链收集；复杂度 O(n + 总词长)。

```javascript
function buildAC(patterns) {
  const root = { children: {}, fail: null, out: [] };
  for (const p of patterns) {                               // ① Trie
    let node = root;
    for (const c of p) node = node.children[c] ??= { children: {}, fail: null, out: [] };
    node.out.push(p);                                      // 词尾标记
  }
  const queue = [];
  for (const c of Object.values(root.children)) { c.fail = root; queue.push(c); }   // ② BFS fail
  while (queue.length) {
    const u = queue.shift();
    for (const [c, v] of Object.entries(u.children)) {
      let f = u.fail;
      while (f && !f.children[c]) f = f.fail;              // 沿 fail 找转移
      v.fail = f ? f.children[c] : root;
      v.out.push(...v.fail.out);                           // 合并 fail 链输出
      queue.push(v);
    }
  }
  return root;
}
function acScan(text, root) {                              // ③ 扫描
  const hits = [];
  let node = root;
  for (let i = 0; i < text.length; i++) {
    while (node !== root && !node.children[text[i]]) node = node.fail;
    node = node.children[text[i]] ?? root;
    for (const p of node.out) hits.push({ pattern: p, end: i });   // 含 fail 链词尾
  }
  return hits;
}
```
