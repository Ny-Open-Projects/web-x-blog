---
title: [ALG-108] 分账系统金额以字符串传来，累加结果超过 Number.MAX_SAFE_INTEGER（约 9e15），浮点还会丢精度。如何精确实现大数加法（含小数）？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-108：分账系统金额以字符串传来，累加结果超过 Number.MAX_SAFE_INTEGER（约 9e15），浮点还会丢精度。如何精确实现大数加法（含小数）？
**答**：按字符串逐位相加：两数右对齐（小数部分 padEnd 补齐），从最低位开始加并用 carry 进位，最后处理剩余进位。时间 O(len)，空间 O(len)。工程上更推荐金额全程用「分」的整数或 BigInt 运算（见 ALG-200），逐位加法是面试标准答案。

```javascript
function addBigNumber(a, b) {
  const [ia, fa = ''] = a.split('.'), [ib, fb = ''] = b.split('.');
  const fl = Math.max(fa.length, fb.length);          // 小数位对齐
  const A = (ia + fa.padEnd(fl, '0')).split('').reverse();
  const B = (ib + fb.padEnd(fl, '0')).split('').reverse();
  const res = [];
  let carry = 0;
  for (let i = 0; i < Math.max(A.length, B.length); i++) {
    const sum = (+A[i] || 0) + (+B[i] || 0) + carry;
    res.push(sum % 10);
    carry = sum > 9 ? 1 : 0;
  }
  if (carry) res.push(1);
  let s = res.reverse().join('');
  const intPart = fl ? (s.slice(0, -fl) || '0') : s;
  return intPart + (fl ? '.' + s.slice(-fl) : '');
}
// addBigNumber('9007199254740993.99', '0.02') => '9007199254740994.01'
// Number 版会得到 9007199254740994 但精度已不可靠
```

## 十二、高频手写综合

> ALG-109 ~ ALG-121：大厂手写题的高频区——Promise 家族、async/await 语义还原、this 显式绑定三件套、new/instanceof/Object.create/flatMap。考察点不是背代码，而是背后的语言机制。
