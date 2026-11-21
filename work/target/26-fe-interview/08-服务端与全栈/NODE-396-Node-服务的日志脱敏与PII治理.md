---
title: [NODE-396] Node 服务的日志脱敏与 PII（个人信息）治理如何落地？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-396：日志脱敏与 PII 治理
**答**:
- PII 分类：直接标识（手机号/身份证/姓名）、准标识（IP/UA/设备号）、业务敏感（余额/地址）。分级策略：直接标识默认不出日志（哈希化/掩码），准标识低敏感可保留但可配置清除。
- 技术落点：logger 序列化层统一脱敏（redact 白名单/黑名单字段——pino redact 路径匹配 phone/idCard）；对象整体 dump 前深度扫描（正则识别手机号/身份证模式替换）；错误堆栈里的参数脱敏（NODE-358 上报前处理）。
- 治理机制：字段分级清单（哪些字段是什么级别，schema 声明驱动脱敏规则）；新接口评审含"PII 流向"检查（会不会进日志/会不会进前端埋点 ARC-154）。
- 权限与保留：原始日志访问权限收紧（脱敏前数据的查看需审批）；保留期分级（PII 类日志短保留期）。
- 验证：日志抽样扫描（自动检测残留 PII，命中率告警）作为常态化巡检。
```javascript
const logger = pino({ redact: {
  paths: ['req.headers.authorization', '*.phone', '*.idCard', 'user.password'],
  censor: '[REDACTED]'
}});
// 深度兜底：dump 前扫描
function scrub(obj) { return deepMap(obj, v =>
  typeof v === 'string' ? v.replace(/1[3-9]\d{9}/g, m => mask(m)) : v); }
```
