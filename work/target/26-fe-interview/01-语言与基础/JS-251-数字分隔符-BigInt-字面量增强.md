---
title: [JS-251] 数字分隔符、BigInt 与字面量增强
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 语法]
type: 面试题
---

## JS-251：数字分隔符、BigInt 与字面量增强

**答**：
- 数字分隔符 `_`：`1_000_000_000`——长数字可读性（ES2021）
- BigInt：`123n` 或 BigInt('123')——超过 Number.MAX_SAFE_INTEGER（2^53-1）的整数计算；与 Number 混算报 TypeError
- 应用场景：雪花 ID、大金额（分）、加密计算、64 位哈希——后端 Long 型字段到前端必用（JSON.parse 丢精度！）
- 其他增强：二进制 0b / 八进制 0o / 十六进制 0x 的组合书写；Number.EPSILON 用于浮点比较
- BigInt 序列化坑：JSON.stringify 不支持 BigInt——需 toJSON 或字符串化传输

```javascript
const snowflake = 724319528506361857n;
Number(snowflake);                 // 724319528506361800 —— 已丢精度！
// 服务端把 Long 输出为字符串，前端 BigInt() 还原
const id = BigInt('724319528506361857');
id + 1n;      // ✅
id + 1;       // ❌ TypeError: Cannot mix BigInt and Number
JSON.stringify({ id: id.toString() }); // 手动字符串化
```
