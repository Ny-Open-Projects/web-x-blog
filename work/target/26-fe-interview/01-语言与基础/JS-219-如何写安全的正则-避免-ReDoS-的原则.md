---
title: [JS-219] 如何写安全的正则：避免 ReDoS 的原则
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 正则]
type: 面试题
---

## JS-219：如何写安全的正则：避免 ReDoS 的原则

**答**：
- 原则一：禁嵌套量词（量词内不含量词组）；原则二：交替分支不重叠（`(a|ab)*` 是雷）；原则三：贪婪量词后不要紧跟可选量词
- 工程防线：用户输入进正则前必限长度；用 new RegExp 时检查来源（拼接用户输入=注入+ReDoS 双风险）
- 工具：safe-regex2/recheck 静态分析；运行时用 node 的 `--max-regexp-length` 或沙箱超时
- 兜底方案：超复杂解析放弃正则，手写状态机（线性时间有保证）——tokenizer 永远比「超级正则」安全

```javascript
// 危险：用户输入拼进正则
const q = userInput;                       // 可能含 .*(((((((...
// new RegExp(`search:${q}`)               // ❌ 注入 + ReDoS
const safeQ = q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); // 转义元字符
const re = new RegExp(`search:${safeQ}`, 'u');
if (safeQ.length > 100) return; // 长度闸门
```
