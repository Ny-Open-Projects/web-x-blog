---
title: [FRP-056] toRef / toRefs 的源码级实现是怎样的？为什么解构 reactive 会丢响应性而 toRefs 不会？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-056：toRef / toRefs 的源码级实现是怎样的？为什么解构 reactive 会丢响应性而 toRefs 不会？

**答**：
- 丢响应性的根因：`const { count } = state` 拿到的是**原始值**（get 拦截器返回的普通 number），之后与代理对象再无关系。
- `toRef(object, key)` 返回一个"引用对象"：它的 `value` getter/setter **转发到原代理对象的对应 key**——读 `r.value` 等价读 `object[key]`（触发 track），写则触发 trigger，响应性保住了。
- `toRefs(object)` 就是遍历所有 key 批量 toRef，常用于解构 props / 组合式函数返回值：`const { x, y } = toRefs(pos)`。
- 源码用 `ObjectRefImpl`（只几十行）：不建 dep，直接依赖 underlying object 的响应系统，所以它没有"自己的依赖"，只是个访问转发器；`unref/isRef` 配套用于脱壳。

```javascript
// 简化实现，帮助理解 toRef/toRefs 的转发原理
function toRef(object, key) {
  return {
    __v_isRef: true,
    get value() {
      return object[key]; // 转发读取：依然走 object 的 get 拦截器 → track
    },
    set value(newVal) {
      object[key] = newVal; // 转发写入：走 set 拦截器 → trigger
    },
  };
}

function toRefs(object) {
  const ret = {};
  for (const key in object) ret[key] = toRef(object, key);
  return ret;
}

function unref(v) { return v.__v_isRef ? v.value : v; }

const state = reactive({ count: 0, msg: 'hi' });

// 错误示范：解构拿原始值，丢失响应性
const { count: rawCount } = state;
rawCount; // 0，改 state.count 它不会变，改它也不会触发更新

// 正确：toRefs 后每个成员仍是活引用
const { count, msg } = toRefs(state);
effect(() => console.log('count =', count.value)); // count = 0
count.value = 5;          // 转发写回 state.count，effect 重跑
console.log(state.count); // 5
console.log(unref(msg));  // hi
```
