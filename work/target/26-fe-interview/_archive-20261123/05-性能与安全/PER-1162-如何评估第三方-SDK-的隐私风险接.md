---
title: [PER-1162] 如何评估第三方 SDK 的隐私风险（接入评审）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1162：如何评估第三方 SDK 的隐私风险（接入评审）

**答**：
- 评审维度：采集字段清单（SDK 文档+抓包实测）、数据流向（上传到哪些域/区域）、是否含指纹行为、政策覆盖。
- 实测优先：SDK 文档不可信，沙箱环境抓包实测上报内容为唯一依据。
- 结论分级：可接入（需配置最小化）/ 需改造（关闭采集项）/ 拒绝（过度采集且无法关闭）。
- 持续：SDK 版本升级重测（抓包 diff），新增采集即触发重新评审。

```javascript
// SDK 隐私实测报告
async function sdkPrivacyAudit(sdkUrl) {
  const captured = await sandboxCapture(sdkUrl);   // 沙箱抓包
  const domains = [...new Set(captured.map(c => c.host))];
  const fields = [...new Set(captured.flatMap(c => c.bodyFields))];
  const fingerprinting = captured.some(c =>
    /canvas|webgl|font/i.test(JSON.stringify(c.body)));
  return { domains, fields, fingerprinting,
    verdict: fingerprinting ? 'reject' : fields.length > 10 ? 'review' : 'approve' };
}
```
