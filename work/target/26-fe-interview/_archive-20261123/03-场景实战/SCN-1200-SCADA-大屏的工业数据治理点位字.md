---
title: [SCN-1200] SCADA 大屏的工业数据治理（点位字典管理）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1200：SCADA 大屏的工业数据治理（点位字典管理）

**答**：
- 字典：点位字典（tag/描述/单位/量程/报警限值）统一管理，组态引用字典。
- 变更：点位变更流程（申请→审核→生效），组态同步更新。
- 质量：点位覆盖率审计（应接入未接入点位清单）。

```javascript
// 点位字典
function tagDictionary(tag) {
  return {
    tag: tag.id, desc: tag.desc, unit: tag.unit,
    range: [tag.low, tag.high], alarm: [tag.alarmLow, tag.alarmHigh],
    change: (patch) => api('/tag/change-request', { tag: tag.id, patch }),   // 变更走流程
    audit: coverageAudit(),                            // 覆盖率审计
  };
}
function coverageAudit() { return { missing: 12 }; }
```
