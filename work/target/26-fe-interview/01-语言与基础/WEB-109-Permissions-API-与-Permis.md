---
title: [WEB-109] Permissions API 与 Permissions-Policy 分别管什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-109：Permissions API 与 Permissions-Policy 分别管什么？
**答**：
- Permissions API 是页面侧的状态查询：`navigator.permissions.query({ name })` 返回 granted/denied/prompt，可监听 onchange，避免在已拒绝时反复弹窗。
- Permissions-Policy 是服务端的能力开关：声明本站（及嵌入的第三方）允许使用哪些浏览器能力，如 camera、geolocation、fullscreen。
- 语法：`camera=()` 全禁、`camera=(self)` 仅本站、`geolocation=(self "https://maps.example.com")` 白名单委派。
- 组合使用：先在头里收紧，再用 API 在 UI 层做体验（未授权时展示引导而不是直接调 API）。

```javascript
// 查询并监听通知权限，拒绝态不再骚扰用户
const status = await navigator.permissions.query({ name: 'notifications' });
console.log('当前状态', status.state);
status.onchange = () => console.log('用户改变了权限', status.state);
if (status.state === 'prompt') {
  // 只有真正 prompt 才走 requestPermission，引导话术放在用户主动开启时
}
```

```http
# 服务端能力开关：本站禁用摄像头，地理位置只允许自身，允许地图 iframe 使用
Permissions-Policy: camera=(), geolocation=(self "https://maps.example.com"), fullscreen=(self)
```

## 十九、实时通信进阶
