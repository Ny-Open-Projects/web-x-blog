---
title: [V3-353] v-model 与 Pinia store 的联动模式有哪些？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-353：v-model 与 Pinia store 的联动模式有哪些？
**答**：
- 直接绑定 store state：`v-model="store.name"` 在 Pinia 中合法（state 是响应式 store），小型场景最简单，但会让组件强耦合 store。
- 双向代理：组件用 defineModel，父组件层 `v-model="store.name"` 桥接——组件可复用，写库动作集中在父层。
- action 收口：表单场景用 `v-model` + watch 防抖后 dispatch action，或在 composable 里返回可写 computed（get 读 state，set 调 action），保证 mutation 有日志/校验。
- 跨页持久化：写 store 的同时由插件同步 localStorage，组件无需关心。
- 注意 storeToRefs 解构后再绑定，避免直接解构丢响应。
```javascript
const name = computed({
  get: () => store.profile.name,
  set: (v) => store.updateName(v) // action 收口
})
```
