---
title: [MP-088] 小程序与 H5/APP 如何互跳？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-088：小程序与 H5/APP 如何互跳？
**答**：
- H5 → 小程序：微信内用 **URL Scheme/URL Link** 或 wx-open-launch-weapp 开放标签；外部浏览器用 URL Link（短信/邮件场景）。
- 小程序 → H5：web-view；小程序 → APP：`wx.openEmbeddedMiniProgram`? 不对——拉起 APP 用 **launchApp**（button open-type="launchApp" 或 App 唤起协议），需 APP 关联同一主体。
- APP → 小程序：开放 SDK（微信 OpenSDK）拉起指定小程序页面并带参。

```xml
<!-- 小程序内跳回 APP：open-type=launchApp，需 APP 与小程序同主体关联 -->
<button open-type="launchApp" app-parameter="from=miniprogram" binderror="onLaunchErr">
  打开 APP
</button>

<!-- H5 内跳小程序：微信开放标签（需开放平台配置） -->
<!-- <wx-open-launch-weapp appid="wx123..." path="pages/index/index?id=1"> -->
```
