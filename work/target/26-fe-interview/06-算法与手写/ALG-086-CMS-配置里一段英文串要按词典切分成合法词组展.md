---
title: [ALG-086] CMS 配置里一段英文串要按词典切分成合法词组展示（单词拆分：能否用词典中的词完整拼出字符串）。如何 DP？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-086：CMS 配置里一段英文串要按词典切分成合法词组展示（单词拆分：能否用词典中的词完整拼出字符串）。如何 DP？
**答**：`dp[i]` 表示前 i 个字符能否被词典切分：枚举最后一个词的起点 j，`dp[j] && 词典含 s.slice(j, i)` 则 `dp[i] = true`。内层循环可只枚举词典里的词长优化。时间 O(n²)（可优化 O(n × 最长词长)），空间 O(n)。

```javascript
function wordBreak(s, dict) {
  const set = new Set(dict);
  const dp = new Array(s.length + 1).fill(false);
  dp[0] = true; // 空串可切分
  for (let i = 1; i <= s.length; i++) {
    for (let j = 0; j < i; j++) {
      if (dp[j] && set.has(s.slice(j, i))) { dp[i] = true; break; }
    }
  }
  return dp[s.length];
}
// wordBreak('vueandreact', ['vue', 'react', 'and']) => true
```

---

## 十、图与综合
