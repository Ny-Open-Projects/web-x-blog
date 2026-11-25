---
title: [ALG-433] 手写 Trie 统计前缀：搜索联想热度
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-433：手写 Trie 统计前缀：搜索联想热度

**答**：
- 题目：搜索框联想——输入前缀实时返回「该前缀下的高频词 Top10」。Trie 节点存经过计数（前缀热度）与词尾计数。
- 思路：insert 时沿途每个节点 cnt++（经过次数）、词尾 end++；联想：走前缀到节点，DFS 收集子树词尾按热度排序取 Top10。
- 评分点：沿途计数 vs 词尾计数；前缀节点定位；Top10 收集（小顶堆剪枝）。

```javascript
class Trie {
  constructor() { this.root = { children: {}, pass: 0, end: 0, word: null }; }
  insert(word, weight = 1) {
    let node = this.root;
    node.pass += weight;
    for (const c of word) {
      node = node.children[c] ??= { children: {}, pass: 0, end: 0, word: null };
      node.pass += weight;                                 // 沿途热度
    }
    node.end += weight; node.word = word;                  // 词尾计数
  }
  suggest(prefix, k = 10) {                                // 联想 Top K
    let node = this.root;
    for (const c of prefix) {
      node = node.children[c];
      if (!node) return [];
    }
    const out = [];
    const dfs = (u) => {                                   // 收集子树词尾
      if (u.word && u.end) out.push({ word: u.word, heat: u.end });
      for (const c of Object.values(u.children)) { dfs(c); if (out.length > 50) return; }
    };
    dfs(node);
    return out.sort((a, b) => b.heat - a.heat).slice(0, k);
  }
}
```
