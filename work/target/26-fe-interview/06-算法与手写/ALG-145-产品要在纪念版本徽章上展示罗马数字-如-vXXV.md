---
title: [ALG-145] 产品要在"纪念版本"徽章上展示罗马数字（如 v.XXV），并解析历史版本的罗马数字编号。如何互转？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-145：产品要在"纪念版本"徽章上展示罗马数字（如 v.XXV），并解析历史版本的罗马数字编号。如何互转？
**答**：转罗马：贪心——从大到小遍历面值表（含 900/400/90/40/9/4 这些"小减大"组合），能减就减并拼接。转数字：从左到右累加，若当前字符值小于后一位则做减法（IV = -1 + 5）。O(1)（面值表固定）。

```javascript
const table = [[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],
               [50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']];
function toRoman(n) {
  let s = '';
  for (const [v, sym] of table) {
    while (n >= v) { s += sym; n -= v; } // 贪心：大面值优先
  }
  return s;
}
function fromRoman(s) {
  const map = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
  let n = 0;
  for (let i = 0; i < s.length; i++) {
    // 小值在大值左侧 => 做减法（IV、IX、XL...）
    n += map[s[i]] < (map[s[i + 1]] || 0) ? -map[s[i]] : map[s[i]];
  }
  return n;
}
// toRoman(2026) => 'MMXXVI'；fromRoman('XXV') => 25
```
