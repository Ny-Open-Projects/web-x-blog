---
title: [JS-159] 对象引用与浅比较在框架 diff 中扮演什么角色？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-159：对象引用与浅比较在框架 diff 中扮演什么角色？

**答**：
- JS 对象赋值是引用传递：改 `b.x` 连 `a.x` 一起变，框架 diff 对比引用发现「没变」，UI 不更新——这是状态不更新的头号原因。
- 浅比较（`===` 逐键比第一层）是 React.memo、shouldComponentUpdate 的核心，引用相等直接跳过渲染。
- 不可变更新：不原地修改，而是 `{...state, list: [...state.list, item]}` 换引用，让浅比较检测到变化。
- 深比较能识别内容变化但 O(n) 昂贵，框架默认不用；需要深语义时用 Immer 类库以「写时复制」实现。

```javascript
// 1. 引用赋值是同一个对象
const a = { x: 1 };
const b = a;
b.x = 2;
console.log(a.x);        // 2 —— a、b 是同一引用
console.log(a === b);    // true

// 2. 浅比较：React.memo / shouldComponentUpdate 的核心
function shallowEqual(o1, o2) {
  if (o1 === o2) return true;                        // 引用相等直接通过
  if (typeof o1 !== 'object' || typeof o2 !== 'object') return false;
  const k1 = Object.keys(o1), k2 = Object.keys(o2);
  if (k1.length !== k2.length) return false;
  return k1.every((k) => o1[k] === o2[k]);           // 只比第一层
}

// 3. 不可变更新让浅比较生效
const state = { list: [1, 2] };
const next1 = { ...state, list: [1, 2] };            // 浅拷贝 + 新壳
console.log(shallowEqual(state, next1));             // true → 跳过渲染（内容相同）
const next2 = { ...state, list: [1, 2, 3] };         // 换数组引用
console.log(shallowEqual(state, next2));             // false → 触发重渲染

// 4. 原地修改是 bug 之源
const arr = [1, 2];
const copy = arr;
arr.push(3);                                         // 原地修改
console.log(copy.length, arr === copy);              // 3 true —— copy 被连带改动，diff 检测不到
```

## 二十三、DOM 与事件深入
