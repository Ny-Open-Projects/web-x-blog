---
title: [MP-118] web-view 加载 H5 时如何通信？postMessage 有哪些限制？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-118：web-view 加载 H5 时如何通信？postMessage 有哪些限制？
**答**：
- 小程序 → H5：只能通过 **URL 参数**传值（load 时拼参）；H5 → 小程序：先 `wx.miniProgram.postMessage`，但消息**只在特定时机**（小程序后退、组件销毁、分享）由 `bindmessage` 收到，**不能实时**。
- 实时通信限制的绕法：H5 每次交互**改 URL 跳转**（`wx.miniProgram.redirectTo/navigateTo` 自身页面带参）让小程序 onLaunch/onLoad 取参；或中间走服务端轮询。
- 微信内 H5 可用 JSSDK，需配置域名白名单（业务域名 + 校验文件）；支付等敏感操作 H5 内做不了，须跳回小程序原生页。
- 个人主体不支持 web-view；域名须 ICP 备案且 HTTPS。

```javascript
// H5 页面（引入 jweixin）
wx.miniProgram.postMessage({ data: { type: 'order', id: '1001' } }) // 暂存，特定时机才送达
wx.miniProgram.navigateUrl ? null : null
wx.miniProgram.redirectTo({ url: '/pages/h5bridge/bridge?action=pay&orderId=1001' }) // 实时传参的正规姿势

// 小程序侧
// <web-view src="{{url}}" bindmessage="onMsg" bindload="onLoad"></web-view>
Page({
  onLoad(q) { /* 取 H5 拼在 URL 上的初始参数 */ },
  onMsg(e) { /* 后退/销毁/分享时才触发，批量收到 e.detail.data 数组 */
    e.detail.data.forEach(m => m.type === 'order' && this.handle(m))
  }
})
```
