---
title: [MP-016] setData 性能优化的完整手段有哪些？（高频压轴）
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-016：setData 性能优化的完整手段有哪些？（高频压轴）
**答**：
- **降频率**：事件（scroll/input/move）高频触发时节流；同一 tick 内多次 setData 用 `wx.nextTick` 批处理合并成一次。
- **降数据量**：只传变化的字段，用路径更新 `'list[2].status'`；不参与渲染的数据放 this 上而非 data。
- **避坑**：不要向后台页面 setData；不要一次性传长列表全量、大 JSON；避免 data 里放大对象/大数组常量。
- 验证手段：开发者工具 Audits/Performance 面板看 setData 调用次数与耗时。

```javascript
// 差：高频全量更新
onPageScroll(e) {
  this.setData({ scrollTop: e.scrollTop, backTopShow: e.scrollTop > 300 })
}
// 好：节流 + 路径更新 + 合并（注意 apply 透传 this，否则 this.setData 取不到页面实例）
const throttle = (fn, ms) => {
  let last = 0
  return function (...args) {
    const now = Date.now()
    if (now - last >= ms) { last = now; fn.apply(this, args) }
  }
}
Page({
  onPageScroll: throttle(function (e) {
    this.setData({ 'page.scrollTop': e.scrollTop })
  }, 200)
})
```
