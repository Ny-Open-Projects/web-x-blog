---
title: [ALG-447] 手写字符串转数字（atoi 全边界）：表单解析健壮性
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-447：手写字符串转数字（atoi 全边界）：表单解析健壮性

**答**：
- 题目：手写 atoi：跳过前导空格、正负号、数字截断、溢出钳制（INT_MAX/MIN）、非法输入返回 0。考边界完备性。
- 思路：状态扫描逐段处理；溢出判定在「乘 10 前」判 cur > (MAX - d) / 10，避免溢出后判。
- 评分点：五类边界齐全；溢出判定时机（乘 10 前）；空串/纯符号/非数字开头。

```javascript
function myAtoi(s) {
  const INT_MAX = 2147483647, INT_MIN = -2147483648;
  let i = 0, sign = 1, num = 0;
  while (i < s.length && s[i] === ' ') i++;                // 1. 前导空格
  if (s[i] === '+' || s[i] === '-') sign = s[i++] === '-' ? -1 : 1;   // 2. 符号
  while (i < s.length && s[i] >= '0' && s[i] <= '9') {     // 3. 数字
    const d = +s[i++];
    if (num > (INT_MAX - d) / 10)                          // 4. 溢出：乘 10 前判
      return sign === 1 ? INT_MAX : INT_MIN;
    num = num * 10 + d;
  }
  return sign * num;
}
// 边界用例：'  -42' → -42；'4193 with words' → 4193；'words 98' → 0；
// '-91283472332' → INT_MIN（钳制）；'+-12' → 0；'' → 0
```
