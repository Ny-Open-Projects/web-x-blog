---
title: [1171] 跨团队的 Agent 怎么互相发现与调用（A2A 思路）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 生态]
type: 面试题
---

## 1171：跨团队的 Agent 怎么互相发现与调用（A2A 思路）

**答**：
- 发现机制：Agent 目录（能力描述 + 输入输出 schema + SLA + 负责人），调用方按能力检索；类似服务目录，但描述的是「能力」而非「接口」。
- 调用契约：请求带任务书（目标/约束/预算），响应带「可验证凭证」（执行摘要 + 产物引用）；跨团队调用的鉴权走能力令牌（调用方的权限上限传递并收窄）。
- 治理三件：调用配额（防某团队的 Agent 吃光共享资源）、质量责任（被调方对 SLA 负责，调用方对任务书质量负责）、兼容承诺（schema 变更提前 N 天通告）。
- 追问钩子：跨团队调用最大的坑？——责任模糊：调用失败双方互相甩锅；对策是「契约即合同」——schema/SLA/配额全部写进目录条目并版本化，争议按契约裁决。

```ts
const directory = {
  find: cap => db.agents.byCap(cap).filter(a => a.sla.ok),
  register(a) { require(a.schema && a.sla && a.owner, '目录条目不全'); return db.agents.add(a); },
};
async function callRemote(cap, brief, callerCap) {
  const a = directory.find(cap)[0];
  const token = await issue({ scope: intersect(callerCap, a.required), ttl: 600 });
  return a.invoke(brief, { token });   // 权限收窄后调用
}
```
