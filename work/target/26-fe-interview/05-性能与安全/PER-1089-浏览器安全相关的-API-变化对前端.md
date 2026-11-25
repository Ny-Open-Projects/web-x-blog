---
title: [PER-1089] 浏览器安全相关的 API 变化对前端的影响盘点
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1089：浏览器安全相关的 API 变化对前端的影响盘点

**答**：
- 第三方 Cookie 分区（CHIPS）：三方场景存储需 Partitioned 属性，否则被清除。
- Storage partitioning：localStorage/IndexedDB 按顶级站点分区，嵌入场景数据不再跨站共享。
- Private Network Access：公网页面访问内网资源需预检授权，内网管理系统嵌入公网页面会受影响。
- Permissions-Policy：可禁用摄像头/地理位置等能力，防止 iframe 子页滥用。

```javascript
<!-- Permissions-Policy 响应头示例 -->
// Permissions-Policy: camera=(), geolocation=(self), interest-cohort=()
// 前端探测：
const cameraAllowed = document.featurePolicy
  ?.allowsFeature?.('camera') ?? 'unknown';
if (!cameraAllowed) disableScanFeature();
// PNA 预检失败处理：
fetch('http://intranet.admin/api', { mode: 'cors' })
  .catch(e => { if (e.message.includes('private network'))
    showIntranetGuide(); });
```
