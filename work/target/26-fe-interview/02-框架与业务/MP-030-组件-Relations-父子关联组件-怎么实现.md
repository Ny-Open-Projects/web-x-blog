---
title: [MP-030] 组件 Relations（父子关联组件）怎么实现？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-030：组件 Relations（父子关联组件）怎么实现？
**答**：
- 在关联双方 `relations` 中声明对方路径与关系类型：`parent/child`（一对一严格层级）或 `ancestor/descendant`（跨层级）。
- 生命周期钩子 `linked/unlinked/linkChanged` 感知对方挂载/卸载；`this.getRelationNodes('./tab-panel')` 获取关联实例集合。
- 典型场景：tabs 与 tab-panel、accordion 与 item、表单与表单项联动。
- 也可由子组件主动 `this.getRelationNodes` 反查父级；单边声明 descendant/ancestor 即可不强制双方都写。

```javascript
// components/tabs/index.js
Component({
  relations: {
    './tab-panel/index': {
      type: 'child',
      linked(panel) { this._panels.push(panel) },        // 子组件挂载
      unlinked(panel) {
        this._panels = this._panels.filter(p => p !== panel)
      }
    }
  },
  lifetimes: {
    attached() { this._panels = [] }
  }
})

// components/tab-panel/index.js
Component({
  relations: { '../tabs/index': { type: 'parent' } }     // 反向声明
})
```

---

## 五、分包与加载（031-037）
