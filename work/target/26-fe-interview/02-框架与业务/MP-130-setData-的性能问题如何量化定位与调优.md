---
title: [MP-130] setData 的性能问题如何量化定位与调优？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-130：setData 的性能问题如何量化定位与调优？
**答**：
- 量化指标：单次 setData 数据量（>256KB 直接失败）、调用频率、相邻两次间隔、渲染层 CPU 占用；开发者工具 Audits 面板与 `wx.getPerformance` 的 render 项。
- 定位：工具「性能面板」录制，看 setData 的 payload 大小与触发堆栈；给 setData 封装打点（时间+路径+size）。
- 调优三板斧：**路径更新**（`a[0].b` 代替整个 a）、**合并批量**（微任务内合并多次 setData）、**移出渲染外**（纯逻辑数据放 this 上不进 data）。
- 高频数据（滚动进度/倒计时秒）用节流或 CSS 动画替代，长列表用分片渲染。

```javascript
// setData 封装：自动批量合并 + 打点
function batchSetData(page) {
  const pending = {}
  let scheduled = false
  return (patch) => {
    Object.assign(pending, patch)
    if (scheduled) return
    scheduled = true
    Promise.resolve().then(() => {
      scheduled = false
      const size = JSON.stringify(pending).length
      if (size > 100 * 1024) report('setdata-huge', { page: page.route, size })
      page.setData(pending)
      for (const k in pending) delete pending[k]
    })
  }
}
Page({
  onLoad() { this.setD = batchSetData(this) },
  onScroll() { this.setD({ 'list[3].active': true }) }  // 路径更新，只传 diff
})
```
