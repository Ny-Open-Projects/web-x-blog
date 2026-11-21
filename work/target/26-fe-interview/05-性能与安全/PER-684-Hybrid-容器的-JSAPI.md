---
title: [PER-684] Hybrid 容器的 JSAPI 调用性能：bridge 往返开销在哪、批量调用与高频 API 的优化怎么做？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-684：Hybrid 容器的 JSAPI 调用性能：bridge 往返开销在哪、批量调用与高频 API 的优化怎么做？

**答**：
- bridge 往返开销链：JS 序列化 -> WebView 拦截（URL scheme/JS 注入）-> Native 执行 -> 结果序列化回注 JS——每次 5~50ms，高频调用（滚动位置、实时数据）会拖垮页面。
- 优化三板斧：**批量**（一帧内多次调用合并成一次，参数数组化）、**推送代替拉取**（Native 主动事件推送，H5 不轮询）、**高频 API 常驻通道**（如定位/滚动位置用专用长连接通道，避免每次握手）。
- 数据面优化：大 JSON 走二进制（ArrayBuffer/MessageChannel 类通道）、只传增量；序列化成本高的（大列表）让 Native 渲染列表、H5 只传配置。
- 度量：bridge 调用耗时分布（p95）、每秒调用次数、单页 bridge 总耗时占比（> 15% 就该治理）。

```javascript

const bridgePerf = {
  costChain: 'JS 序列化 -> WebView 拦截 -> Native 执行 -> 回注 JS（每次 5~50ms）',
  strategies: {
    batch: 'rAF 周期内合并调用，参数数组化一次往返',
    push: 'Native 事件推送替代 H5 轮询（scroll/location 变化）',
    channel: '高频 API（定位/滚动）用常驻专用通道',
    binary: '大数据走 ArrayBuffer，传增量不传全量',
  },
  budget: { p95PerCall: '50ms', totalShare: '单页 bridge 总耗时占比 < 15%' },
};
// 批量封装示例见 685；度量先于优化：先统计 bridge 调用耗时分布再动手
```
