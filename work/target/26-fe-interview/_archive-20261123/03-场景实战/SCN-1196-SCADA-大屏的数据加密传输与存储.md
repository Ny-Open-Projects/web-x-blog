---
title: [SCN-1196] SCADA 大屏的数据加密传输与存储加密
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1196：SCADA 大屏的数据加密传输与存储加密

**答**：
- 传输：采集数据 TLS（国密 SM2/SM4 场景），存储透明加密（敏感工艺参数）。
- 密钥：密钥管理（定期轮换），密钥不落前端。
- 合规：商密改造（国密算法替换）进度跟踪。

```javascript
// 国密改造
function cryptoMigration(status) {
  return {
    tls: status.tls === 'sm2' ? 'done' : 'migrating',
    storage: status.storage === 'sm4' ? 'done' : 'migrating',
    keyRotation: status.keyRotateDays,
    note: '密钥不落前端，前端只见密文/脱敏',
  };
}
```
