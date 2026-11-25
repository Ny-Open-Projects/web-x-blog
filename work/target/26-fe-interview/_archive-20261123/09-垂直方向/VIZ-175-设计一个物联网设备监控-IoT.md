---
title: [VIZ-175] 设计一个物联网设备监控（IoT）。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-175：设计一个物联网设备监控（IoT）。
**答**：① **设备树**——站点→网关→设备层级树表 + 状态点，万级设备虚拟滚动；② **遥测时序**——多通道曲线（温度/电流），min-max 降采样（VIZ-129），时间刷联动多图；③ **告警**——阈值越限：设备树标红 + 时序图阈值线 + 告警时刻数据快照存档；④ **离线处理**——心跳超时灰显，恢复后补数据（回填窗口标注）；⑤ **聚合视图**——按设备类型分组的均值带（P50/P95 阴影带），单设备下钻看原始曲线。

```javascript
// 遥测时序：阈值线 + P50/P95 聚合带 + 单设备下钻
function telemetryOption(deviceData, thresholds, aggBand) {
  return {
    series: [
      ...(deviceData ? [{ type: 'line', data: minMaxSample(deviceData, 2000), name: 'raw' }] : []),
      ...(aggBand ? [{ type: 'line', data: aggBand.p50, lineStyle: { width: 2 } },
                      { type: 'line', data: aggBand.p95, areaStyle: { opacity: 0.15 } }] : []),
    ],
    markLine: { silent: true, symbol: 'none',
      data: thresholds.map(t => ({ yAxis: t.value,
        lineStyle: { color: t.level === 'warn' ? '#f59e0b' : '#ef4444' },
        label: { formatter: t.name } })) },          // 阈值越限线
    dataZoom: [{ type: 'inside' }],                  // 时间窗刷选联动
  };
}
// 心跳超时：设备状态 = now - lastHeartbeat > offlineMs ? 'offline' : status
```
