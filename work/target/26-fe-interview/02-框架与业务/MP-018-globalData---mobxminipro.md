---
title: [MP-018] globalData / mobx-miniprogram / 自研 store 三种全局状态方案怎么选？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-018：globalData / mobx-miniprogram / 自研 store 三种全局状态方案怎么选？
**答**：
- `app.globalData`：零依赖、最简单，但**无响应式**，页面需在 onShow 手动拉取，适合状态极少的小项目。
- `mobx-miniprogram` + `mobx-miniprogram-bindings`：官方推荐，响应式、computed、action，bindings 自动建立组件与 store 的双向绑定并自动销毁。
- 自研 store：observer 模式 + 在 Page/Component 包装器里统一订阅与 unsubscribe，可控可埋点，但维护成本高。
- 中大型项目建议 mobx 或自研响应式 store，globalData 只放 appId、token 等基础字段。

```javascript
// store/index.js（mobx-miniprogram）
import { observable, action } from 'mobx-miniprogram'
export const store = observable({
  cartCount: 0,
  setUser: action(function (n) { this.cartCount = n })
})

// 组件内自动绑定与响应
import { storeBindingsBehavior } from 'mobx-miniprogram-bindings'
import { store } from '../../store/index'
Component({
  behaviors: [storeBindingsBehavior],
  storeBindings: {
    store,
    fields: ['cartCount'],       // data 变化自动刷新视图
    actions: ['setUser']
  }
})
```
