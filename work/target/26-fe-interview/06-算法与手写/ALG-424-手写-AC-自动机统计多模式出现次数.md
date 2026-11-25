---
title: [ALG-424] 手写 AC 自动机统计多模式出现次数：内容安全扫描
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-424：手写 AC 自动机统计多模式出现次数：内容安全扫描

**答**：
- 题目：在 ALG-423 基础上统计每个敏感词出现总次数（含重叠），输出审计报告。
- 思路：扫描时沿 fail 链逐节点累加计数——直接沿链走会 O(n×depth)，优化：构建时记录 fail 树父子关系，扫描只累加当前节点计数，最后按 fail 树后序（BFS 逆序）聚合。
- 评分点：沿链计数的复杂度问题；逆 BFS 序聚合优化；重叠匹配语义。

```javascript
function acCount(text, patterns) {
  const root = buildAC(patterns);                          // 复用 ALG-423
  const nodes = [];
  (function collect(u) { nodes.push(u); for (const c of Object.values(u.children)) collect(c); })(root);
  const counter = new Map(patterns.map(p => [p, 0]));
  let node = root;
  for (let i = 0; i < text.length; i++) {
    while (node !== root && !node.children[text[i]]) node = node.fail;
    node = node.children[text[i]] ?? root;
    node.hitCount = (node.hitCount ?? 0) + 1;              // 当前节点命中计数
  }
  for (const u of [...nodes].reverse()) {                  // 逆 BFS 序聚合 fail 链
    if (u.fail && u.hitCount) u.fail.hitCount = (u.fail.hitCount ?? 0) + u.hitCount;
  }
  for (const u of nodes)
    for (const p of u.out) counter.set(p, counter.get(p) + (u.hitCount ?? 0));
  return counter;                                          // 每个敏感词总次数
}
```
