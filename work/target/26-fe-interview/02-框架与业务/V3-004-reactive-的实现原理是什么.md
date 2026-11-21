---
title: [V3-004] reactive 的实现原理是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-004：reactive 的实现原理是什么？
**答**：
- reactive 返回原对象的 Proxy，拦截 get/set/deleteProperty/has/ownKeys 等操作。
- get 里调用 track 收集依赖，set/delete 里调用 trigger 派发更新。
- 嵌套对象采用惰性深代理：get 时才对属性值递归调用 reactive，避免初始化遍历整棵树。
- set 时对比新旧值、判断 key 是否新增（hadKey），决定按 ADD/SET/DELETE 哪种类型 trigger。

```javascript
function reactive(obj) {
  return new Proxy(obj, {
    get(target, key, receiver) {
      track(target, key);
      const value = Reflect.get(target, key, receiver);
      // 惰性深代理：访问到对象属性时才递归转换
      if (typeof value === "object" && value !== null) {
        return reactive(value);
      }
      return value;
    },
    set(target, key, value, receiver) {
      const old = target[key];
      const hadKey = key in target;
      const result = Reflect.set(target, key, value, receiver);
      if (!hadKey) {
        trigger(target, key, "add"); // 新增属性也要触发
      } else if (old !== value) {
        trigger(target, key, "set");
      }
      return result;
    },
    deleteProperty(target, key) {
      const hadKey = key in target;
      const result = Reflect.deleteProperty(target, key);
      if (hadKey) trigger(target, key, "delete");
      return result;
    },
  });
}
```
