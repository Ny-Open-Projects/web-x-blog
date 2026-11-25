---
title: [SCN-1112] IoT 设备数据的时间序列存储查询（前端聚合展示）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1112：IoT 设备数据的时间序列存储查询（前端聚合展示）

**答**：
- 查询：原始 1s 数据不直接查询——服务端降采样（1m/1h 粒度聚合）返回。
- 前端：查询带粒度参数（zoom 联动粒度切换），多指标对比（同轴/双轴）。
- 导出：原始数据导出（异步任务，大数据量）。

```javascript
// 粒度查询
function telemetryQuery(deviceId, from, to, zoom) {
  const granularity = zoom > 30 ? '1h' : zoom > 7 ? '10m' : '1m';
  return api('/telemetry', { deviceId, from, to, granularity });
}
// zoom：天级视图用 1h，小时视图 10m，分钟视图 1m
```
