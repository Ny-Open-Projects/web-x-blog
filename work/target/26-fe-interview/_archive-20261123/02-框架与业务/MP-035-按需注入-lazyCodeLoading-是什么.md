---
title: [MP-035] 按需注入 lazyCodeLoading 是什么原理？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-035：按需注入 lazyCodeLoading 是什么原理？
**答**：
- 默认启动时会把**所有**自定义组件代码注入逻辑层，页面多了注入耗时与内存显著上升。
- `"lazyCodeLoading": "requiredComponents"` 后，仅注入**当前页面声明需要**的自定义组件代码，未使用的不注入。
- 收益：减少启动注入时间与内存占用；是官方启动性能优化的标配项。
- 注意：动态 `this.selectComponent` / `createSelectorQuery` 获取未注册组件的场景要验证；配合 glass-easel/Skyline 使用。

```json
{
  "lazyCodeLoading": "requiredComponents"
}
```
