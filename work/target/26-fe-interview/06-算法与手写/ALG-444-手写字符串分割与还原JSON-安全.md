---
title: [ALG-444] 手写字符串分割与还原（JSON 安全复合 key）：复合键设计
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-444：手写字符串分割与还原（JSON 安全复合 key）：复合键设计

**答**：
- 题目：缓存 key 由多字段拼接（userId:orderId:page），字段本身可能含分隔符——设计「可逆分割」编码（转义或长度前缀）。
- 思路：方案 A 转义（分隔符转义 \:）；方案 B 长度前缀（len:field|）；方案 C JSON 数组序列化（可读差但无歧义）。
- 评分点：歧义场景认知；转义的成对处理（encode/decode 对称）；长度前缀最稳。

```javascript
// 方案 B：长度前缀（无歧义、无需转义）
function encodeKey(fields) {
  return fields.map(f => `${f.length}:${f}`).join('|');
}
function decodeKey(key) {
  const out = [];
  let i = 0;
  while (i < key.length) {
    const sep = key.indexOf(':', i);
    const len = +key.slice(i, sep);
    out.push(key.slice(sep + 1, sep + 1 + len));           // 按长度取，无歧义
    i = sep + 1 + len + 1;                                 // 跳过 '|'
  }
  return out;
}
// encodeKey(['user:1', 'order:2']) = '6:user:1|7:order:2'
// decodeKey 可精确还原——字段含 ':' 或 '|' 均安全
// 方案 A 转义版：escape(':') → '\\:'，decode 时按非转义 ':' 切——须成对实现
```
