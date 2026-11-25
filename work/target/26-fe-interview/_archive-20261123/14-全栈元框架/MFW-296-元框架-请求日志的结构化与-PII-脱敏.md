---
title: [MFW-296] 请求日志结构化与 PII 脱敏管线
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, RBL]
type: 面试题
---

## MFW-296：请求日志 PII 脱敏

**答**:
- 结构化基座：JSON 行日志（traceId/route/method/status/durationMs/userHash）——禁止字符串拼消息（不可查询不可脱敏）
- 脱敏管线分层：采集端白名单（只记声明字段——默认不记 body）、必须记录的敏感字段假名化（ userEmail → u_a3f…HMAC）、出口扫描（日志管道尾端 PII 正则二次网——双保险）
- 用户关联而不暴露：userHash = HMAC(uid, 日志盐)——可关联分析但反查不出真身（盐与日志库分离存储）
- 保留期与访问：日志 30 天热 + 审计要求延长的进冷存（访问审批）——「日志是负债」的默认心态

```javascript
log.info({
  traceId, route: '/order/:id', status: 200, ms: 42,
  userHash: hmac(uid, LOG_SALT),                       // 假名化
  // body 字段不进——白名单例外单独声明
})
// 出口网：email/phone 正则命中 → [PII] 替换 + 计数告警（发现漏白名单的源）
```
