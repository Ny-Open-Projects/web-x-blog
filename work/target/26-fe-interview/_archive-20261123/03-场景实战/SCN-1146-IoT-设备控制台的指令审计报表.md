---
title: [SCN-1146] IoT 设备控制台的指令审计报表
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1146：IoT 设备控制台的指令审计报表

**答**：
- 报表：指令下发统计（按操作人/设备类型/时段），异常指令（非工作时间/高频）标记。
- 合规：审计报表导出（监管检查）。
- 风控：异常指令实时告警（权限异常操作）。

```javascript
// 指令审计
function cmdAudit(commands) {
  const odd = commands.filter(c => {
    const h = new Date(c.at).getHours();
    return h < 6 || h > 22;                            // 非工作时间
  });
  return {
    total: commands.length, oddHours: odd,
    export: () => exportAudit(commands),
    alert: odd.length > 10 ? '非工作时段指令偏多，建议核查' : null,
  };
}
```
