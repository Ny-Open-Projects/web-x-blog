---
title: [SCN-942] 政务大厅的访客 Wi-Fi 与门户页
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-942：政务大厅的访客 Wi-Fi 与门户页

**答**：
- 门户：连 Wi-Fi 弹门户页（办事指南/排队查询/下载 App 引导）。
- 认证：短信/一键认证；时效（4 小时自动登出）。
- 性能：门户页极简（< 100KB），弱网可用。

```javascript
// 门户页
function wifiPortal() {
  return {
    size: '<100KB', inline: true,                     // 全内联资源
    features: ['queue-query', 'guide', 'app-download'],
    auth: { sms: true, ttlHours: 4 },
  };
}
// 排队查询免登录（输ticket号即查）——降低门槛
```
