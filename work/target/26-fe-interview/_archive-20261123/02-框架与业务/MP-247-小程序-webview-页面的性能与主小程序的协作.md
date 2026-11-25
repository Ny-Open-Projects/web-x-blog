---
title: [MP-247] 小程序内嵌 web-view 页面的性能与协作要点？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-247：web-view 页面协作要点？
**答**：
- 通信：web-view 内 H5 用 wx.miniProgram.postMessage/navigateTo（有限单向通信），消息在「小程序特定时机」才收到（后退/组件销毁）——设计上用 URL 参数与跳转传数据为主。
- 登录态：H5 域名白名单 + URL 带 token（短时效一次性）或 cookie 共享（业务域）——注意 URL 泄漏风险（分享）。
- 性能：web-view 是独立 WebView（内存重）——多级 web-view 页面内存压力大；加载白屏用 H5 侧骨架 + 域名 DNS 预热。
- 兼容：个人小程序不支持 web-view；分享/h5 内支付跳转限制多。
- 选型：优先原生实现，web-view 只用于快速复用既有 H5（过渡方案）。
