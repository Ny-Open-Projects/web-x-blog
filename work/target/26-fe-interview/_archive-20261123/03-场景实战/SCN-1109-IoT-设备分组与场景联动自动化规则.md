---
title: [SCN-1109] IoT 设备分组与场景联动（自动化规则）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1109：IoT 设备分组与场景联动（自动化规则）

**答**：
- 联动：规则引擎（当 A 设备事件 → 触发 B 设备动作），前端可视化规则编辑器。
- 执行：规则执行记录（成功/失败/耗时），失败重试与告警。
- 调试：规则试运行（模拟输入看输出，不实际下发）。

```javascript
// 联动规则编辑
function automationRule(trigger, action, { dryRun = false } = {}) {
  return {
    rule: { when: trigger, then: action },
    test: () => simulate(trigger),                     // 试运行模拟
    apply: dryRun ? null : api('/automation', { trigger, action }),
    log: () => ruleExecLog(trigger.id),
  };
}
function simulate(t) { return { matched: true }; }
function ruleExecLog(id) { return []; }
```
