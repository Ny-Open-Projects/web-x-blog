---
title: [OPS-073] 告警分级与值班 oncall 机制怎么设计？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-073：告警分级与值班 oncall 机制怎么设计？
**答**：
- 分级标准要可执行：P0 全站不可用（电话，15 分钟响应）、P1 核心功能受损（IM 群，30 分钟）、P2 非核心劣化（工单，工作日处理）、P3 优化建议（周会）。
- 路由规则：按告警标签（service/page/level）路由到对应 oncall，节假日轮值表提前排、交接有记录。
- 升级机制：30 分钟无响应自动升级到主管，1 小时升级到总监——告警必须有兜底责任人。
- 值班体验：oncall 手册（常见告警的 first response 动作）常备，新告警类型出现必须回填手册。

```yaml
# oncall-routing.yaml：告警分级与路由（告警平台配置）
levels:
  P0:
    desc: 全站不可用/资损/数据泄露
    channels: [phone-call, sms, im]
    ack_timeout: 5m
    response_sla: 15m
    escalation: [fe-oncall, fe-lead, eng-director]
  P1:
    desc: 核心功能受损或错误率超阈值
    channels: [im, sms]
    ack_timeout: 10m
    response_sla: 30m
    escalation: [fe-oncall, fe-lead]
  P2:
    desc: 非核心页面劣化/性能劣化
    channels: [im]
    ack_timeout: 4h
    response_sla: 下个工作日
  P3:
    desc: 优化建议/趋势提醒
    channels: [weekly-report]
routes:
  - match: { service: web-mall, type: js_error, level: P1 }
    to: fe-oncall
  - match: { service: web-mall, type: dial_test, level: P0 }
    to: fe-oncall            # 全站拨测失败直接 P0
    escalation_on_silence: 30m
schedules:
  fe-oncall:
    rotation: weekly
    members: [zhang.san, li.si, wang.wu, zhao.liu]
    handover_doc: https://wiki.example.com/oncall/handover
    runbook: https://wiki.example.com/oncall/fe-runbook
quiet_hours:               # 低优先级告警静默时段，防疲劳
  P2: "22:00-09:00"
  P3: always
```
