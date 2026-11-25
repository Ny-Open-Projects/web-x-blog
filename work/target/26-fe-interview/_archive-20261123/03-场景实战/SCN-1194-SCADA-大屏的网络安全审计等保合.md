---
title: [SCN-1194] SCADA 大屏的网络安全审计（等保合规）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1194：SCADA 大屏的网络安全审计（等保合规）

**答**：
- 合规：等保 2.0 要求——访问控制/日志审计/边界防护，前端配合（登录审计/操作审计）。
- 检查项：等保自查清单（密码策略/会话超时/日志留存 6 个月）。
- 整改：等保测评问题整改跟踪。

```javascript
// 等保自查
function mlps2Check(cfg) {
  return [
    { item: '密码策略', pass: cfg.pwdPolicy?.minLen >= 8 },
    { item: '会话超时', pass: cfg.sessionTimeout <= 10 * 60_000 },
    { item: '日志留存', pass: cfg.logRetentionDays >= 180 },
    { item: '双因素', pass: cfg.mfaEnabled },
  ].filter(i => !i.pass).map(i => i.item);             // 未达标项整改
}
}
```
