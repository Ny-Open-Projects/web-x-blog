---
title: [JS-274] 输出题：this 综合（对象方法/箭头/call）
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, this]
type: 笔试题
---

## JS-274：输出题：this 综合

**题目**：覆盖「方法调用、箭头捕获、call/apply、嵌套对象、类字段」的 this 判定，写出输出。

**答**：
```javascript
const obj = {
  name: 'outer',
  normal() { console.log(this.name); },
  arrow: () => console.log(this?.name),
  nested() {
    const inner = { name: 'inner', fn: this.normal };
    inner.fn();                       // ？
    setTimeout(() => console.log(this.name), 0); // ？
  },
};
obj.normal();          // 'outer'（③ 方法调用）
obj.arrow();           // undefined（箭头捕获定义处 this = 模块顶层）
const ref = obj.normal;
ref();                 // undefined / window.name（④ 默认）
obj.normal.call({ name: 'call' }); // 'call'（② 显式）
obj.nested();
// inner.fn() → 'outer'（fn 是 obj.normal 的引用，但调用点是 inner.fn
//   ——等等，inner 上没有 name... fn 指向 obj.normal，调用者是 inner，
//   this = inner，inner.name = 'inner' → 输出 'inner'）
// 箭头 → 'outer'（捕获 nested 定义处 this = obj）
```

**评分点**：
- 调用点判定（inner.fn() 的 this 是 inner，输出 inner）
- 箭头函数捕获定义处作用域（模块顶层 undefined）
- call 显式绑定优先于方法调用
- 解引用丢失调用者的默认规则
