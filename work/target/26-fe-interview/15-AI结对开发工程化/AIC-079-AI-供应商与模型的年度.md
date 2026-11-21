---
title: [AIC-079] AI 工具供应商和模型的「年度复审」应该看什么？怎么避免被单一供应商锁定？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-079：AI 工具供应商和模型的「年度复审」应该看什么？怎么避免被单一供应商锁定？
**答**：
- 复审维度：能力（用团队基准任务集重跑对比，而不是看厂商发布会）、成本（单任务成本而非单价）、合规条款变化（隐私政策、保留策略是否偷偷改）、稳定性（限流、宕机记录）、生态（IDE 支持、Agent 能力演进）。
- 反锁定工程手段：① prompt/规则文件保持供应商中立格式（markdown + 槽位，不深绑专有语法）② 调用走统一网关层（换模型只改路由配置）③ 基准任务集是自己的，不依赖厂商榜单 ④ 至少一个备用供应商保持接入可用。
- 商务手段：合同写入数据可迁移条款、退出时的数据删除证明；席位采购留 10~20% 弹性。
- 复审产出是一份「去/留/切换」决策记录，写明依据数据——防止被厂商 demo 带节奏。
- 追问钩子：锁定的真正风险不是价格而是「团队习惯固化」——复审时要评估切换成本里的人员适应成本。

```javascript
// 供应商基准任务重跑（统一网关屏蔽差异）
async function benchmarkAll(tasks, vendors) {
  const results = {};
  for (const v of vendors) {
    results[v.name] = await runTasks(tasks, gateway(v)); // gateway 统一接口
  }
  return results; // 每任务: { pass, cost, duration, humanScore }
}
```
