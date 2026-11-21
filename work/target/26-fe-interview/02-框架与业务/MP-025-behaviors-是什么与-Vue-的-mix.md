---
title: [MP-025] behaviors 是什么？与 Vue 的 mixin 有何异同？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-025：behaviors 是什么？与 Vue 的 mixin 有何异同？
**答**：
- behaviors 是组件级逻辑复用单元，可包含 data/properties/methods/lifetimes/observers，等价于 Vue2 mixin 的定位。
- 合并规则：同名 properties/data **组件自身优先**；生命周期按声明顺序**依次执行**（mixin 也是先 mixin 后组件）。
- 差异：behaviors 是框架运行时按规则合并、支持组件间 relations 复用；mixin 是编译期对象合并；behaviors 还可被抽象节点/继承链复用。
- 共同的坑：隐式依赖来源不清晰，滥用后维护困难，需控制粒度。

```javascript
// behaviors/loading.js
module.exports = Behavior({
  data: { loading: false },
  methods: {
    showLoading() { this.setData({ loading: true }) },
    hideLoading() { this.setData({ loading: false }) }
  }
})

// 组件中使用
const loadingBehavior = require('../behaviors/loading.js')
Component({
  behaviors: [loadingBehavior],
  methods: {
    async fetch() {
      this.showLoading()
      try { await api.list() } finally { this.hideLoading() }
    }
  }
})
```
