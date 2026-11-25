---
title: [SCN-1179] SCADA 大屏的预测性维护展示（设备健康度）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1179：SCADA 大屏的预测性维护展示（设备健康度）

**答**：
- 健康度：振动/温度特征 → 设备健康评分（模型输出），评分趋势（劣化预警）。
- 建议：预测剩余寿命（RUL）+ 维护建议窗口（下次停机时更换）。
- 降级：模型未覆盖设备回退阈值监控。

```javascript
// 预测性维护
function predictiveHealth(device, model) {
  if (!model.covers(device.type))
    return { mode: 'threshold', note: '该机型未建模，走阈值监控' };
  return {
    health: model.score(device),                       // 0~100
    rul: model.remainingLife(device),                  // 剩余寿命
    window: model.maintWindow(device),                 // 建议维护窗口
    trend: device.healthHistory.slice(-10),
  };
}
```
