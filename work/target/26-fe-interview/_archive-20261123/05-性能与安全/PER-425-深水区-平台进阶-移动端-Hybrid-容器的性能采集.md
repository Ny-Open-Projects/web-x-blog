---
title: [PER-425] Hybrid/WebView 容器的性能采集：native 容器如何把启动与页面指标喂给统一 RUM？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-425：Hybrid/WebView 容器的性能采集：native 指标如何接入统一 RUM？

**答**:
- Hybrid 特有指标：容器冷启动（点击图标 → WebView 就绪）、容器复用率、JS Bridge 调用耗时、native↔H5 通信开销、离线包加载时长——这些 CWV 完全不覆盖，但恰恰是 Hybrid 用户感知的大头。
- 采集路径：native 侧（容器启动计时/Bridge 耗时统计）通过 JS Bridge 注入到 H5 的 RUM SDK（统一 schema，platform: 'webview-ios'）；WebView 内的标准指标（Web 端那套）正常采集；两侧数据在聚合层合并出"端到端启动"指标（native 启动 + 容器就绪 + H5 首屏）。
- 口径注意：WebView 的 Performance API 在 iOS/Android 内核有差异（Android 系统 WebView 版本碎片化），采集前特性检测；Bridge 耗时要在 native 侧计时（JS 侧只能看到回调时间）。
- 价值场景："App 内打开 H5 慢"的归因拆解——native 启动占比 vs 容器复用 vs H5 渲染占比，决定优化投入方向（复用容器池通常收益最大）。

```text
Hybrid 统一采集架构：
native 侧计时：冷启动 / WebView 就绪 / Bridge 调用耗时（native 侧权威计时）
  → JS Bridge 注入 RUM SDK（统一 schema，platform=webview-*)
H5 侧标准采集：LCP/INP/CLS/资源（特性检测兜底）
聚合层合并：端到端启动 = native 启动 + 容器就绪 + H5 LCP（分段瀑布）
归因示例："App 内 H5 慢"拆解 → native 启动 800ms + 容器未复用 600ms + H5 渲染 1.2s
  → 结论：容器池复用率 40% → 90% 收益最大（native 优化次之）
注意：Android WebView 内核碎片化 → 特性检测；Bridge 耗时以 native 计时为准
```
