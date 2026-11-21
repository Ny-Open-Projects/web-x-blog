---
title: [OPS-089] 大促前 CDN 预热与大流量应对怎么做？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-089：大促前 CDN 预热与大流量应对怎么做？
**答**：
- 预热对象分层：入口 html（必须预热+刷新双做）、核心 JS/CSS chunk、首屏图片视频；按流量 Top N 与转化路径选资源。
- 预热时机：活动开始前 1~2 小时执行，并在开始后校验命中率（目标 > 95%）。
- 大流量应对：CDN 带宽弹性预估（峰值 QPS × 页面大小 × 系数）、回源保护（源站限流+多级缓存）、图片走专属图片域名便于独立限流。
- 预案：预热失败的资源清单要有告警与人工补推流程，不能"预热了就算做了"。

```bash
#!/usr/bin/env bash
# cdn_warmup.sh：大促预热与命中率校验
set -euo pipefail
CDN_API="https://cdn.console.example.com/api"
AUTH="Authorization: Bearer $CDN_TOKEN"

# 1. 生成预热清单：入口 + Top 资源（来自近 7 天访问日志统计）
{
  echo "https://www.example.com/index.html"
  awk -v f=$(( $(date +%s) - 604800 )) \
    '$1>=f && $7 ~ /^\/assets\/.*\.js$/ {print $7}' /var/log/nginx/access.json \
    | sort | uniq -c | sort -rn | head -50 | awk '{print "https://cdn.example.com"$2}'
  awk -v f=$(( $(date +%s) - 604800 )) \
    '$1>=f && $7 ~ /^\/img\/promo\// {print $7}' /var/log/nginx/access.json \
    | sort | uniq -c | sort -rn | head -100 | awk '{print "https://cdn.example.com"$2}'
} > /tmp/warmup.list
echo "预热资源数: $(wc -l < /tmp/warmup.list)"

# 2. 分批提交预热（每批 100，厂商配额限制）
split -l 100 /tmp/warmup.list /tmp/warmup_batch_
for batch in /tmp/warmup_batch_*; do
  jq -R . "$batch" | jq -s '{urls: .}' > "$batch.json"
  curl -fsS -X POST "$CDN_API/prefetch" -H "$AUTH" \
    -H "Content-Type: application/json" -d @"$batch.json"
  sleep 2
done

# 3. T+30min 命中率校验：抽样 100 个 URL 看边缘是否命中
sleep 1800
hit=0; total=0
head -100 /tmp/warmup.list | while read -r url; do
  total=$((total+1))
  xcache=$(curl -sI "$url" | grep -i 'x-cache' | head -1)
  echo "$xcache" | grep -qi 'HIT' && hit=$((hit+1))
done
echo "抽样命中率: $hit / $total"
awk -v h="$hit" -v t="$total" 'BEGIN{ if (t>0 && h/t < 0.95) exit 1 }' \
  || { echo "命中率低于 95%，触发补推告警"; \
       curl -fsS -X POST "$OPS_WEBHOOK" -d '{"msgtype":"text","text":{"content":"[P2] 大促预热命中率不达标，请人工补推"}}'; }
```
