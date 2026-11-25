---
title: [NODE-698] 数据脱敏与日志合规（服务端）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-698：脱敏与日志合规怎么做？
**答**：
- 脱敏器统一：字段级脱敏规则表（SCN-FIN-544 规则表驱动——手机号/卡号/证件号）+ 场景策略（接口响应/日志/导出不同策略）；出口统一（所有出口过脱敏器——响应中间件/日志 serializer/导出任务）。
- 日志合规：敏感字段 redact（pino redact 白名单——SCN-NODE-646）、PII 标记传播（schema 字段标 pii——自动脱敏，SCN-联想-584 采集白名单同源）、日志留存期限（合规等级——SCN-FIN-625 保留策略）。
- 响应脱敏：服务端脱敏优先（明文不下发——SCN-FIN-509）；展示需要明文的按需接口（授权+审计）。
- 审计闭环：合规扫描（日志/响应抽样脱敏校验——CI 自动化，SCN-联想-584 CI 对齐）；泄露事件应急（轮换+溯源）。
- 追问钩子：为什么「出口统一脱敏器」优于「各业务点自行脱敏」——业务点自行脱敏靠记忆（新接口漏脱敏——日志里明文手机号）；出口统一（响应序列化器/日志 serializer 强制过脱敏器）让「新增出口自动被覆盖」——安全默认值做进出口（fail-closed），新增数据流默认受保护。

```javascript
// 出口统一：日志 serializer
const redact = { paths: ['*.phone', '*.idCard', 'req.headers.authorization'],
  censor: maskFn };                                    // pino redact
// 响应序列化脱敏
res.serializeUser = (user) => maskObject(user, { scene: 'partial' });   // SCN-FIN-544
// PII schema 标记
const UserSchema = z.object({ phone: pii(z.string()), name: pii(z.string()) });
```
