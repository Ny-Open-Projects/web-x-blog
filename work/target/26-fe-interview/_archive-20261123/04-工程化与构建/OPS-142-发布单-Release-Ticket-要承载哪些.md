---
title: [OPS-142] 发布单（Release Ticket）要承载哪些信息？怎么实现变更可追溯？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-142：发布单（Release Ticket）要承载哪些信息？怎么实现变更可追溯？
**答**：
- 发布单是发布的"身份证"：制品（版本+sha）、变更引用（Jira/MR/commit）、风险等级、checklist、时间线全部聚合。
- 三个方向都可追溯：按发布单反查代码、按 commit 反查发布、按制品 sha 反查产物——事故时三秒内回答"是不是这个发布引起的"。
- 时间线由系统自动写入（创建/审批/灰度各档/回滚），人工动作也走 API 留痕。
- 发布单与变更单/工单双向关联：合规审计与复盘取材都从这里来（OPS-185）。
- 发布单状态机驱动流程：不满足 checklist 就无法进入下一状态，工具替代自觉（OPS-180）。

```json
{
  "release_ticket": {
    "id": "REL-2026-0412",
    "status": "canary_25pct",
    "change_ref": {
      "jira": ["FE-1888", "FE-1901"],
      "commits": ["8f3d21c", "a1b2c3d"],
      "mrs": ["!2341", "!2344"]
    },
    "artifact": { "version": "1.42.0+g8f3d21c", "sha256": "e3b0c44298fc..." },
    "risk_level": "medium",
    "checklist": [
      { "item": "CI 全绿含安全扫描", "done": true },
      { "item": "预发回归通过", "done": true },
      { "item": "灰度看板阈值已配置", "done": true },
      { "item": "回滚预案已确认", "done": true }
    ],
    "timeline": [
      { "at": "2026-10-30T14:02:00+08:00", "event": "created",  "actor": "zhang" },
      { "at": "2026-10-30T14:10:00+08:00", "event": "approved", "actor": "li" },
      { "at": "2026-10-30T14:12:00+08:00", "event": "canary_5pct",  "actor": "pipeline" },
      { "at": "2026-10-30T14:40:00+08:00", "event": "canary_25pct", "actor": "pipeline" }
    ],
    "traceability": "事故时：ticket 反查发布 → commit 反查代码 → artifact sha 反查产物，三向互查"
  }
}
```
