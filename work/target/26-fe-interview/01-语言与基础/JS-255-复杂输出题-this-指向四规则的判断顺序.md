---
title: [JS-255] 复杂输出题：this 指向四规则的判断顺序
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, this]
type: 面试题
---

## JS-255：this 指向四规则的判断顺序

**答**：
- 优先级从高到低：① new 调用（指向新对象）② call/apply/bind（显式指定）③ 对象方法调用（指向调用者，看「谁点出来的」）④ 默认（非严格 window，严格 undefined）
- 判断口诀：先看「怎么被调」而非「在哪定义」——this 是调用点动态确定的
- 箭头函数例外：不参与以上规则，捕获「定义处外层作用域的 this」且不可改变
- 高频陷阱：方法被取出引用后调用（丢失调用者→默认规则）；回调里 this 丢失（setTimeout(obj.fn) 传引用）；类字段箭头函数绑定实例

```javascript
const obj = {
  name: 'a',
  fn() { console.log(this.name); },
  arrow: () => console.log(this?.name), // 定义处的 this（模块=undefined）
};
obj.fn();            // 'a'（规则③）
const f = obj.fn; f(); // undefined（规则④，严格）/ window.name（非严格）
obj.fn.call({ name: 'b' }); // 'b'（规则②压过③）
setTimeout(obj.fn);  // undefined —— 引用丢失调用者
```
