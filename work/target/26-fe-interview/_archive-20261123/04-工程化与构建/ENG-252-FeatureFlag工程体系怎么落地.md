---
title: [ENG-252] Feature Flag 工程体系怎么落地？flag 的生命周期怎么管？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-252：Feature Flag 体系怎么落地？
**答**：
- flag 类型分级：发布 flag（临时，功能完成后删）、实验 flag（A/B，实验结束删）、运维 flag（长期，降级开关）、权限 flag——类型决定生命周期与清理 SLA。
- 生命周期管理：flag 注册（名称/owner/过期日期/默认值）→ 使用 → 到期清单自动提醒 → 删除 PR 自动生成——僵尸 flag 是代码腐化的慢性病。
- 技术要求：读取本地缓存默认值（flag 服务挂了不阻塞渲染）、决策一致（同会话同值，防 UI 抖动）、依赖声明（flag 间依赖显式）。
- 度量：flag 数量趋势（增长失控告警）、flag 评估耗时（热路径上的开关判断要便宜）。
- 追问钩子：为什么「到期清单 + 自动删除 PR」是 flag 体系的核心运维——没有清理机制的 flag 系统必然膨胀到没人敢动；把删除做成自动化（到期提醒 → 一键生成清理 PR）让卫生成本趋近于零。

```javascript
// flag 定义（带生命周期元数据）
flag.define('checkout-v2', { type: 'release', owner: 'pay-team',
  expiresAt: '2026-12-01', default: false });
// 读取：本地默认 + 缓存决策（服务挂了不阻塞）
const on = flags.get('checkout-v2', { sessionSticky: true });
// 到期清理
cron('0 9 * * 1', () => expiredFlags().forEach(f =>
  createDeleteFlagPR(f)));             // 自动生成清理 PR
```
