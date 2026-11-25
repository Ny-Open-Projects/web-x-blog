---
title: [SCN-1134] IoT 设备控制台的告警规则配置界面
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1134：IoT 设备控制台的告警规则配置界面

**答**：
- 配置：阈值/持续时间/恢复条件/通知方式——表单化配置（避免表达式门槛）。
- 测试：规则测试（历史数据回放验证触发情况）。
- 版本：规则变更历史（回滚到上一版）。

```javascript
// 告警规则配置
function alertRuleForm(rule) {
  return {
    fields: { metric: rule.metric, op: rule.op, threshold: rule.threshold,
      duration: rule.durationMin, notify: rule.channels },
    replay: (range) => replayAlerts(rule, range),      // 历史回放测试
    versions: rule.history,
    rollback: (v) => api('/alert-rule/rollback', { id: rule.id, version: v }),
  };
}
function replayAlerts(rule, range) { return { triggered: 3 }; }
```
