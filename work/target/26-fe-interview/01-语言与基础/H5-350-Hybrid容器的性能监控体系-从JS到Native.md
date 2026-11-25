---
title: [H5-350] Hybrid 容器的性能监控体系：从 JS 到 Native 全链路
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 可观测]
type: 面试题
---

## H5-350：Hybrid 容器的性能监控体系：从 JS 到 Native 全链路

**答**：
- 双端链路打点：App 侧（点击→容器创建→WebView 首帧）+ H5 侧（HTML 开始→FCP→接口完成→可交互），桥上传统一时间轴拼出完整瀑布
- H5 侧采集：web-vitals 库取 LCP/INP/CLS + 自定义业务指标（首屏接口 P75）；Native 侧采集容器冷启动、离线包命中率、桥调用耗时分布
- 错误监控闭环：window.onerror/unhandledrejection + 资源加载失败 + 接口失败，带 webview 版本/容器版本归因；Native crash 与 H5 JS 错误分域统计
- 桥质量监控：bridge call 的 P95 耗时、超时率、Native 崩溃率——桥是两端耦合点，最容易烂
- 数据消费：按版本/机型/渠道看核心页面秒开率排行，出「劣化 top 页面清单」驱动优化迭代

```javascript
// Hybrid 全链路上报
bridge.call('perf', { event: 'container-timeline', data: nativeTimeline }); // Native 侧时序
const metrics = { fcp, lcp, inp, cls };
beacon({ page: location.pathname, ...metrics,
  wv: navigator.userAgent.match(/Chrome\/(\d+)/)?.[1],
  offline: window.__OFFLINE_HIT__ });        // 离线包命中标记由拦截层注入
```
