---
title: [FRP-133] mixin 到 composable 的演进，本质解决了什么问题？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-133：mixin 到 composable 的演进，本质解决了什么问题？

**答**：
- mixin 的问题是**隐式合并**：`mixins: [a, b]` 后模板里的 `this.foo`、`this.loading` 找不到定义处（来源不明）、多 mixin 同名冲突静默覆盖、mixin 之间靠 this 隐式耦合。
- composable 用"普通函数 + 显式返回值"替代合并：`const { loading, load } = useFetch()` —— 来源显式、可重命名、可传参、可自由组合多次。
- 能成立的技术前提是**响应式系统脱离组件存在**：函数里创建的 ref/computed 生命周期由 effectScope 管理，不需要依附组件实例（Vue2 的 data/mixin 必须挂在 this 上）。
- 本质一句话：从"框架帮你合并属性"变成"你自己组合函数"——把继承式复用换成函数式复用。

```javascript
// 简化实现，帮助理解两种复用方式的差异
// —— Vue2 时代：mixin 隐式合并 ——
const fetchMixin = {
  data() { return { loading: false, data: null }; },           // 来源不明 #1
  methods: {
    async fetch(url) {                                          // 如果两个 mixin 都有 fetch？静默覆盖
      this.loading = true;
      this.data = await api(url);
      this.loading = false;
    }
  },
  mounted() { this.fetch(this.url); }                           // 多个 mixin 的 mounted 合并调用，顺序难追
};
// 组件模板里用 this.loading —— IDE 无法跳转，冲突无提示

// —— Vue3：composable 显式组合 ——
function useFetch(url) {
  const loading = ref(false);
  const data = ref(null);
  const error = ref(null);
  async function load() {
    loading.value = true;
    try { data.value = await api(url.value); }
    catch (e) { error.value = e; }
    finally { loading.value = false; }
  }
  watch(url, load, { immediate: true });   // 自动注册进组件 scope（FRP-125）
  return { loading, data, error, load };   // 显式返回：来源一目了然
}

// 组件里：可重命名、可并行多个实例
const { data: user,  loading: userLoading  } = useFetch(userUrl);
const { data: posts, loading: postsLoading } = useFetch(postsUrl);
// 同一个 useFetch 用两次 = 两份独立状态 —— mixin 根本做不到（data 会被合并共享语义）
```
