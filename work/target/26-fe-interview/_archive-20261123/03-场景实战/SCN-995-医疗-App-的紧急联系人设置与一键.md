---
title: [SCN-995] 医疗 App 的紧急联系人设置与一键呼救
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-995：医疗 App 的紧急联系人设置与一键呼救

**答**：
- 呼救：一键 SOS（定位+病史摘要发送紧急联系人+急救中心）。
- 防误触：长按 3 秒 + 倒计时取消（防误触误报）。
- 联动：呼救后自动通知紧急联系人（短信+电话）。

```javascript
// 一键呼救
async function sos(patient) {
  const location = await locate({ accuracy: 'gps', timeoutMs: 3000 });
  const payload = { location, history: patient.criticalHistory };
  await Promise.all([
    api('/sos/dispatch', payload),                     // 急救中心
    ...patient.emergencyContacts.map(c =>
      sms(c.phone, `紧急求助：${patient.name}，位置已共享`)),
  ]);
  report({ type: 'sos', ms: performance.now() - t0 });
}
// 长按 3s + 倒计时 3s 可取消，防误触
```
