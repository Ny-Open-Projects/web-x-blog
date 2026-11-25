---
title: [MP-060] 长列表性能方案：recycle-view 与自研虚拟列表？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-060：长列表性能方案：recycle-view 与自研虚拟列表？
**答**：
- 问题：几百上千节点的列表 setData 慢、内存高、滚动掉帧。
- 方案一：官方组件库 **recycle-view**（回收复用 + 固定/可估高度），接入成本低。
- 方案二：自研虚拟列表——只渲染可视区 ± buffer 的切片，上方用占位高度撑起滚动，scrollTop 映射 startIndex；不定高需缓存实测高度。
- 配合：分页加载 + 图片懒加载 + 局部路径更新，避免整列表 setData。

```javascript
// 自研虚拟列表核心：切片 + 位移占位
Page({
  data: { slice: [], offset: 0 },
  itemH: 120, buffer: 5, viewportH: 600,
  onScroll(e) {
    const { scrollTop } = e.detail
    const start = Math.max(0, Math.floor(scrollTop / this.itemH) - this.buffer)
    const count = Math.ceil(this.viewportH / this.itemH) + this.buffer * 2
    this.setData({
      slice: this.allData.slice(start, start + count),
      offset: start * this.itemH    // 占位：translateY(offset) 撑起上方空白
    })
  }
})
```
