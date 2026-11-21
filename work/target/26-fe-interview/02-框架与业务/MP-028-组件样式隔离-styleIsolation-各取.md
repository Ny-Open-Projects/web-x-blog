---
title: [MP-028] 组件样式隔离 styleIsolation 各取值有什么区别？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-028：组件样式隔离 styleIsolation 各取值有什么区别？
**答**：
- `isolated`（默认）：组件内外样式完全隔离，页面样式不影响组件，组件样式也不外泄。
- `apply-shared`：页面（含 app.wxss）样式可影响组件，组件样式不外泄；旧写法 `addGlobalClass: true` 等价。
- `shared`：双向共享——页面样式影响组件，组件样式也影响页面及所有开启 shared 的组件，慎用（易互相污染）。
- 页面级也可配置 `options.styleIsolation`；全局样式想进 isolated 组件只能走 CSS 变量或 externalClasses。

```javascript
// 组件级
Component({
  options: { styleIsolation: 'apply-shared' } // 接收页面样式，不外泄
})

// 页面级
Page({
  options: { styleIsolation: 'shared' }
})
```
