---
title: [HW-013] 手写 instanceof
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-013：手写 instanceof

**答**：
- 评分点：本质是沿 `Object.getPrototypeOf(left)` 的原型链逐层向上，与 `right.prototype` 比对；右侧必须是函数（构造函数/class），否则直接 false（注意 `typeof right !== 'function'` 这层校验，许多人漏掉）；终止条件是原型链到 null；能提一句 ES6 的 `Symbol.hasInstance` 可自定义 instanceof 行为是加分项。

```javascript
// ===== 5 分钟速写版 =====
function myInstanceof(left, right) {
  let proto = Object.getPrototypeOf(left);
  while (proto !== null) {
    if (proto === right.prototype) return true;
    proto = Object.getPrototypeOf(proto);
  }
  return false;
}

// ===== 标准完整版（含边界处理）=====
function myInstanceofPro(left, right) {
  // 右侧必须是可实例化的函数（含 class）；包装对象场景下 String 等也合法
  if (right === null || typeof right !== 'function') {
    throw new TypeError('right-hand side must be a constructor');
  }
  if (left === null || (typeof left !== 'object' && typeof left !== 'function')) {
    return false; // 原始值不在原型链上（除 Symbol.hasInstance 自定义外）
  }
  // 兼容 ES6 自定义 instanceof 行为。注意：Function.prototype 上有默认
  // Symbol.hasInstance（普通函数沿原型链继承到它），所以必须用「自有属性」判断，
  // 否则该分支永远命中，下面的手写遍历就成了死代码。
  if (Object.getOwnPropertyDescriptor(right, Symbol.hasInstance)) {
    return !!right[Symbol.hasInstance](left);
  }
  let proto = Object.getPrototypeOf(left);
  while (proto !== null) {
    if (proto === right.prototype) return true;
    proto = Object.getPrototypeOf(proto);
  }
  return false;
}
// 追问点：
// myInstanceofPro([], Array) === true; myInstanceofPro([], Object) === true（原型链多级命中）
// myInstanceofPro('abc', String) === false（原始值），new String('abc') 则为 true
```

---
