---
title: [OPS-158] DORA 四指标怎么定义与自动化采集？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-158：DORA 四指标怎么定义与自动化采集？
**答**：
- 四指标：部署频率、变更前置时间（commit→生产）、变更失败率（导致回滚/事故的发布占比）、服务恢复时长 MTTR。
- 数据全可从系统取：git 记录 + 发布审计（OPS-142 的发布单时间线）+ 事故记录，无需人工填报。
- 分级基线：elite（每日多次、前置 < 1h、失败率 0-15%、MTTR < 1h）到 low（月度、前置 > 1 月），用分位值而非均值。
- 指标用于团队改进方向（哪个环节最拖后腿），不用于个人考核——否则指标立刻失真。
- 与 SLO 错误预算联动解读：发布频率高但失败率也高，说明灰度与验证环节薄弱。

```bash
# DORA 指标自动化采集：全部从 git 与发布审计系统取数
# 1. 部署频率：当周生产发布单数
jq '[.[] | select(.env=="prod")] | length' /data/audit/deploys_week.json

# 2. 变更前置时间：发布单记录 commit → 生产时长，取 p50
jq '[.[] | select(.env=="prod") | .lead_time_minutes] | sort | .[length/2]' /data/audit/deploys_week.json

# 3. 变更失败率：导致回滚或事故的发布占比
jq '[.[] | select(.env=="prod")] as $p |
    ([$p[] | select(.rolled_back == true)] | length) * 100 / ($p | length)' /data/audit/deploys_week.json

# 4. MTTR：事故记录的恢复时长均值（分钟）
awk -F'\t' '/SEV/ {s += ($3 - $2)} END {if (NR) print "MTTR:", s/NR/60, "min"}' /data/incidents/current.log

# 5. 分级基线对照（elite→low）：部署 每日多次→月度；前置 <1h→>1mo；失败率 0-15%→46%+；MTTR <1h→>1mo
```
