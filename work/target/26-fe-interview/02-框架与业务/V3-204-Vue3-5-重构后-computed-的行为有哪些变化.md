---
title: [V3-204] Vue 3.5 重构后 computed 的行为有哪些变化与可感知改善？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-204：Vue 3.5 重构后 computed 的行为有哪些变化与可感知改善？
**答**：
- 不再依赖 `dirty` 布尔：改用版本号 + 依赖版本比对，脏检查更精准，避免"标脏了但重算发现没变"的浪费。
- 计算属性稳定性：3.4 中 computed 在多次访问间可能重复执行 getter 的边界场景（如 batch 中断）被修复。
- 与 v-model 配合：3.4 引入的 `defineModel` 在 3.5 后底层 computed 实现更稳，双向绑定在父组件未传值时的警告更准确。
- 内存：computed 也复用双向链表结构，长 computed 链（computed of computed）内存占用显著下降。
- 行为可感知点：`computed` 依赖数组元素（`arr[i]`）的追踪在 3.5 中更精细（数组索引级），`arr.splice` 后不再全量失效。

```javascript
// 3.5 之前 vs 之后：重复求值场景
const count = ref(0);
const double = computed(() => count.value * 2);
// 3.4：trigger(count) -> 标脏 double -> 渲染访问 double 重算（即使 getter 结果没变也要跑一遍比较）
// 3.5：trigger(count) -> count.version++ -> 渲染访问 double ->
//      version 比对发现 double 依赖的 count 版本未变（本轮 count 没被改）-> 直接返回缓存
const arr = ref([1, 2, 3]);
const sum = computed(() => arr.value.reduce((a, b) => a + b));
arr.value[0] = 100; // 3.5：只触发索引 0 的 dep，sum 重算一次；3.4 数组级依赖粒度更粗
```
