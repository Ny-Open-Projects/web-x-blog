---
title: [JS-172] 从 IIFE 命名空间到 ESM，模块化是如何演进的？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-172：从 IIFE 命名空间到 ESM，模块化是如何演进的？

**答**：
- 原始问题：多个 script 共享全局作用域，变量冲突、依赖顺序靠人肉维护。
- IIFE + 命名空间：闭包隔离私有状态，只暴露一个全局对象入口，是 ES5 时代的模块雏形。
- CommonJS：Node 的 require/module.exports，同步加载、值的拷贝；浏览器需要打包器才能用。
- ESM：编译期静态分析，导入的是「活的绑定」（live binding），天然支持 tree-shaking 与动态 import。
- 判断题眼：CJS 导出值快照，ESM 导出引用——ESM 里 inc 后再读 count 是新值，CJS 是旧值。

```javascript
// 阶段 1：全局变量污染
var utilLegacy = { format() {} };        // 任何脚本都能改写 utilLegacy

// 阶段 2：IIFE + 命名空间 —— 闭包隔离
var App = window.App || {};
App.Math = (function () {
  const rate = 0.8;                      // 私有：外部不可见、不可篡改
  return {
    discount(price) { return price * rate; },
  };
})();
console.log(App.Math.discount(100));     // 80
// console.log(App.Math.rate);           // undefined —— 私有性由闭包保证

// 阶段 3：CommonJS（Node 环境）
// const { discount } = require('./math');  同步加载
// module.exports = { discount };           值的拷贝

// 阶段 4：ESM —— 静态结构 + 活绑定
// counter.mjs
export let count = 0;
export function inc() { count += 1; }
// main.mjs
// import { count, inc } from './counter.mjs';
// inc();
// console.log(count);  // 1 —— ESM 是活引用；CJS 下拿到的永远是快照 0
```

**追问**：

1. ESM 的 live binding 遇到循环依赖会怎样？ → 可能先拿到尚未初始化的绑定，访问时抛 ReferenceError（TDZ）；要用函数延迟访问，避免在模块顶层立即求值。
2. 为什么 ESM 能做 tree-shaking 而 CJS 不行？ → ESM 的导入导出是静态结构，编译期即可确定；CJS 的 require 是运行时表达式，打包器无法静态判断用了哪些导出。
3. 打包器怎么把 CJS 交给浏览器运行？ → 用 interop 包装：把 module.exports 映射为 default 导出，并打上 `__esModule` 标记，供运行时区分。
