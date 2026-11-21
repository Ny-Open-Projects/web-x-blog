---
title: [SCN-175] 老板要每天看核心页面的性能趋势（LCP/INP/CLS），如何搭一条自动化看板链路？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-175：老板要每天看核心页面的性能趋势（LCP/INP/CLS），如何搭一条自动化看板链路？
**答**：
- 数据两条腿：线上真实用户数据（web-vitals 上报 → 数仓）是"体感"，实验室数据（Lighthouse CI 定时跑关键页面）是"可复现归因"，两条线都要有。
- 实验室侧自动化：CI 定时任务对核心页面矩阵（机型 × 网络 × 页面）跑 Lighthouse，结果结构化入库。
- 看板只展示"趋势 + 突变"：每天与上周基线对比，超阈值标红并自动建 issue，避免人肉盯曲线。
- 告警要带归因入口：突变时自动对比两次构建的资源体积（bundle diff），多数性能回退是资源膨胀。

```bash
#!/bin/bash
# 每日性能看板采集：Lighthouse CI 矩阵跑分 + 入库 + 突变检测
set -euo pipefail

PAGES=("home:https://www.example.com/" "list:https://www.example.com/list" "detail:https://www.example.com/item/1")
PROFILE=("mobile:slow4G" "desktop:4G")
OUT=./perf-results/$(date +%F)
mkdir -p "$OUT"

for p in "${PAGES[@]}"; do
  name="${p%%:*}"; url="${p#*:}"
  for prof in "${PROFILE[@]}"; do
    device="${prof%%:*}"
    lhci collect \
      --url="$url" \
      --numberOfRuns=3 \
      --settings.emulatedFormFactor="$device" \
      --settings.throttling.rttMs=150
    lhci assert --assertions.categories:performance=["error"] \
      || echo "::warning::${name}/${device} 性能分低于阈值"
    mv .lighthouseci "$OUT/${name}-${device}"
  done
done

# 结构化入库：提取关键指标供看板消费
node scripts/extract-metrics.js "$OUT" | curl -s -X POST "$METRICS_API/vitals" \
  -H 'Content-Type: application/json' -d @-

# 突变检测：与上周基线对比，超阈值自动建 issue
node scripts/compare-baseline.js --metric LCP --threshold 0.15 \
  && echo "OK" || node scripts/create-issue.js "性能回退 $(date +%F)"
```
