---
title: [SCN-1268] 国际电商的合规banner（Cookie/隐私同意按辖区）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1268：国际电商的合规banner（Cookie/隐私同意按辖区）

**答**：
- 差异：GDPR（欧盟 Cookie 同意横幅）/CCPA（Do Not Sell）/其他地区——按 IP/账号地区展示合规横幅。
- 实现：CMP 分辖区配置（1256），同意记录按辖区版本。
- 审计：同意/拒绝率分辖区统计（合规报告）。

```javascript
// 辖区合规横幅
function complianceBanner(region) {
  const CFG = {
    EU: { type: 'cookie-consent', granular: true },
    US_CA: { type: 'ccpa', link: 'Do Not Sell My Info' },
    default: null,
  }[region];
  if (!CFG) return null;
  return { ...CFG, version: policyVersion(region),
    record: choice => logConsent(region, choice) };
}
function policyVersion(r) { return 'v3'; }
function logConsent(r, c) { return true; }
```
