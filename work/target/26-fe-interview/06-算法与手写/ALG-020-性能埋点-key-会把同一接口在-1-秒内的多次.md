---
title: [ALG-020] 性能埋点 key 会把同一接口在 1 秒内的多次调用拼成 `aabbcc` 形式，需要压缩成 `a2b2c2` 减少上报体积；若压缩后更长则保留原串。如何实现？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-020：性能埋点 key 会把同一接口在 1 秒内的多次调用拼成 `aabbcc` 形式，需要压缩成 `a2b2c2` 减少上报体积；若压缩后更长则保留原串。如何实现？
**答**：线性扫描，统计连续相同字符个数，遇到不同字符时把"字符 + 个数"写入结果。注意压缩后可能变长（如 `abc` → `a1b1c1`），最后比较长度取较短者。时间 O(n)，空间 O(n)。

```javascript
function compress(str) {
  if (!str) return str;
  let res = '', count = 1;
  for (let i = 1; i <= str.length; i++) {
    if (str[i] === str[i - 1]) {
      count++;
    } else {
      res += str[i - 1] + count;
      count = 1;
    }
  }
  return res.length < str.length ? res : str; // 变长则退回原串
}
// compress('aabbccddddd') => 'a2b2c2d5'
```

---

## 三、树结构
