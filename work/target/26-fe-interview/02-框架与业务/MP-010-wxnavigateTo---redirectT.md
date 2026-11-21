---
title: [MP-010] wx.navigateTo / redirectTo / reLaunch / switchTab / navigateBack 的差异与选型？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-010：wx.navigateTo / redirectTo / reLaunch / switchTab / navigateBack 的差异与选型？
**答**：
- `navigateTo`：保留当前页入栈，可返回；适合列表→详情的常规前进。
- `redirectTo`：关闭当前页再打开新页，不入栈；适合"提交成功"后替换表单页，防返回重复提交。
- `switchTab`：只能跳 tabBar 页面，且会**关闭所有非 tab 页面**。
- `reLaunch`：关闭全部页面打开任意页（含 tab 页）；适合登录态切换、清栈重开。
- `navigateBack`：退栈，配合 EventChannel 可向上一页回传数据。

```javascript
wx.navigateTo({ url: '/pages/detail/detail?id=1' })  // 入栈，可返回
wx.redirectTo({ url: '/pages/success/success' })     // 替换当前页
wx.switchTab({ url: '/pages/index/index' })          // 仅 tab 页，清空非 tab 页
wx.reLaunch({ url: '/pages/index/index' })           // 清空整个页面栈
wx.navigateBack({ delta: 2 })                        // 后退两层
```
