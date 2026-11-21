---
title: [JS-111] BigInt 如何用于金额处理？有哪些限制？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-111：BigInt 如何用于金额处理？有哪些限制？

**答**：
- Number 的安全整数上限是 2^53-1，超过即精度丢失，金额/ID 大数必须用 BigInt。
- BigInt 只能表示整数，除法向零截断；金额应先统一转“最小单位（分）”的 BigInt 再运算。
- BigInt 与 Number 不能混算（抛 TypeError），需显式 BigInt()/Number() 转换。
- JSON.stringify 不支持 BigInt，序列化前要转字符串；展示时再做格式化。

```javascript
console.log(Number.MAX_SAFE_INTEGER); // 9007199254740991
console.log(9007199254740993 === 9007199254740992); // true — 精度丢失！
const big = 9007199254740993n;
console.log(big + 1n === 9007199254740994n); // true — BigInt 精确

// 混算限制
try { big + 1; } catch (e) { console.log(e instanceof TypeError); } // true
console.log(big + BigInt(1)); // 9007199254740994n

// 金额计算：以"分"为单位的 BigInt，展示时转字符串
function fenToYuan(fen) {
  const sign = fen < 0n ? '-' : '';
  const abs = fen < 0n ? -fen : fen;
  return `${sign}${abs / 100n}.${String(abs % 100n).padStart(2, '0')}`;
}
console.log(fenToYuan(123456789012345678n)); // 1234567890123456.78

// 除法截断：必须先统一单位
console.log(1n / 2n); // 0n — 不是 0.5n

// JSON 序列化：先转字符串
const order = { id: big, amountFen: '123456789012345678' };
console.log(JSON.stringify(order));
```
