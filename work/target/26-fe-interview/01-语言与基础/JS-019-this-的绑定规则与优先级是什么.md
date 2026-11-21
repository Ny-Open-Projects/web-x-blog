---
title: [JS-019] this 的绑定规则与优先级是什么？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-019：this 的绑定规则与优先级是什么？

**答**：
- 四条规则：默认绑定（非严格 window、严格 undefined）、隐式绑定（obj.fn() 指向 obj）、显式绑定（call/apply/bind）、new 绑定。
- 优先级：new > 显式 > 隐式 > 默认；箭头函数没有自己的 this，定义时捕获外层。
- 隐式丢失最常见：把对象方法赋给变量或作为回调传入，this 变回默认绑定。
- 排查口诀：先看调用形式，再看是否箭头函数，最后看是否被 bind 过。

```javascript
function show() { console.log(this); }

show();                     // window（严格模式 undefined）
const obj = { name: 'obj', show };
obj.show();                 // obj，隐式绑定

const lost = obj.show;
lost();                     // window，隐式丢失

const bound = show.bind({ name: 'bound' });
new bound();                // {name:'bound'} 的实例？new 优先于 bind，
                            // this 是新创建的实例

setTimeout(obj.show, 100);  // window，作为回调丢失
setTimeout(() => obj.show(), 100); // obj，箭头包裹保住隐式绑定
```
