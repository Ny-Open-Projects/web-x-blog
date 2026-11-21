---
title: [JS-062] Reflect 是什么？为什么要与 Proxy 配合？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-062：Reflect 是什么？为什么要与 Proxy 配合？

**答**：
- Reflect 把对象操作函数化：get/set/has/deleteProperty/defineProperty 等，返回值更友好（失败返回 false 而不报错）。
- 与 Proxy 配合：trap 内用 Reflect 执行默认行为，能正确传递 receiver、保证 this 与 getter 语义。
- 让“拦截 + 默认行为”的写法规范化，避免手动复制逻辑。
- 也用于探测：`Reflect.has(obj, key)` 等价 `key in obj`。

```javascript
const handler = {
  get(target, key, receiver) {
    if (!(key in target)) {
      console.warn(`missing key: ${String(key)}`);
      return undefined;
    }
    return Reflect.get(target, key, receiver); // 保持 receiver 语义
  },
  set(target, key, value, receiver) {
    if (typeof value === 'function') {
      throw new TypeError('not allowed');
    }
    return Reflect.set(target, key, value, receiver);
  },
};
const proxy = new Proxy({ a: 1 }, handler);
proxy.a;            // 1
proxy.missing;      // warn
// proxy.fn = () => {}; // TypeError

console.log(Reflect.has(proxy, 'a'));       // true
console.log(Reflect.ownKeys(proxy));        // ['a']，含 symbol
```
