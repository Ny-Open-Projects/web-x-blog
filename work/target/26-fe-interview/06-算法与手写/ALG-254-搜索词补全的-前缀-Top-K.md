---
title: [ALG-254] 搜索框联想：给定搜索热词表，按前缀返回 Top-10 补全（Trie + 节点级缓存）
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-254：搜索框联想：给定搜索热词表，按前缀返回 Top-10 补全（Trie + 节点级缓存）
**答**：搜索联想：热词表 5 万条（词 + 热度），用户输入前缀返回热度 Top-10。朴素：每输入过滤全表 O(5万×输入) 太慢。Trie + **节点级 Top 缓存**：每个节点存"该前缀下热度 Top-10"——查询 O(前缀长) 直接拿结果。

**思路**：建 Trie 时自底向上合并每节点的 Top-K（子节点 Top-K 并集 + 自身，取前 K）；查询沿前缀走，末节点的缓存即答案。

```javascript
class AutocompleteTrie {
  constructor(words, k = 10) {
    this.k = k; this.root = {};
    for (const { word, heat } of words) this.#insert(word, heat);
  }
  #insert(word, heat) {
    let node = this.root;
    for (const ch of word) node = node[ch] ??= { top: [], children: {} };
    (node.top ??= []).push({ word, heat });
    node.top.sort((a, b) => b.heat - a.heat);
    node.top = node.top.slice(0, this.k);            // 节点级 Top-K 截断
  }
  complete(prefix) {
    let node = this.root;
    for (const ch of prefix) {
      node = node.children?.[ch];
      if (!node) return [];
    }
    return (node.top ?? []).slice(0, this.k);        // O(前缀长) 直接取
  }
}
// 但上面实现有缺陷：node.top 只含"经过该节点的词在插入顺序下的前 K"，
// 需要自底向上合并子节点 Top-K 才是"该前缀下的全局 Top-K"：
// 后序遍历：node.top = merge(top of self + all children.tops).slice(0, k)
function mergeUp(node, k) {
  if (!node) return [];
  let all = [...(node.top ?? [])];
  for (const child of Object.values(node.children ?? {})) all = all.concat(mergeUp(child, k));
  return all.sort((a, b) => b.heat - a.heat).slice(0, k);
}
// 查询复杂度：O(L)（L=前缀长）；构建 O(总字符 × k log k)
// 空间代价：每节点存 Top-K（可按层级控制——深层节点存更少）
```

**评分点**：
- 节点级 Top-K 缓存实现 O(L) 查询——本题核心（朴素 Trie 收集后排序是 O(子树大小)）。
- 自底向上合并（mergeUp 后序）的正确性说明。
- Top-K 截断的空间控制。
- 热度排序的稳定性与更新策略（热词表周期重建）。
