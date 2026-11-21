---
title: [V3-306] 响应式数组的 sort / reverse 等原地方法如何触发更新？有什么陷阱？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-306：响应式数组的 sort / reverse 等原地方法如何触发更新？有什么陷阱？
**答**：
- Proxy 层面对 `sort/reverse/splice/pop/push` 等方法做了拦截包装：先 `pauseTracking` 关闭收集再调原始方法，避免 length 与索引依赖被误收，结束后统一 trigger。
- 原地方法只触发一次批量派发（内部用 noTracking 包裹），而不是每个索引写入都触发——这是 Vue3 对 Vue2 数组方法 hack 的替代。
- 陷阱一：`sort` 比较函数里读取其他响应式数据不会建立依赖（收集被暂停），后续该数据变化不会引发重排。
- 陷阱二：频繁 sort 大数组仍然会全量触发列表 diff；性能敏感的排序列表应配合 computed 缓存排序结果。
- 拷贝方法（`toSorted/toReversed`）返回普通数组副本，直接赋值回去也可以，代价是全量替换引用。
```javascript
const sorted = computed(() => [...list.value].sort((a, b) => a.price - b.price))
// 模板渲染 sorted 而不是直接 sort 原数组：排序逻辑可缓存，且不污染原始顺序
```
