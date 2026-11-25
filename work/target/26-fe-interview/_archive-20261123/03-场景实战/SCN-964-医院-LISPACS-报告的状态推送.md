---
title: [SCN-964] 医院 LIS/PACS 报告的状态推送
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-964：医院 LIS/PACS 报告的状态推送

**答**：
- 状态：检验中→已出报告（分项出报告：先出的先推）。
- 推送：订阅消息/短信 + 小程序红点；影像报告（PACS）出片提醒。
- 体验：已出报告列表按时间倒序，点击直达报告详情（957 展示）。

```javascript
// 报告推送
function reportSubscription(patientId) {
  return subscribe({
    event: 'report-ready',
    on: (report) => {
      markRedDot(report.id);
      if (report.critical)                            // 危急值强提醒
        showCriticalBanner(report);
    },
  });
}
// 危急值（如血钾极值）：横幅强提醒 + 建议立即就医，医生端同步通知
```
