---
title: [PER-711] 移动端 Web 容器的 JS 异常与 Native 崩溃如何关联定位？跨端日志对齐方案
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-711：移动端 Web 容器的 JS 异常与 Native 崩溃如何关联定位？跨端日志对齐方案

**答**：
- 问题：H5 白屏可能由 Native 崩溃/容器重启引起，Native 崩溃也可能由 H5 注入触发——两端日志独立时无法互证。
- 对齐方案：**会话级 traceId**（容器创建时生成，注入 H5 UA/启动参数，H5 全部上报携带；Native 日志同样携带）；**时间轴对齐**（统一用容器单调时钟偏移换算）；**共同维度**（页面路由、容器版本、设备档）。
- 定位模式：H5 白屏样本 -> 查同 traceId 的 Native 日志 -> 发现 WebView 渲染进程崩溃（则非前端问题）；Native 崩溃栈里带 H5 URL（注入点异常）-> 转前端排查。
- 落地：约定跨端日志协议"（traceId/时钟基准/公共维度字段），两端 SDK 各自实现采集，平台侧按 traceId 拼装完整时间线。

```javascript

const crossStackLogProtocol = {
  traceId: '容器创建时生成 -> 注入 UA/启动参数 -> H5 上报全携带 -> Native 日志同携带',
  clock: '统一单调时钟基准，两端时间戳可换算对齐',
  dims: ['route', 'containerVersion', 'deviceTier', 'pkgVersion'],
  patterns: {
    whiteScreen: 'H5 白屏 -> 同 traceId 查 Native 日志 -> 渲染进程崩溃 = 非 H5 问题',
    nativeCrash: '崩溃栈带 H5 URL -> JSBridge 注入异常 -> 转前端',
  },
  essence: '跨端日志协议三要素：traceId 串联 + 时钟对齐 + 公共维度，平台按 traceId 拼时间线',
};
console.log(crossStackLogProtocol.essence);
```
