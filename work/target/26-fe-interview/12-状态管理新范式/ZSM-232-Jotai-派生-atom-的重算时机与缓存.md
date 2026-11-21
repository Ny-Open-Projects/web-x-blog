---
title: [ZSM-232] Jotai 派生 atom 什么时候重算依赖不变会重算吗
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-232：Jotai 派生 atom 什么时候重算，依赖不变会重算吗

**答**：
- 派生 atom 有记忆化：依赖的值全部不变时读取直接命中缓存不重算；任一依赖变化才惰性重算（pull 模型）
- 重算后用 Object.is 比较结果，相同则不向下游传播——派生函数返回稳定引用（如统一空数组常量）能斩断多余渲染
- 与 useMemo 的区别：记忆化挂在 atom 实例上而非组件实例，跨组件共享缓存；组件卸载不影响
- 反模式：派生函数里返回 `filter().map()` 新数组——依赖没变不会重算，但依赖一变所有消费组件都会收到新引用，配合 shallow 比较或拆小原子优化

```javascript
const nums = atom([3, 1, 2])
const sorted = atom((g) => [...g(nums)].sort((a, b) => a - b))  // 依赖 nums
// nums 不变时读取 sorted：直接缓存命中，sort 不重复执行
const sum = atom((g) => g(sorted).reduce((a, b) => a + b, 0))   // 链式依赖按图传播
```
