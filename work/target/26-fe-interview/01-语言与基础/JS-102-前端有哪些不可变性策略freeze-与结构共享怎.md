---
title: [JS-102] 前端有哪些不可变性策略？freeze 与结构共享怎么理解？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-102：前端有哪些不可变性策略？freeze 与结构共享怎么理解？

**答**：
- Object.freeze 是浅冻结：只冻结第一层，嵌套对象仍可修改；递归 deepFreeze 才能完全只读。
- Immutable 思想：不原地修改，每次变更返回新对象，旧引用保持不变（时间旅行、React 比较优化都依赖它）。
- 结构共享：变更路径上的节点才复制，未变化的兄弟分支直接复用引用，避免整棵深拷贝。
- 工程实践：浅层用展开运算符，深层用 Immer（写时按需 copy-on-write）。

```javascript
// 1. 浅 freeze 的坑
const state = Object.freeze({ user: { name: 'a' } });
state.user.name = 'b';            // 嵌套对象没被冻结
console.log(state.user.name);     // b — 改成功了
// state.name = 'x' 会静默失败（严格模式抛错）

// 2. 递归冻结
function deepFreeze(obj) {
  if (obj && typeof obj === 'object' && !Object.isFrozen(obj)) {
    Object.freeze(obj);
    for (const v of Object.values(obj)) deepFreeze(v);
  }
  return obj;
}
deepFreeze(state);
try { state.user.name = 'c'; } catch (e) {
  console.log('冻结生效', e instanceof TypeError); // 严格模式 true
}

// 3. Immutable 思想：返回新对象，旧引用不动
const v1 = { list: [1, 2, 3], meta: { count: 3 } };
const v2 = { ...v1, list: [...v1.list, 4] };     // 只复制变更路径
console.log(v1.list.length, v2.list.length);     // 3 4
console.log(v1.meta === v2.meta);                // true — 结构共享：meta 被复用

// 4. 数组的不可变更新
const nextList = v1.list.map((n) => (n === 2 ? 99 : n)); // map/filter/concat 天然不可变
console.log(v1.list, nextList); // [1,2,3] [1,99,3]
```

## 十五、函数式编程
