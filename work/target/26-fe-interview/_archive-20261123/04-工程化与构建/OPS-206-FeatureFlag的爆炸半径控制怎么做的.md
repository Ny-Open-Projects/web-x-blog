---
title: [OPS-206] Feature Flag 的爆炸半径控制（flag 也可能挂）怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## OPS-206：Flag 爆炸半径怎么控制？
**答**：
- flag 服务故障隔离：flag 读取必须本地默认值兜底（SCN-ENG-252），服务挂了页面照常渲染（用默认值），绝不阻塞渲染链路。
- flag 决策缓存：决策结果带版本戳缓存（本地 + CDN），服务恢复后增量拉取——flag 服务的可用性要求是「最终一致」而非强一致。
- 变更防误操作：flag 值变更有审批（高危 flag 双人）+ 变更审计 + 一键回滚（上一次值快照）——flag 误改等价于线上事故。
- 关键 flag 的「熔断位」：核心链路的 flag 配置紧急关闭通道（不依赖 flag 服务可达——本地 kill-switch 文件）。
- 追问钩子：为什么核心 flag 需要「不依赖 flag 服务的本地 kill-switch」——flag 服务挂掉时你需要「关闭某个功能」却无法通过 flag 服务下发；本地 kill-switch（CDN 上的静态配置文件/构建时内置）是 flag 体系的最后一道不依赖自身的保险。

```javascript
// 三层读取：本地 kill-switch > 缓存决策 > 默认值
function getFlag(key) {
  if (localKillSwitch[key] !== undefined) return localKillSwitch[key];  // 通道 1
  const cached = decisionCache.get(key);                                 // 通道 2
  if (cached) return cached.value;
  return flagRegistry[key]?.default ?? false;                            // 通道 3
}
```
