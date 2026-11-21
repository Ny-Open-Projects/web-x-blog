---
title: [OPS-151] 埋点与隐私合规（GDPR/个保法）要注意什么？Cookie Consent 怎么实现？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-151：埋点与隐私合规（GDPR/个保法）要注意什么？Cookie Consent 怎么实现？
**答**：
- 数据最小化：必传字段只有事件名/时间戳/页面路径；手机号、证件、邮箱等 PII 明文禁止上报，采集前 sanitize。
- 授权分级：统计、营销、会话回放分别授权；未授权前不初始化对应 SDK、不写非必要 Cookie。
- 个保法关注"单独同意"项（设备指纹、精准画像）与最小必要；GDPR 关注合法性基础与用户权利（访问/删除/导出）。
- IP 匿名化（截断存储）、数据留存期声明、按用户删除数据的能力是平台必备。
- 合规不是一次性：新增埋点走隐私评审进 Checklist（OPS-150），第三方 SDK 的数据流向也要纳入治理（OPS-152）。

```javascript
// 隐私合规：授权分级 + 数据脱敏 + 用户权利
const consent = { analytics: false, marketing: false, replay: false };

function onConsentChange(next) {
  Object.assign(consent, next);
  if (consent.analytics) initAnalytics({ anonymizeIp: true });  // IP 截断存储
  else teardownAnalytics();
  if (consent.replay) startRRWeb();      // rrweb 仅明确授权后启动（OPS-131）
  else stopRRWeb();
}

// 埋点脱敏：PII 字段在采集层直接剥离，绝不离开浏览器
function sanitize(props) {
  const { phone, idCard, email, name, ...rest } = props;   // eslint 标注禁报字段
  return rest;
}

// 用户权利支持：数据导出与删除（GDPR / 个保法要求）
async function deleteUserTraces(uid) {
  await fetch('/api/privacy/delete', { method: 'POST', body: JSON.stringify({ uid }) });
}
```
