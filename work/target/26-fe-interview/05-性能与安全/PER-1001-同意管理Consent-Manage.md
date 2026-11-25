---
title: [PER-1001] 同意管理（Consent Management）的工程实现
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1001：同意管理（Consent Management）的工程实现

**答**：
- 模型：同意分桶（必需/分析/广告/个性化），存储用户选择 + 版本号（政策更新需重新同意）。
- 接入：所有采集/个性化代码在对应桶授予后才初始化；SDK 加载改为"同意后动态注入"。
- 审计：记录同意变更事件（何时/何版本/何选择），可追溯到每次采集的合法性。
- 深水：拒绝广告桶 ≠ 可以继续用旧数据画像——要实现"撤回即停采并清理"。

```javascript
// 同意管理器
const CONSENT_KEY = 'cm.v2';
const DEFAULT = { analytics: false, ads: false, personal: false, v: 1 };
const listeners = [];
export const consent = {
  get: () => JSON.parse(localStorage.getItem(CONSENT_KEY) ?? 'null') ?? DEFAULT,
  set(next) {
    const val = { ...DEFAULT, ...next, v: DEFAULT.v };
    localStorage.setItem(CONSENT_KEY, JSON.stringify(val));
    listeners.forEach(f => f(val));
    report({ type: 'consent-change', ...val });      // 审计留痕
  },
  onChange(f) { listeners.push(f); },
};
// SDK 装载：consent.onChange(s => s.ads ? loadAdsSDK() : unloadAdsSDK());
```
