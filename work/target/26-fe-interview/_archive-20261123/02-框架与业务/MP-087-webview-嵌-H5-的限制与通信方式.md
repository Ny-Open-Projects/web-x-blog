---
title: [MP-087] web-view 嵌 H5 的限制与通信方式？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-087：web-view 嵌 H5 的限制与通信方式？
**答**：
- web-view 自动铺满整页，内部 H5 必须是**业务域名**（后台配置校验文件）且 HTTPS；个人主体不可用。
- 通信：H5 → 小程序用 `wx.miniProgram.postMessage`（**消息在特定时机**——后退/销毁/分享才由 bindmessage 收到）与 navigateBack/navigateTo；小程序 → H5 靠 url 参数。
- 登录态同步：小程序 storage 无法直达 H5，需经 URL ticket 或 cookie 域打通。

```javascript
// H5 侧（jweixin）
wx.miniProgram.postMessage({ data: { action: 'buy', id: 1 } })
wx.miniProgram.navigateTo({ url: '/pages/pay/pay?id=1' })

// 小程序侧：特定时机才能收到 postMessage
// <web-view src="{{url}}" bindmessage="onMessage" />
Page({
  onMessage(e) {
    console.log(e.detail.data)   // 后退/组件销毁/分享时触发
  }
})
```
