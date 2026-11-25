---
title: [SCN-975] 互联网医院的多学科会诊（MDT）编排
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-975：互联网医院的多学科会诊（MDT）编排

**答**：
- 编排：多科室医生会诊（主诊医生发起，各科医生加入），材料共享（病历/影像）。
- 前端：会诊室（多方视图+意见收集）、结论汇总（主诊医生签发）。
- 时序：意见收集截止时间、提醒未提交医生。

```javascript
// MDT 编排
function mdtRoom(session) {
  return {
    members: session.doctors.map(d => ({ ...d,
      submitted: !!d.opinion })),
    deadline: session.deadline,
    remind: session.doctors.filter(d => !d.opinion &&
      session.deadline - Date.now() < 4 * 3600_000),
    conclude: session.lead.id === currentUserId()
      ? () => api('/mdt/conclude', { id: session.id }) : null,   // 主诊签发
  };
}
```
