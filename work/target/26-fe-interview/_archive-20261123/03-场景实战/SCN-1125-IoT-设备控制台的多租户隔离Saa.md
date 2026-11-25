---
title: [SCN-1125] IoT 设备控制台的多租户隔离（SaaS 化）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1125：IoT 设备控制台的多租户隔离（SaaS 化）

**答**：
- 隔离：租户设备/数据/规则隔离（tenant 维度），跨租户零可见。
- 配额：租户设备数/消息量配额（超限告警限流）。
- 计量：按设备/消息计量的用量报表（计费依据）。

```javascript
// 多租户
function tenantScope(user, query) {
  if (!query.tenantId || query.tenantId !== user.tenantId)
    return { ...query, tenantId: user.tenantId };      // 强制注入租户
  return query;
}
function tenantQuota(tenant, usage) {
  return { devices: usage.devices, limit: tenant.quota.devices,
    over: usage.devices > tenant.quota.devices,
    metering: usage.messagesPerDay };                  // 计量报表
}
}
```
