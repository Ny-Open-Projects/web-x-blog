---
title: [HW-012] 手写 new
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-012：手写 new

**答**：
- 评分点：new 做的四件事要说全——① 创建空对象并把原型指向构造函数的 prototype；② 以该对象为 this 执行构造函数；③ 构造函数若**显式返回对象或函数**，则覆盖默认实例（返回原始值会被忽略）；④ 返回实例。用 `Object.create(Ctor.prototype)` 一步完成原型挂载；判断返回值要用 `typeof === 'object' | 'function'` 且非 null。

```javascript
// ===== 5 分钟速写版 =====
function myNew(Ctor, ...args) {
  const obj = Object.create(Ctor.prototype); // ① ②合并：空对象 + 原型链
  const res = Ctor.apply(obj, args);         // ② this 绑定为新对象
  // ③ 返回对象/函数则覆盖，否则返回实例
  return res !== null && (typeof res === 'object' || typeof res === 'function') ? res : obj;
}

// ===== 标准完整版（含边界处理）=====
function myNewPro(Ctor, ...args) {
  if (typeof Ctor !== 'function') {
    throw new TypeError('Ctor must be a constructor function');
  }
  // Object.create 同时处理了 Ctor.prototype 为对象与 null 两种情况：
  // 为 null 时实例没有原型，仍可正常创建
  const obj = Object.create(Ctor.prototype);
  let res;
  try {
    res = Ctor.apply(obj, args);   // 构造函数内部 throw 时，new 表达式同样向上抛
  } catch (e) {
    throw e;
  }
  const isOverride = res !== null && (typeof res === 'object' || typeof res === 'function');
  return isOverride ? res : obj;
}
// 验证：
// function Person(name) { this.name = name; }
// myNewPro(Person, 'Tom').name === 'Tom'，且 instanceof Person 为 true
// function Weird() { return { custom: 1 }; } → myNewPro(Weird).custom === 1
// function Prim() { return 42; } → myNewPro(Prim) 是实例而非 42
```

---
