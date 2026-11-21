---
title: [PER-124] 国际化产品的隐私合规（GDPR/个保法）如何落地？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-124：国际化产品的隐私合规（GDPR/个保法）如何落地？

**答**：
- 三地核心要求：**GDPR**（明确同意、数据最小化、被遗忘权、数据可携带）、**个保法**（单独同意用于敏感处理、本地化要求、个人信息影响评估）、**CCPA**（选择退出出售）。
- 前端落地件：**同意管理平台 CMP**（分场景分目的的同意开关、记录同意凭证）、地理围栏（按地区启用不同合规模式）、Cookie 分类治理（必要/分析/营销）。
- 工程约束：同意前不加载非必要 SDK（分析/广告脚本必须在同意后才注入）、删除权提供数据导出与注销接口、埋点默认匿名化（IP 截断、userId 哈希）。
- 凭证留存：同意时间、版本、范围要可追溯，审计时能证明“该用户在何时同意了哪个版本的隐私政策”。

```javascript
// 同意管理平台：同意前不加载任何非必要 SDK
const CONSENT_VERSION = '2026-01';

const consent = JSON.parse(localStorage.getItem('cmp-consent') ?? 'null');

export function hasConsent(purpose) {
  if (!consent || consent.version !== CONSENT_VERSION) return false; // 政策升级需重新同意
  return Boolean(consent.purposes?.[purpose]);
}

export async function setConsent(purposes) {
  const record = { version: CONSENT_VERSION, purposes, ts: Date.now() };
  localStorage.setItem('cmp-consent', JSON.stringify(record));
  // 同意凭证上送留痕：审计可追溯“何时同意了哪个版本哪个范围”
  await fetch('/api/privacy/consent', { method: 'POST', body: JSON.stringify(record) });
  purposes.analytics && loadScript('/vendor/analytics.js');  // 同意后才注入分析 SDK
  purposes.ads && loadScript('https://ads.example.com/sdk.js');
}

// 埋点默认匿名化：合规模式下 IP 截断、userId 哈希
export function anonymize(event) {
  return {
    ...event,
    uid: event.uid ? sha256(event.uid + SALT).slice(0, 16) : null, // 不可逆哈希
    ip: undefined,                                                   // 前端不采集，服务端按地区决定是否截断存储
  };
}

// 被遗忘权：注销时前端触发全端数据清理
export async function eraseMe() {
  await fetch('/api/privacy/erase', { method: 'POST' }); // 服务端删除主数据
  localStorage.clear(); sessionStorage.clear();          // 本地残留清理
  indexedDB.databases?.().then((dbs) => dbs.forEach((d) => indexedDB.deleteDatabase(d.name)));
  location.assign('/goodbye');
}
```
