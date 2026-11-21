---
title: [OPS-086] 典型事故复盘（postmortem）模板包含哪些部分？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-086：典型事故复盘（postmortem）模板包含哪些部分？
**答**：
- 固定结构：摘要（影响面+时长）、时间线（每个动作的时间戳）、根因（5 Why 到系统性原因）、影响量化（请求失败数/用户数/资损）、改进项（负责人+期限）。
- 复盘文化：对事不对人， blameless 原则——追责会让下一次事故被隐瞒，隐瞒比事故本身更危险。
- 根因要回答"为什么防线没拦住"：缺监控？缺开关？回滚不熟练？改进项必须落到"可验证的自动化/流程改动"。
- 改进项进迭代跟踪，下季度复盘时先检查上次改进项完成率。

```yaml
# postmortem-template.yaml：事故复盘模板（P0/P1 强制 48h 内提交）
incident:
  id: INC-2026-1101-01
  title: 详情页改版发布导致白屏
  level: P1
  blameless: true          # 复盘原则：对事不对人

summary:
  impact: 移动端详情页约 35% 会话白屏
  duration: 14:23 - 14:51（28 分钟）
  quantified:
    affected_sessions: 18234
    error_peak: 31%
    revenue_impact: 无直接资损，转化率下降 12%（持续期间）

timeline:
  - { t: "14:23", e: 监控告警 JS 错误率超阈值，值班确认 }
  - { t: "14:26", e: 定位到 14:20 的灰度发布 }
  - { t: "14:31", e: 暂停放量，错误率不再扩大 }
  - { t: "14:38", e: 决策回滚（旧版本兼容已确认） }
  - { t: "14:45", e: 回滚完成 + CDN 刷新 }
  - { t: "14:51", e: 指标恢复基线，宣布恢复 }

root_cause:
  five_whys:
    - 白屏：新版入口引用了不存在的 chunk
    - chunk 缺失：CDN 刷新把旧 hash 资源一并清掉
    - 为什么会清：刷新脚本误用目录刷新
    - 为什么误用：发布脚本未区分入口与资源
    - 系统性原因：发布工具缺少"禁止对 hash 资源做目录刷新"的防护
  why_not_prevented: 预发未接入真实 CDN 链路，刷新路径未演练

action_items:               # 改进项必须可验证、有 owner、有 deadline
  - { action: 发布脚本禁止对 /assets 做目录刷新, owner: zhang.san, due: 2026-11-08 }
  - { action: 预发接入与生产同构的 CDN 配置, owner: li.si, due: 2026-11-15 }
  - { action: 回滚演练纳入每季度值班培训, owner: wang.wu, due: 2026-12-01 }
```
