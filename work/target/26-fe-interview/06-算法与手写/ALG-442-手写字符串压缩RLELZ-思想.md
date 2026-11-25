---
title: [ALG-442] 手写字符串压缩（RLE/LZ 思想）：上报体积压缩
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-442：手写字符串压缩（RLE/LZ 思想）：上报体积压缩

**答**：
- 题目：埋点事件序列上报体积大——先做轻量压缩：RLE（连续重复压缩）+ 字典替换（高频词编号）。
- 思路：RLE：连续相同事件折叠为 count×event；字典：高频 token 建表，正文存编号。评估压缩率与解压成本。
- 评分点：RLE 适用场景（重复多）；字典替换；压缩率测量与 CPU 成本权衡。

```javascript
function compressEvents(events) {                          // 埋点序列轻量压缩
  // 1) 字典替换：高频事件类型编号
  const dict = new Map();
  const encode = (e) => {
    if (!dict.has(e.type)) dict.set(e.type, dict.size);
    return dict.get(e.type);
  };
  const codes = events.map(encode);
  // 2) RLE：连续相同编号折叠
  const rle = [];
  for (let i = 0; i < codes.length;) {
    let j = i;
    while (j < codes.length && codes[j] === codes[i]) j++;
    rle.push(j - i > 1 ? `${j - i}x${codes[i]}` : String(codes[i]));
    i = j;
  }
  return { payload: rle.join(','), dict: [...dict.keys()] };   // 解压 = 展开编号
}
// 压缩率测量：payload.length vs 原始 JSON 长度；CPU 成本 O(n)
// 大批量再上 gzip/pako——应用层压缩与传输压缩叠加的收益评估
```
