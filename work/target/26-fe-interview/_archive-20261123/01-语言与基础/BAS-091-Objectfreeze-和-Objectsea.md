---
title: [BAS-091] Object.freeze 和 Object.seal 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-091：Object.freeze 和 Object.seal 有什么区别？
**答**：
- seal 密封：不能增删属性，已有属性值仍可改；freeze 冻结：在 seal 基础上值也不可改（writable 变 false）。
- 两者都是浅操作：嵌套对象内部不受影响，深冻结需递归处理。
- 严格模式下修改冻结对象抛 TypeError；冻结的数组不能 push。

```javascript
'use strict';
const s = Object.seal({ a: 1 });
s.a = 10;            // 允许：seal 只封结构
// s.newKey = 1;     // TypeError：不能新增属性
const f = Object.freeze({ nested: { b: 2 } });
// f.nested = {};    // TypeError
f.nested.b = 99;     // 浅冻结：内部对象照样能改
console.log(f.nested.b);  // 99
```
