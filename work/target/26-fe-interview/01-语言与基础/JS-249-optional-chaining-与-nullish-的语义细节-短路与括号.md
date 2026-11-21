---
title: [JS-249] optional chaining 与 nullish 的语义细节
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 语法]
type: 面试题
---

## JS-249：optional chaining 与 nullish 的语义细节

**答**：
- ?. 短路条件：只对 null/undefined 短路——0、''、false 照常执行（与 && 链的本质区别）
- 三种形态：a?.b（属性）、a?.()（调用，存在才调）、a?.[k]（动态键）；delete obj?.key 也合法
- 短路范围：`a?.b.c` 中 a 短路则整条链返回 undefined，但 `a.b?.c` 只保护 c 段——边界要明确
- 与 ?? 组合：`(a?.b) ?? 默认`——注意 ?. 返回 undefined 时 ?? 才生效；加括号防 `??` 与 `||` 混用语法错误
- 陷阱：?. 后面接函数调用 `obj?.fn()` 只保护 obj，fn 本身为 undefined 时仍报错（需 obj?.fn?.()）

```javascript
const user = null;
user?.profile?.name;      // undefined，不报错
const v = 0;
v?.toString();            // "0" —— 0 不短路
const o = {};
o.fn?.();                 // undefined（o.fn 不存在）
o.fn();                   // ❌ TypeError
(o.a ?? b)?.c;            // 括号明确短路边界
```
