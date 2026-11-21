---
title: [AIC-130] AI 结对开发的安全审计日志记什么？出合规检查时怎么举证？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-130：AI 结对开发的安全审计日志记什么？出合规检查时怎么举证？
**答**：
- 审计日志五要素：谁（账号 + agent 实例）、做了什么（工具调用/代码变更/数据访问）、基于什么（任务 id、trace）、何时（时间戳）、产出去了哪（PR/分支）。
- 举证场景演练：① 数据合规检查「公司代码有没有发到外部模型」——举证=网关脱敏日志（AIC-076）+ 私有化/企业版协议 ② 事故调查「这段代码怎么来的」——举证=AI trailer（AIC-117）+ 任务 trace ③ 权限审计「agent 能否访问生产」——举证=权限三元组配置与越权记录（AIC-086）。
- 日志治理：分级存储（含代码的 trace 限内部）、保留期策略（合规通常要求 ≥ 1 年）、不可篡改（append-only 存储）。
- 关键设计：日志在平时就按「能直接回答审计问题」的结构组织——出事才补日志等于没日志。
- 追问钩子：审计日志是「证据链」不是「大杂烩」——按合规问题反推日志 schema 是正确设计顺序。

```javascript
// 审计事件 schema（按举证问题反推设计）
const auditEvent = {
  who: { user: 'u123', agent: 'cursor-agent@v1.3' },
  what: { tool: 'fs.write', target: 'src/payment/index.ts', action: 'modify' },
  basis: { taskId: 'TICKET-8821', traceId: 'tr_9f2' },
  when: 1763512800000,
  output: { pr: '#421', branch: 'agent/TICKET-8821' },
};
```
