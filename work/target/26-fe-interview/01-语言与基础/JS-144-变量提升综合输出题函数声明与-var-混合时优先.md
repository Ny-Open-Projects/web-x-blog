---
title: [JS-144] 变量提升综合输出题？函数声明与 var 混合时优先级如何？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-144：变量提升综合输出题？函数声明与 var 混合时优先级如何？

**答**：
- var 声明提升（值为 undefined），函数声明整体提升（声明+赋值一起），所以 `typeof fn` 在声明前就是 function。
- 同名冲突：函数声明优先于 var 声明提升；随后执行阶段的赋值会覆盖函数。
- 函数表达式只提升变量声明部分，赋值留在原地，声明前调用是 TypeError。
- 块级作用域中的函数声明在非严格模式下按 var 语义处理（Annex B 历史遗留），会泄漏到块外。

```javascript
console.log(typeof a);          // undefined：var a 声明提升但未赋值
var a = 1;
console.log(typeof b);          // function：函数声明整体提升
function b() { return 'b'; }
console.log(typeof c);          // undefined：函数表达式只提升 var c
var c = function () { return 'c'; };
console.log(typeof c);          // function：赋值已执行

// 经典陷阱：函数声明 vs 函数表达式同名
console.log(fn());              // 'declared'：函数声明优先提升，此时 fn 还是函数
var fn = function () { return 'expression'; };
function fn() { return 'declared'; }
console.log(fn());              // 'expression'：执行阶段的赋值覆盖了函数

// 块内函数声明（Annex B）：非严格模式下按 var 语义泄漏到块外
{
  function blockFn() {}
}
console.log(typeof blockFn);    // function（浏览器非严格实现）；严格模式下块级函数声明只在块内可见，这里输出 "undefined"
```
