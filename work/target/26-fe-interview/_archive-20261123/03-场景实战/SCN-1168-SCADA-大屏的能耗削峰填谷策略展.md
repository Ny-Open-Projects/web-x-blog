---
title: [SCN-1168] SCADA 大屏的能耗削峰填谷策略展示
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1168：SCADA 大屏的能耗削峰填谷策略展示

**答**：
- 策略：峰谷电价时段展示 + 可移负荷（储能/空调）削峰建议。
- 执行：削峰执行记录（负荷调整量）与节省电费量化。
- 验证：需量控制（最大需量接近合同容量预警）。

```javascript
// 削峰填谷
function peakShaving(load, priceTiers, demand) {
  const peak = priceTiers.find(t => t.type === 'peak');
  const shiftable = load.devices.filter(d => d.shiftable);
  return {
    peakHours: peak.hours,
    shift: shiftable.map(d => ({ device: d.id, kW: d.power,
      save: d.power * peak.price })),                  // 移峰节省
    demandWarn: demand.current > demand.contract * 0.9 ? '接近合同需量' : null,
  };
}
```
