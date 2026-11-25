---
title: [WEB-594] iOS WebKit 与 Chromium 多进程模型的差异及前端影响
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 浏览器架构]
type: 面试题
---

## WEB-594：iOS WebKit 与 Chromium 多进程模型的差异及前端影响

**答**：
- Chromium 全平台多进程：浏览器/渲染/GPU/网络进程完整分工，Android 上也基本完整（站点隔离默认开）
- iOS 强制所有 WebView 走 WKWebView（WebKit）：进程模型由系统统一管理，内存限额更紧（jetsam 直接杀进程）、GPU 能力受限、无自研网络栈（系统代理/缓存策略不同）
- 前端影响一：iOS 上页面可用内存远小于桌面（数百 MB 级），大图/长列表更易触发白屏刷新——iOS 内存预算是性能优化的第一约束
- 前端影响二：WKWebView 无完整站点隔离语义差异、HTTP/3 支持跟随系统版本而非 Chrome 版本，灰度策略要按 OS 版本分桶
- 混合 App 提醒：iOS App 多个 WKWebView 实例可能共享 WebContent 进程也可能独立，跨实例通信不要依赖共享 JS 全局

```text
差异速查:
  内存限额: iOS 数百MB(jetsam) vs 桌面 GB 级
  进程模型: 系统统管 vs Chromium 自管
  h3: iOS 跟随系统 vs Chrome 跟随版本
  结论: iOS 单页内存预算 <500MB 是硬设计约束
```
