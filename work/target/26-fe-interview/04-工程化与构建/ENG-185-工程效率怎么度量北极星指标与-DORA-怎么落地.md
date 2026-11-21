---
title: [ENG-185] 工程效率怎么度量？北极星指标与 DORA 怎么落地？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-185：工程效率怎么度量？北极星指标与 DORA 怎么落地？
**答**：
- 北极星选一个能代表又快又稳的：常见是需求前置时间，或部署频率与变更失败率的组合视图。
- DORA 四指标打底：部署频率 变更前置时间 变更失败率 恢复时长；研发侧加评审时长与 CI 时长。
- 反指标防御：不度量代码行与提交数（会被博弈），度量团队不度量个人。
- 闭环：月度读数 → 找最差指标 → 专项改进 → 下月复核，指标不动说明措施失效要换方向。

```javascript
// scripts/dora-metrics.mjs —— 从 git tag 计算部署频率与前置时间
import { execSync } from 'node:child_process'

const tags = execSync('git tag --sort=-creatordate').toString().trim().split('\n').slice(0, 20).reverse()
let totalLead = 0
for (const tag of tags) {
  const releaseAt = execSync(`git log -1 --format=%ct ${tag}`).toString().trim() * 1000
  const firstAt = execSync(`git log ${tag}^..${tag} --format=%ct --reverse | head -1`).toString().trim() * 1000
  totalLead += (releaseAt - firstAt) / 864e5
}
const metrics = {
  部署频率: `${(tags.length / 4).toFixed(1)} 次/周`,
  变更前置时间均值: `${(totalLead / tags.length).toFixed(1)} 天`,
  // 变更失败率与恢复时长取自监控平台故障与回滚记录 接入点示意
}
console.log(JSON.stringify(metrics, null, 2))
```
