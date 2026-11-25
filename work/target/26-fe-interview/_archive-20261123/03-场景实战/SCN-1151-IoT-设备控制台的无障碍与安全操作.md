---
title: [SCN-1151] IoT 设备控制台的无障碍与安全操作确认
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1151：IoT 设备控制台的无障碍与安全操作确认

**答**：
- 确认：高危操作（重启/恢复出厂）二次确认（输入设备 SN 后缀验证）。
- 无障碍：控制按钮可键盘操作，状态不只靠颜色区分（图标+文字）。
- 防呆：危险操作锁（连续失败冷却）。

```javascript
// 高危操作确认
async function dangerousOp(device, op, input) {
  if (input !== device.sn.slice(-4))
    return { ok: false, reason: '请输入设备 SN 后 4 位确认' };
  if (this.coolingDown?.(device.id)) return { ok: false, reason: '操作冷却中' };
  auditLog({ type: 'dangerous-op', device: device.id, op });
  return sendCommand(device.id, op);
}
```
