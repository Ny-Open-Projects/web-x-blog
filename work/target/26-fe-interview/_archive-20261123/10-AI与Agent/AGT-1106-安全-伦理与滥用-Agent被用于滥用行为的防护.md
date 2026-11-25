---
title: [1106] 怎么防止用户借 Agent 批量滥用（刷评/骚扰/爬取）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 滥用]
type: 面试题
---

## 1106：怎么防止用户借 Agent 批量滥用（刷评/骚扰/爬取）

**答**：
- 滥用画像三维度：频率（单位时间动作数超人类合理水平）、模式（批量同构请求、目标轮换规律）、目标（被操作对象的投诉/防护触发）。
- 防护分层：速率硬限（每用户每工具 QPS 上限）、行为检测（同构请求聚类，批量模板识别）、目标方保护（对被操作方提供「Agent 流量标识」与拒收机制——尊重生态）。
- 治理闭环：滥用样本转检测规则；账号级处置阶梯（限速→验证→封禁），误判有申诉通道。
- 追问钩子：正常用户批量操作（如整理 100 篇笔记）和滥用的边界？——按「目标对象」区分：操作自己资产的是正常批量，触达他人资产/公共空间的批量是滥用高危，规则按目标对象归属分级。

```ts
async function rateAndAbuseGuard(user, action) {
  if (await rate.userQPS(user) > HUMAN_MAX) return throttle(user);
  const pattern = await cluster.today(user);
  if (pattern.isomorphic > 50 && targetsOthers(action)) {
    return abuseHold(user, pattern);               // 批量触达他人 = 高危
  }
  markAgentTraffic(action);                        // Agent 流量标识，尊重目标方
  return action.run();
}
```
