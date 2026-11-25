---
title: [MFW-323] 版本化 API 与前端契约测试（防静默破坏）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-323：契约测试防破坏

**答**:
- 契约来源：前端实际消费的字段集（从代码扫描：query select/解构清单）生成「消费契约」——后端改接口时 CI 拿新响应 schema 对比消费契约（破坏性变更前置暴露）
- 版本策略：内部同仓同部署（Action 内联——无版本问题）；跨仓/对外 /v1 显式版本 + 弃用头（Sunset + 替代链接——RFC8594）
- 兼容写法纪律：只加字段不删改语义（消费方宽容读）；必须 breaking 时开 /v2 双跑一周期（流量迁移后删旧）
- 测试落位：契约快照进 CI（后端仓跑「前端消费断言」——跨仓契约用共享 schema 包或 OpenAPI diff 门禁）

```javascript
// 消费契约提取（简化）
const used = collectUsedFields(src, 'orderApi')      // AST 扫解构/访问
// CI: fetch(v1).json → keys ⊇? used；缺 → fail 'breaking change for web'
// Sunset 头：Sunset: <date>; Link: </v2/...>; rel="sunset"
```
