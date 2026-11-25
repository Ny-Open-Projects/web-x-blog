---
title: [SCN-1193] SCADA 大屏的数据压缩与断点续传（历史站）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1193：SCADA 大屏的数据压缩与断点续传（历史站）

**答**：
- 压缩：历史数据旋压压缩（死区压缩）——存储减量，趋势还原需解压。
- 断点：采集断线期间设备本地缓存，恢复后补传（时间戳保留）。
- 查询：压缩数据查询透明（服务端解压聚合）。

```javascript
// 死区压缩
function deadbandCompress(points, { pct = 0.005 } = {}) {
  const out = [points[0]];
  for (const p of points.slice(1)) {
    const last = out[out.length - 1];
    if (Math.abs(p.v - last.v) / Math.max(1, Math.abs(last.v)) > pct)
      out.push(p);                                     // 超死区才存
  }
  return { compressed: out, ratio: +(1 - out.length / points.length).toFixed(2) };
}
```
