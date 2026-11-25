---
title: [MP-329] 小程序的 iOS 与 Android 差异兼容
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 适配]
type: 面试题
---

## MP-329：小程序的 iOS 与 Android 差异兼容

**答**：
- 差异清单：iOS 上拉惯性（回弹导致页面抖动——scroll-view enhanced 模式/禁 bounce）、键盘顶起行为（iOS fixed 元素漂移——visualViewport 等价的 pageMeta）、字号缩放（iOS 字体缩放影响布局——text 支持自适应或锁定）、时间解析（iOS 严格 ISO 格式——'2026-01-01' 可解析，'2026/01/01' 部分版本失败）
- 系统信息 API 的版本化：getSystemInfoSync 已弃用 → 拆分（getDeviceInfo/getAppBaseInfo/getWindowInfo）——新旧 API 兼容封装
- 安卓特有的坑：video 同层渲染失效机型、长列表 recycler 视图（部分机型复用错位）、web-view 内核差异（X5/XWeb）
- 兼容策略：特性检测优先（canIUse('Skyline') / wx.canIUse）——按能力分支而不是 UA 猜机型
- 深水点：iOS「切后台 5 秒断连」与安卓「存活更久」的连接策略差异——连接管理按平台分支

```javascript
// 时间兼容
const safeDate = (s) => new Date(s.includes('/') ? s.replace(/\//g, '-') : s);
// 系统信息拆分 API 兼容
function getWindowInfo() {
  return wx.getWindowInfo?.() ?? wx.getSystemInfoSync();   // 新 API 回退
}
// 特性检测
const supportSkyline = wx.canIUse('Skyline') ?? false;
Page({ data: { supportSkyline } });
```
