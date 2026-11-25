---
title: [PER-1138] 数据可携权（Data Portability）的工程实现
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1138：数据可携权（Data Portability）的工程实现

**答**：
- 要求：用户可获取其数据（结构化通用格式）并迁移到其他服务；GDPR Art.20/个保法相应条款。
- 实现：导出任务（异步生成 JSON/CSV 归档）→ 签名临时链接 → 通知下载；覆盖所有可识别个人的数据。
- 格式：JSON 为主（含 schema 版本），大附件给引用 URL（有时效）。
- 边界：导出不包含他人数据（群聊记录只含本人消息）、不包含商业机密（算法/内部配置）。

```javascript
// 数据导出任务
async function exportUserData(uid) {
  const parts = await Promise.all([
    db.user.find(uid), db.orders.byUser(uid),
    db.events.bySubject(hash(uid)),
  ]);
  const bundle = { schema: 'export-v2', subject: hash(uid),
    generatedAt: new Date().toISOString(), data: parts };
  const url = await putToTemp(JSON.stringify(bundle), { ttl: 24 * 3600_000 });
  logAudit(uid, 'export', 'GDPR Art.20');
  return { downloadUrl: sign(url, { ttl: 3600_000 }), expiresIn: '1h' };
}
```
