---
title: [V3-021] 组合式 API 解决了 mixin 的哪些问题？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-021：组合式 API 解决了 mixin 的哪些问题？
**答**：
- mixin 属性来源不明：组件里看到的方法不知道来自哪个 mixin，重构风险高。
- 命名冲突：多个 mixin 与组件的同名 data/methods 静默覆盖。
- 隐式耦合：mixin 依赖组件的属性，组件不知道自己必须提供什么。
- composable 显式 import、显式传参、显式返回，且天然支持 TS 类型推导。

```typescript
// mixin 的问题：来源不明、命名冲突、隐式耦合
const petsMixin = {
  data() {
    return { pets: ["cat", "dog"] };
  },
  methods: {
    feedPets() {}, // 组件里看不到定义却能用，重构极易出错
  },
};

// Vue3 用 composable 替代：显式导入、来源清晰、类型友好
import { ref } from "vue";

export function usePets() {
  const pets = ref<string[]>([]);
  const feedPets = () => pets.value.forEach((p) => console.log(p));
  return { pets, feedPets }; // 来源和依赖一目了然
}
```
