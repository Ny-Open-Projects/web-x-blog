---
title: [1111] Agent 安全的值班与漏洞响应 SLA 怎么定
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 运营]
type: 面试题
---

## 1111：Agent 安全的值班与漏洞响应 SLA 怎么定

**答**：
- 值班设计：安全告警分级路由——P0（高危绕过/数据泄露）实时呼叫、P1（防线异常）15 分钟响应、P2（情报类）次日处理；值班表覆盖模型/防线/基础设施三个域。
- 漏洞响应 SLA：内部发现 P0 修复 24h、外部报告（SRC）首次响应 4h、修复 72h、披露按协调流程；SLA 写进制度并度量达成率。
- 复盘制度：每个 P0/P1 出「事故报告」（时间线、根因、防线缺口、补丁），报告进知识库并转培训素材。
- 追问钩子：SLA 定了达不成怎么办？——SLA 与资源挂钩：响应时限决定需要的值班人力与自动化程度（P0 依赖自动化止血而非人力速度），达不成就先建自动化。

```ts
const sla = {
  P0: { ack: '5m', mitigate: '1h', fix: '24h', route: 'oncall-pager' },
  P1: { ack: '15m', fix: '72h' },
  P2: { ack: '1d' },
};
metrics.on('security_alert', a => {
  const s = sla[a.priority];
  pager.route(s.route, a);                        // 分级路由
  tracker.start(a, s);                            // SLA 计时
});
```
