---
title: [SCN-1123] IoT 设备的历史数据回填（补录与校准）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1123：IoT 设备的历史数据回填（补录与校准）

**答**：
- 场景：设备时钟漂移导致数据时间错乱——补录接口（带原始时间戳），平台按可信时间重排。
- 校准：NTP 校准状态上报，漂移量展示（设备时钟偏差）。
- 标识：补录数据打标（非实时采集），统计时区分。

```javascript
// 数据补录
async function backfill(deviceId, records) {
  const drifted = records.some(r => r.deviceTs - r.gatewayTs > 60_000);
  return api('/telemetry/backfill', { deviceId,
    records: records.map(r => ({ ...r,
      calibrated: r.gatewayTs ?? r.deviceTs,
      backfilled: true })),                            // 补录打标
    clockDrift: drifted };
}
// 统计查询排除 backfilled 或单独标注
```
