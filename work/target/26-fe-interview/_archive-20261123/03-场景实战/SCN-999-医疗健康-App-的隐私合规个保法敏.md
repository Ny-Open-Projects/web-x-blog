---
title: [SCN-999] 医疗健康 App 的隐私合规（个保法敏感信息专项）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-999：医疗健康 App 的隐私合规（个保法敏感信息专项）

**答**：
- 敏感：健康数据属 S4 敏感个人信息——单独同意 + 目的限定 + 最小化。
- 实现：健康数据采集逐项单独同意（963 模式）、撤回即停（1158 验证）。
- 审计：健康数据访问全留痕（DSAR 支持导出/删除）。

```javascript
// 健康数据合规
const HEALTH_SENSITIVE = ['diagnosis', 'prescription', 'mental-health'];
function healthConsentGate(dataType, consent) {
  if (HEALTH_SENSITIVE.includes(dataType) && !consent.separate?.[dataType])
    return { allowed: false,
      action: '单独同意弹窗（不得捆绑）' };
  return { allowed: true, audit: true };
}
```
