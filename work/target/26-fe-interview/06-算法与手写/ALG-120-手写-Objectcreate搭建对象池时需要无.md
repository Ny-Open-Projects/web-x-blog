---
title: [ALG-120] 手写 Object.create：搭建对象池时需要"无构造副作用地继承某个原型"，还要支持第二参数的属性描述符？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-120：手写 Object.create：搭建对象池时需要"无构造副作用地继承某个原型"，还要支持第二参数的属性描述符？
**答**：核心是临时构造函数桥接：`F.prototype = proto; new F()`——既挂上原型，又不执行任何用户构造逻辑。第二参数用 `Object.defineProperties` 处理属性描述符。注意 proto 为 null 时 F 的原型链会带 Object.prototype，需用 `__proto__`（或 `Object.setPrototypeOf`）置空。时间 O(1)。

```javascript
function objectCreate(proto, props) {
  if (proto === null) {
    // null 原型：new F() 必带 Object.prototype，需单独置空
    const bare = {};
    Object.setPrototypeOf(bare, null);
    if (props) Object.defineProperties(bare, props);
    return bare;
  }
  function F() {}            // 临时构造函数，无副作用
  F.prototype = proto;
  const obj = new F();
  if (props) Object.defineProperties(obj, props); // 支持 { key: { value, writable... } }
  return obj;
}
// const pool = objectCreate({ reset() { this.inUse = false; } }, { inUse: { value: false, writable: true } });
```
