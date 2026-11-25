---
title: [PER-999] 浏览器隐私新格局：第三方 Cookie 淘汰后前端要做什么
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-999：浏览器隐私新格局：第三方 Cookie 淘汰后前端要做什么

**答**：
- 趋势：Safari/Firefox 已默认拦截三方 Cookie，Chrome 转向用户选择模式；依赖三方 Cookie 的广告归因/登录态失效。
- 替代：First-Party Sets/相关站点集（RWS）、Partitioned cookies（CHIPS，按顶级站点分区）、Storage Access API（受控申请三方存储）。
- 前端动作：盘点三方 Cookie 依赖清单 → 登录态迁到同站 Cookie/OAuth → 归因迁到 Privacy Sandbox API。
- 兼容：检测 document.requestStorageAccess 可用性，失败给降级体验（如引导跳转登录）。

```javascript
// Storage Access API：受控的三方访问
async function ensureThirdPartyAccess() {
  if (!document.hasStorageAccess) return true;   // 未启用分区，无需申请
  if (await document.hasStorageAccess()) return true;
  try {
    await document.requestStorageAccess();       // 浏览器按用户与站点交互授权
    return true;
  } catch { return false; }                      // 拒绝 -> 走降级流程
}
// 降级：无权限时把依赖数据通过 postMessage 从第一方页转发
```
