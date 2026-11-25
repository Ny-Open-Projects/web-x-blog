---
title: [PER-1146] 数据泄露事件（Breach）的响应与通报要求
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1146：数据泄露事件（Breach）的响应与通报要求

**答**：
- GDPR：72 小时内通报监管；影响高风险的个人需直接告知；个保法要求及时告知并补救。
- 响应流程：发现→遏制（切断泄露通道）→评估范围（哪些数据/多少人）→通报（监管+用户）→根因修复→复盘。
- 工程准备：泄露检测（异常导出告警）、影响评估的数据地图（知道什么数据在哪）、通报模板。
- 演练：年度泄露演练，检验 72h 时限内完成评估与通报的可行性。

```javascript
// 泄露影响评估
function assessBreach(event) {
  return {
    dataTypes: event.fields,                    // 泄露字段
    subjects: event.affectedCount,
    sensitivity: event.fields.every(f => FIELD_LEVEL[f] >= 3) ? 'high' : 'mid',
    notify: { regulator: '72h', users: event.fields.some(f => FIELD_LEVEL[f] >= 4) },
    containment: event.actions,                 // 已采取措施
  };
}
// 高敏字段泄露 -> 用户直接告知义务触发
```
