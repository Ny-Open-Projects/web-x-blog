---
title: [PER-1154] 多辖区合规的差异处理（GDPR/CCPA/个保法）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1154：多辖区合规的差异处理（GDPR/CCPA/个保法）

**答**：
- 差异点：合法基础（GDPR 多基础 vs 个保法同意中心）、删除权时限、可携权格式、敏感数据定义。
- 工程策略：以最严格辖区为基线（统一高水位实现），辖区差异只影响 UI 文案与流程细节。
- 区域路由：账号区域决定适用政策版本（1002 的区域路由延伸），政策与同意按区域版本管理。
- 变更监控：法规更新跟踪清单，评估影响面，季度合规评审。

```javascript
// 辖区策略基线
const STRICTEST = { consent: 'opt-in', eraseDays: 30, exportDays: 30,
  sensitiveSeparateConsent: true };
function regionalAdjust(region, base = STRICTEST) {
  // 高水位实现：所有辖区统一按 STRICTEST，仅 UI 差异
  return { ...base, ui: {
    gdpr: { banner: true, granular: true },
    ccpa: { optOut: 'Do Not Sell 链接' },
    cn: { separateConsentList: ['人脸', '位置', '身份证'] },
  }[region] };
}
```
