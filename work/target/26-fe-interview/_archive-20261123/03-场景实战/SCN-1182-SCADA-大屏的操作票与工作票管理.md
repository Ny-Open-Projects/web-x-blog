---
title: [SCN-1182] SCADA 大屏的操作票与工作票管理
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1182：SCADA 大屏的操作票与工作票管理

**答**：
- 工作票：检修工作票（审批/许可/终结）流程前端展示，检修设备大屏标注（检修色）。
- 操作票：倒闸操作票步骤逐步确认（防误操作）。
- 联锁：检修设备与运行联锁（检修中禁止相关操作）。

```javascript
// 操作票
function operationTicket(ticket) {
  return {
    steps: ticket.steps.map(s => ({ ...s, confirmed: false })),
    confirm: (i) => {                                  // 逐步确认
      if (i !== ticket.currentStep) return { ok: false, reason: '须按顺序确认' };
      ticket.currentStep++;
      return { ok: true };
    },
    interlock: ticket.maintDevices,                    // 检修联锁设备
  };
}
```
