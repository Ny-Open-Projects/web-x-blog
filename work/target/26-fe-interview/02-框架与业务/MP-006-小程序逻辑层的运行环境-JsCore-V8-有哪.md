---
title: [MP-006] 小程序逻辑层的运行环境（JsCore/V8）有哪些限制？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-006：小程序逻辑层的运行环境（JsCore/V8）有哪些限制？
**答**：
- iOS 用 JavaScriptCore，Android 用 V8，开发者工具用 NW.js（chromium）——三端能力有差异，ES 新特性覆盖不同，需按基础库版本兼容。
- 没有 window/document/navigator，没有 Cookie，因此鉴权只能靠 header + storage 自行管理。
- 全局可用的只有 `wx/getApp/App/Page/Component/getCurrentPages/getCurrentInstance` 等框架注入对象。
- 网络请求必须走已配置的**合法域名**白名单（HTTPS），本地调试需勾选"不校验合法域名"。

```javascript
// 运行环境探测：多端兼容时判断平台与基础库
const { platform, SDKVersion, benchmarkLevel } = wx.getDeviceInfo()
const env = {
  platform,            // ios / android / devtools / mac / windows
  SDKVersion,          // 基础库版本，决定可用的 wx API
  benchmarkLevel,      // 机型性能等级，-1 表示未知，可用于低端机降级
  isDevtools: platform === 'devtools'
}
```
