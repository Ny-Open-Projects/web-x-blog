---
title: [MP-117] 小程序如何嵌入 App？SDK 集成与互跳方案？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-117：小程序如何嵌入 App？SDK 集成与互跳方案？
**答**：
- 两条路线：**App 内嵌小程序容器**（微信开放 SDK/自家容器如 FinClip/uni 小程序 SDK）或 App 跳起微信小程序（微信开放标签/`openapi` 拉起）。
- App 内嵌：App 集成小程序 SDK，宿主注入自定义 API（如调用原生推送/相机），小程序侧用"JSBridge 约定"调用；需定义 API 白名单与版本协商。
- 互跳：App 用微信 OpenSDK 拉起小程序（带 path/参数），小程序 `wx.navigateToMiniProgram` 回跳 App（或返回宿主容器）；参数透传要签名校验。
- 场景值区分来源（场景值 1069 从 App 拉起），登录态与 App 侧打通见 MP-119。

```javascript
// 宿主容器注入的自定义 API 与互跳示例
// App 侧 SDK 注入 wx.ext = { callNative }
async function onJumpToApp(appId, extData) {
  const inHost = typeof wx.ext !== 'undefined'   // 运行在 App 容器中
  if (inHost) {
    // 容器内：直接调宿主 bridge 回 App 指定页
    wx.ext.callNative('openAppPage', { route: 'detail', payload: extData })
  } else {
    // 独立运行：跳转 App 关联的微信小程序，或引导拉起 App
    wx.navigateToMiniProgram({
      appId,
      path: `pages/detail/detail?from=miniprogram&d=${encodeURIComponent(JSON.stringify(extData))}`,
      envVersion: 'release',
      fail: () => wx.showToast({ title: '跳转失败', icon: 'none' })
    })
  }
}
```
