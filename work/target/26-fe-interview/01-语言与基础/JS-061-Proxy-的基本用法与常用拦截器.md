---
title: [JS-061] Proxy 的基本用法与常用拦截器？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-061：Proxy 的基本用法与常用拦截器？

**答**：
- `new Proxy(target, handler)` 创建代理，外部操作先经过 handler 拦截。
- 常用 trap：get/set/has/deleteProperty/ownKeys/apply/construct。
- set 里可做校验与通知，是响应式系统（Vue3）的基础。
- 拦截的是代理对象上的操作，直接持有原 target 可绕过代理。

```javascript
function reactive(obj) {
  return new Proxy(obj, {
    get(target, key, receiver) {
      console.log(`get ${String(key)}`);
      return Reflect.get(target, key, receiver);
    },
    set(target, key, value, receiver) {
      const ok = Reflect.set(target, key, value, receiver);
      console.log(`set ${String(key)} = ${value}，触发更新`);
      return ok;
    },
    deleteProperty(target, key) {
      console.log(`delete ${String(key)}`);
      return Reflect.deleteProperty(target, key);
    },
  });
}

const state = reactive({ count: 0, user: { name: 'Tom' } });
state.count = 1;        // set count = 1，触发更新
state.user.name;        // get user（深层需要递归代理，Vue3 惰性处理）
delete state.count;
```
