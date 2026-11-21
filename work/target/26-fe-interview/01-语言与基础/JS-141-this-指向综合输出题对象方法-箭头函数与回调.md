---
title: [JS-141] this 指向综合输出题？对象方法、箭头函数与回调三层嵌套怎么判断？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-141：this 指向综合输出题？对象方法、箭头函数与回调三层嵌套怎么判断？

**答**：
- 判断顺序：看调用方式（谁调用指向谁）→ 箭头函数继承外层 this → 定时器回调中的普通函数独立调用。
- 箭头函数的 this 在定义时就固定为外层词法作用域的 this，与执行位置无关。
- 普通函数回调（如 `setTimeout(function(){})`）独立调用时，非严格指向 globalThis，严格为 undefined。
- 方法被提取赋值后再调用，this 丢失，回到独立调用规则。
- 输出顺序还需考虑宏任务：嵌套 `setTimeout` 的回调要等当前任务全部执行完才运行。

```javascript
const user = {
  name: 'outer',
  say() {
    console.log(1, this.name);          // user.say() → this 是 user → outer
    setTimeout(() => {
      console.log(2, this.name);        // 箭头函数继承 say 的 this → outer
      setTimeout(function () {
        console.log(3, this.name);      // 普通函数独立调用 → globalThis.name（浏览器为 ''，Node 为 undefined）
      }, 0);
      const inner = {
        name: 'inner',
        run() {
          console.log(4, this.name);    // inner.run() → inner
          const arrow = () => console.log(5, this.name); // 箭头继承 run 的 this → inner
          arrow();
          console.log(6, this.name);    // 仍是 run 的 this → inner
        },
      };
      inner.run();
      // 方法提取后独立调用：this 丢失（放在 run 外部调用，放 run 内部会无限递归调自己）
      const stolen = inner.run;
      stolen();
    }, 0);
  },
};
user.say();
// 输出顺序（非严格全局脚本）：
// 1 outer → 2 outer → 4 inner → 5 inner → 6 inner
// → 4 undefined → 5 undefined → 6 undefined → 3 undefined
// 关键：stolen() 独立调用后 this 丢失指向 globalThis，run 的三行 4/5/6 全部按丢失后的 this 再打一遍、
//       this.name 是 globalThis.name（Node 为 undefined；浏览器 window.name 默认是 ''）
// 第 3 行在嵌套宏任务中，要等当前定时器回调（2~7 行所在任务）完全结束后才执行
// 严格模式陷阱：ESM/class 内 stolen() 的 this 是 undefined，4 处直接 TypeError——严格化本身就是追问点
```
