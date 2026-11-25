---
title: [925] 笔试手写：实现简化版 SimHash 做文档近重复检测
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, RAG, 去重]
type: 笔试题
---

## 925：笔试手写：实现简化版 SimHash 做文档近重复检测

**需求**：实现 simhash(text, bits=64)：分词（按空格/标点简化）→ 每个 token 的 hash（提供 hashFn）→ 加权累加 → 生成 bits 位指纹。再实现 hamming(a, b) 与 nearDuplicate(a, b, maxDist=6)。同一文档两次调用结果一致（确定性）。

```js
function tokens(text) { return text.toLowerCase().split(/[\s,.;，。；]+/).filter(Boolean); }
function simhash(text, bits = 64, hashFn = fnv) {
  const v = new Array(bits).fill(0);
  for (const t of tokens(text)) {
    const h = hashFn(t);
    const w = 1; // 简化：词频加权可扩展为 w = tf
    for (let i = 0; i < bits; i++) {
      v[i] += (h >> i) & 1 ? w : -w;    // 位上加权投票
    }
  }
  let out = 0n;
  for (let i = 0; i < bits; i++) if (v[i] > 0) out |= (1n << BigInt(i));
  return out;                            // >0 的位记 1
}
function hamming(a, b) {
  let x = a ^ b, c = 0;
  while (x) { c += Number(x & 1n); x >>= 1n; }
  return c;
}
const near = (a, b, maxDist = 6) => hamming(simhash(a), simhash(b)) <= maxDist;
console.log(near('RAG 分块策略 很 重要', 'RAG 分块策略 很 重要！')); // true
```

**评分点**：
- 位投票逻辑：+1/-1 累加后按符号定 0/1，方向搞反整个指纹失效
- hamming 用异或后逐位计数，BigInt 处理不溢出
- 确定性要求：同输入同输出（禁用随机 hash）
- 能说出工程用途：爬虫文档去重、知识库重复段落合并，阈值 3~8 经验区间

