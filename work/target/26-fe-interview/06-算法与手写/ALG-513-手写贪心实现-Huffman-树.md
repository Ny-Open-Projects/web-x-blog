---
title: [ALG-513] 手写贪心实现 Huffman 树：编码压缩
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-513：手写贪心实现 Huffman 树：编码压缩

**答**：
- 题目：字符频次表，构造 Huffman 编码（高频短码），输出编码表与压缩率估算。贪心：小顶堆每次合并最小两个。
- 思路：与 ALG-499 同构——堆合并，合并节点为内部节点；编码 = 根到叶路径（左 0 右 1）。
- 评分点：堆合并构造；编码路径生成；压缩率计算（Σ频次×码长 / 原始 8bit×n）。

```javascript
function huffman(freqs) {                                  // freqs: {char: freq}
  const heap = new MinHeap(Object.entries(freqs)
    .map(([c, f]) => ({ f, nodes: [{ c }] })));             // {f, nodes}
  while (heap.size > 1) {
    const a = heap.pop(), b = heap.pop();
    heap.push({ f: a.f + b.f, nodes: [...a.nodes, ...b.nodes], children: [a, b] });
  }
  const codes = {};
  const walk = (node, path) => {
    if (node.nodes.length === 1 && node.c) { codes[node.c] = path || '0'; return; }
    node.children?.forEach((ch, i) => walk(ch, path + i));
  };
  const root = heap.pop();
  walk(root, '');
  const totalBits = Object.entries(freqs)
    .reduce((s, [c, f]) => s + f * codes[c].length, 0);
  const rawBits = Object.values(freqs).reduce((s, f) => s + f, 0) * 8;
  return { codes, compression: +(totalBits / rawBits).toFixed(3) };   // 压缩率
}
// 例：a:45 b:13 c:12 d:16 e:9 f:5 → 前缀码压缩率约 0.69
```
