---
title: [MP-050] 分享 onShareAppMessage / onShareTimeline 的实现与差异？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-050：分享 onShareAppMessage / onShareTimeline 的实现与差异？
**答**：
- 好友会话：页面定义 `onShareAppMessage` 返回 `{ title, path, imageUrl }`；path 决定落地页与参数，最长约 5 个标题字/10 字符截断规则注意。
- 朋友圈：`onShareTimeline` 返回 `{ title, query, imageUrl }`——**没有 path**，进入的是单页模式，能力受限（部分组件/API 不可用），靠 query 传参。
- 触发方式：右上角菜单转发、`<button open-type="share">`；朋友圈入口需 `wx.showShareMenu({ menus: ['shareAppMessage', 'shareTimeline'] })` 显式开启。

```javascript
Page({
  onShareAppMessage() {
    return {
      title: '好友邀请标题',
      path: `/pages/detail/detail?id=${this.data.id}&from=share`,
      imageUrl: 'https://cdn.example.com/share-cover.png'
    }
  },
  onShareTimeline() {
    return { title: '朋友圈标题', query: `id=${this.data.id}`, imageUrl: 'https://cdn.example.com/sq.png' }
  }
})
```
