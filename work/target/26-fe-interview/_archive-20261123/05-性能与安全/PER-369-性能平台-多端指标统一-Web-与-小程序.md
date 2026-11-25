---
title: [PER-369] Web 与小程序/客户端的多端性能指标如何统一？口径映射与看板合并？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-369：Web 与小程序/客户端的多端性能指标如何统一？口径映射与看板合并？

**答**：
- 口径差异现实：小程序没有标准 CWV API（wx.getPerformance 提供有限指标），客户端原生有自己的启动指标（冷启动/温启动）。统一方案是"**语义对齐而不是 API 对齐**"：定义平台无关的语义指标——首屏内容就绪（Web=LCP、小程序=首页 setData 完成渲染、客户端=首帧+首屏数据）、交互就绪、页面切换时长，各端用自己最接近的 API 实现。
- 采集适配层：每端一个 adapter（Web adapter 用 PerformanceObserver，小程序 adapter 用 wx.getPerformance + 自打点），输出统一 schema（指标名/值/页面模板/端标识），聚合层不感知平台差异。
- 看板原则：分端看板为主（口径差异客观存在，混在一起误导），跨端对比视图只对"语义对齐"指标开放，并标注每端的实现方式与已知偏差。
- SLO 分端设定：小程序初始化管线不同，阈值可以不同（如小程序首屏 SLO 3s，Web 2.5s），但验收流程统一。

```text
多端指标语义映射表：
语义指标          Web 实现                    小程序实现                     客户端实现
首屏内容就绪      LCP (last candidate)        首页 onReady + 首屏 setData    首帧渲染 + 首屏接口完成
交互就绪          首次 click 无排队            首屏可点击事件绑定完成          启动完成回调
页面切换          SPA-NT 自定义                路由切换 onPageShow           Activity 冷启动分段
统一 schema: { metric, value, platform, pageTemplate, device, version }
看板：分端主视图 + "语义对齐指标"跨端对比（标注口径来源）
```
