---
title: [V3-236] defineModel 与手写 prop+emit 有哪些语义差异？哪些场景仍该手写？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-236：defineModel 与手写 prop+emit 有哪些语义差异？哪些场景仍该手写？
**答**：
- 语义差异 1：defineModel 自带本地乐观值；手写 computed 中转默认无乐观值（必须父回传才变），行为更"严格受控"。
- 语义差异 2：defineModel 声明了 required/default 后父组件未传会有警告，且子组件写入仍会 emit——即"无父也能写"的宽松模式。
- 仍该手写的场景 1：一个字段变化要联动多个副作用（校验、埋点）——直接 watch props.modelValue 更清晰。
- 仍该手写的场景 2：双向绑定只是表象、实际是复杂状态机（分步表单）——显式 emit + 状态管理更可测。
- 结论：简单值绑定用 defineModel 提效，复杂联动用显式 prop+emit 保语义，团队规范里写清楚选择标准。

```javascript
// 手写严格受控（无乐观值）
const inner = computed({
  get: () => props.modelValue,
  set: (v) => emit('update:modelValue', v),
}); // 父不同步 → 输入框永远不动，可发现数据流 bug
// defineModel 宽松模式（自带乐观值）
const model = defineModel(); // 父不同步也先变，适合"父只是转发存储"的组件
// 多副作用场景：用 defineModel + watch 组合
const search = defineModel<string>('search');
watch(search, (v) => trackLog(v)); // 保留 defineModel 便利又挂副作用
```
