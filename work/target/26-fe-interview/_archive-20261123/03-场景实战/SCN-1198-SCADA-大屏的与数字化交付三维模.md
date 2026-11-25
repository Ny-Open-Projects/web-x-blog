---
title: [SCN-1198] SCADA 大屏的与数字化交付（三维模型/数字孪生联动）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1198：SCADA 大屏的与数字化交付（三维模型/数字孪生联动）

**答**：
- 联动：3D 数字孪生（设备三维模型绑定点位），大屏点击设备 → 3D 视图定位。
- 同步：3D 模型状态同步（运行/停机着色），轻量化（glTF 减面）。
- 降级：低端终端回退 2D 组态图。

```javascript
// 三维联动
function twinLink(device, twin) {
  return {
    focus: () => twin.focus(device.modelNodeId),       // 3D 定位
    color: twin.setColor(device.modelNodeId, stateColor(device.state)),
    fallback: device.lowEnd ? '2D 组态图' : null,
    model: { format: 'glTF', decimated: true },        // 减面轻量化
  };
}
function stateColor(s) { return s === 'running' ? 'green' : 'red'; }
```
