---
title: [ALG-426] 手写 Z 函数：重复片段检测
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-426：手写 Z 函数：重复片段检测

**答**：
- 题目：检测用户昵称的重复模式（如「abcabcabc」由「abc」重复 3 次），或找「文本与自身后缀的最长公共前缀」。Z 函数：z[i] = 后缀 i 与原串的 LCP。
- 思路：维护窗口 [l, r]（最右匹配段）；i 在窗口内 → 初始 z[i] = min(z[i-l], r-i+1) 再暴力扩展；否则直接扩展。O(n)。
- 评分点：z-box 窗口复用；与 KMP next 的等价转换；周期检测（n % (n - z[n-1]·) == 0 判周期）。

```javascript
function zFunction(s) {
  const z = new Array(s.length).fill(0);
  z[0] = s.length;
  let l = 0, r = 0;                                        // z-box 窗口
  for (let i = 1; i < s.length; i++) {
    if (i <= r) z[i] = Math.min(z[i - l], r - i + 1);      // 窗口内：复用已知信息
    while (i + z[i] < s.length && s[z[i]] === s[i + z[i]]) z[i]++;   // 暴力扩展
    if (i + z[i] - 1 > r) { l = i; r = i + z[i] - 1; }     // 更新窗口
  }
  return z;
}
function isRepetitive(nick) {                              // 重复模式检测
  const z = zFunction(nick);
  for (let len = 1; len < nick.length; len++) {
    if (nick.length % len) continue;
    const ok = z[len] >= nick.length - len;                // 后缀与前缀 LCP 足够长
    if (ok) return { period: len, repeat: nick.length / len };
  }
  return null;
}
```
