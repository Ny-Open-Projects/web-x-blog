---
title: [ENG-115] DORA 指标怎么在前端团队落地？数据怎么采集？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-115：DORA 指标怎么在前端团队落地？数据怎么采集？
**答**：
- 四个指标：部署频率、变更前置时间（lead time）、变更失败率、故障恢复时长（MTTR）。
- 采集源：CI 事件（流水线开始/结束/部署）+ 代码事件（commit/MR）+ issue 事件（故障单开关时间）。
- 落地方式：CI 结束时把结构化事件写入数据仓（或直接用 DevLake 类工具聚合），看板按周展示趋势。
- 用法：指标是改进的探针不是考核的鞭子，关注四者的联动关系（部署频率提高是否带来失败率上升）。

```bash
# 用 git 与 issue 数据近似采集 DORA 指标
# 1. 部署频率：按部署 tag 统计
git tag --list 'deploy/2026-11*' | wc -l

# 2. 变更前置时间：commit 时间与合入时间的差值（配合 CI 事件更准确）
git log --since='1 month ago' --format='%ct %H' main | head -5

# 3. MTTR：故障 issue 从创建到关闭的时长
gh issue list --label incident --state closed --json createdAt,closedAt \
  | jq '[.[] | (((.closedAt | fromdate) - (.createdAt | fromdate)) / 3600)] | add / length'
```
