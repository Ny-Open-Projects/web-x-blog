---
title: [MP-112] uni-app/Taro 项目中如何处理平台差异？条件编译实战？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-112：uni-app/Taro 项目中如何处理平台差异？条件编译实战？
**答**：
- uni-app 用注释条件编译：`#ifdef MP-WEIXIN / #ifdef MP-ALIPAY / #ifndef`，js/模板/样式/json 均支持；Taro 用 `process.env.TARO_ENV` 分支 + 文件后缀（`.weixin.jsx` 覆盖）。
- 原则：**90% 逻辑共用**，差异集中在 adapter 层与页面级小分支；超过一屏的平台分支应抽成独立平台文件。
- 组件差异：条件编译选组件（如抖音的 `video` 播放器行为不同），样式差异用 `/* #ifdef */` 处理安全区/rpx 边界。
- 每个目标平台都要有独立构建产物与冒烟脚本，防止"只测微信"。

```javascript
// uni-app 条件编译示例
// #ifdef MP-WEIXIN
wx.requestSubscribeMessage({ tmplIds: ['tmpl-1'] })
// #endif
// #ifdef MP-ALIPAY
my.requestSubscribeMessage({ pageId: 'alipay-sub-page-id' }) // 支付宝订阅消息走 pageId
// #endif
// #ifdef MP-TOUTIAO
tt.requestSubscribeMessage({ tmplIds: ['tt-tmpl-1'] })
// #endif

// Taro 写法
if (process.env.TARO_ENV === 'weapp') { /* 微信专属逻辑 */ }
```
