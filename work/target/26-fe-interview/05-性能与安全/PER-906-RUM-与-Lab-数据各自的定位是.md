---
title: [PER-906] RUM 与 Lab 数据各自的定位是什么？怎么结合
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-906：RUM 与 Lab 数据各自的定位是什么？怎么结合

**答**：
- Lab（Lighthouse/CWV 实验室）：可控环境、可重复、适合 CI 门禁与回归对比，但样本少、不能代表真实用户网络与设备。
- RUM（真实用户监控）：样本量大、覆盖真实分布，适合看 P75/P95 与业务影响，但受采样与上报丢包影响。
- 结合方式：Lab 做门禁（不达标不发版），RUM 做验证与告警（发版后观察真实指标），两者指标口径必须统一（如都按 Chrome UA 的 INP 定义）。
- 追问点：RUM 采样策略——低流量页面全量、高流量页面按 5%~10% 采样 + 抽样保持用户一致性（按 uid 哈希）。

```javascript
// 统一指标口径的采集层：RUM 上报 + 本地 Lab 复现链接
import { onLCP, onINP, onCLS } from 'web-vitals';
function send(m) {
  const body = { name: m.name, value: m.value, rating: m.rating,
    url: location.pathname, build: __BUILD_ID__,
    conn: navigator.connection?.effectiveType,
    uidHash: hash(localStorage.uid ?? anonId()) % 100 };  // 分流桶
  navigator.sendBeacon('/rum', JSON.stringify(body));
}
onLCP(send); onINP(send); onCLS(send);
// Lab 侧：CI 生成 Lighthouse 报告并附"复现链接"，RUM 告警可直接跳转复现
```
