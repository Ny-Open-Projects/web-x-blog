---
title: [PER-170] 性能劣化的快速定位 SOP（1 小时内从告警到根因）？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-170：性能劣化的快速定位 SOP（1 小时内从告警到根因）？

**答**：
- 时间盒设计：**5 分钟**确认影响面与版本切片（是否发布引起）→ **10 分钟**多维切片定位维度 → **15 分钟**本地 Lab 复现 → **15 分钟**链路验证（TTFB 分离服务端/前端）→ **15 分钟**产出止血方案。
- 决策树第一叉是版本：新版本独有 → 直接走回滚；与版本无关 → 按维度继续切（机型/网络/第三方）。
- 止血优先级：**回滚 > 开降级开关 > 预算内热修**；任何止血动作要先在值班群同步，再执行。
- SOP 要脚本化：把切片查询、Lighthouse 复测、TTFB 探测写成一条命令，值班同学零思考执行。

```bash
#!/bin/bash
# 性能劣化快速定位 SOP：告警到根因控制在 1 小时内
set -euo pipefail

# 第 1 步（5 分钟）：确认面与版本，排除发布因素
curl -s "https://monitor.example.com/api/slice?metric=lcp_p75&by=release" | jq '.[:3]'
# 新版本独有 -> 直接走回滚预案；与版本无关 -> 继续

# 第 2 步（10 分钟）：切片定位维度（机型/网络/地域）
curl -s "https://monitor.example.com/api/slice?metric=lcp_p75&by=deviceClass,netType" | jq '.[:5]'

# 第 3 步（15 分钟）：本地 Lab 复现
npx lighthouse "$URL" --preset=perf --output=json --quiet > lab.json
jq '.audits["largest-contentful-paint"].numericValue' lab.json
jq '.audits["third-party-summary"].items[0]' lab.json

# 第 4 步（15 分钟）：链路验证，TTFB 分离服务端与前端责任
curl -o /dev/null -sw "TTFB=%{time_starttransfer} total=%{time_total}\n" \
  -H "traceparent: 00-$(openssl rand -hex 16)-$(openssl rand -hex 8)-01" "$URL"
# TTFB 抬升 -> 找后端与 CDN；TTFB 正常 -> 前端资源，看 Lab 明细

# 第 5 步（15 分钟）：产出报告与止血项
# 止血优先级：回滚 > 开降级开关 > 预算内修复；修复项进 ROI 矩阵排期
```
