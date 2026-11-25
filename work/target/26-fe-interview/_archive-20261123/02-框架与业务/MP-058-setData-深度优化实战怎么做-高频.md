---
title: [MP-058] setData 深度优化实战怎么做？（高频）
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-058：setData 深度优化实战怎么做？（高频）
**答**：
- 先度量：开发者工具 Performance/Audits 看 setData **次数、单次数据量、耗时占比**，找到 Top 问题页。
- 批处理：封装 `batchSetData`，同一 tick 多次 patch 合并为一次（wx.nextTick 落笔）。
- 路径化：长列表局部更新用 `'list[3].checked'`；数组整体替换改 splice 思维；纯逻辑数据挂 this 而非 data。
- 隐藏页不 setData：后台页面把 patch 存起来，onShow 时合并刷入。

```javascript
// 实战：批量合并 setData
let pending = {}
let scheduled = false
function batchSetData(page, patch) {
  Object.assign(pending, patch)
  if (scheduled) return
  scheduled = true
  wx.nextTick(() => {
    page.setData(pending)   // 一个 tick 只有一次真实 setData
    pending = {}
    scheduled = false
  })
}
// 页面里：滚动、输入、轮询统一走 batchSetData(this, {...})
```
