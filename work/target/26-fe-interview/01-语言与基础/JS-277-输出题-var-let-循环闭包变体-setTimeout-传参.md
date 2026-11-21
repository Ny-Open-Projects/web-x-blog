---
title: [JS-277] 输出题：var/let 循环闭包变体（setTimeout 传参）
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 闭包]
type: 笔试题
---

## JS-277：输出题：循环闭包变体

**题目**：四种循环 + 异步组合的输出：var/let、setTimeout 传参、IIFE、块内 await。

**答**：
```javascript
// A：var 共享槽位
for (var i = 0; i < 3; i++) setTimeout(() => console.log('A' + i));
// A3 A3 A3

// B：let 每次迭代新绑定
for (let i = 0; i < 3; i++) setTimeout(() => console.log('B' + i));
// B0 B1 B2

// C：var + setTimeout 第三参传值（复制进参数，与闭包无关）
for (var j = 0; j < 3; j++) setTimeout((x) => console.log('C' + x), 0, j);
// C0 C1 C2

// D：var + IIFE 立即捕获
for (var k = 0; k < 3; k++) ((n) => setTimeout(() => console.log('D' + n)))(k);
// D0 D1 D2

// E：let + for-await（每轮先等上轮完成，值顺序确定）
(async () => {
  for (let m = 0; m < 3; m++) {
    await new Promise(r => setTimeout(r, 10));
    console.log('E' + m);
  }
})();
// E0 E1 E2
```

**评分点**：
- var 共享 vs let 逐次绑定的机制解释
- setTimeout 第三参传值不受闭包影响——变体识别力
- IIFE 捕获当时值的等价性
- E 的串行 await 语义（每轮等待）
