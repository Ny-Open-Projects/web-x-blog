---
title: [MP-011] 页面间通信 EventChannel 怎么用？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-011：页面间通信 EventChannel 怎么用？
**答**：
- `wx.navigateTo` 的 `events` 参数声明监听器，`success` 回调里拿到**发往目标页**的 EventChannel；目标页用 `this.getOpenerEventChannel()` 拿到反向通道。
- 双向 `emit/on`，适合选择器页面回传结果、列表页实时刷新等场景；页面关闭后通道失效。
- 相比 url 传参：可传对象不必序列化；相比全局变量：生命周期与页面绑定，无泄漏风险。

```javascript
// A 页面：跳转并监听 selected 事件
wx.navigateTo({
  url: '/pages/select/select',
  events: {
    selected: (data) => this.setData({ picked: data })   // 接收 B 回传
  }
})

// B 页面：向打开它的页面发数据
Page({
  onPick() {
    const channel = this.getOpenerEventChannel()
    channel.emit('selected', { id: 1, name: '北京' })    // 回传 A 页面
  }
})
```
