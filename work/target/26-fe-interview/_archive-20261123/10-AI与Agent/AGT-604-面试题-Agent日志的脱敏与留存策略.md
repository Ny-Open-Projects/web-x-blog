---
title: [AGT-604] Agent 日志里有用户隐私（对话内容/工具返回的业务数据），日志采集怎么做脱敏与分级留存？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-604：Agent 日志里有用户隐私（对话内容/工具返回的业务数据），日志采集怎么做脱敏与分级留存

**答**：
- 三级数据分级：L1 元数据（traceId/耗时/token 数）全量长期留；L2 参数与结果摘要（脱敏后）留 30 天；L3 全量对话与工具结果（加密）留 7 天且仅调试权限可取。
- 脱敏在采集端（SDK 内）做而不是在查询端做：正则（手机/邮箱/身份证）+ 结构化字段白名单双通道，漏网内容靠采样抽检兜底。
- 用户删除权的落实：会话删除时级联清理 L2/L3 日志（按 sessionId 索引），L1 匿名化保留（统计价值）。

```javascript
function logSpan(span, data, level = 2) {
  if (level >= 2) {
    data = redact(data, { patterns: PII_PATTERNS,   // 采集端脱敏
      whitelist: ['tool', 'status', 'elapsedMs'] });
    ttl(span, level === 3 ? 7 : 30);                // 分级 TTL
    if (level === 3) span.blobRef = encryptStore(data); // L3 加密外置
  } else Object.assign(span.attrs, data);           // L1 直接进 span
}
function purgeUser(userId) {                         // 删除权
  logIndex.byUser(userId).forEach(entry =>
    entry.level >= 2 ? hardDelete(entry) : anonymize(entry));
}
```

