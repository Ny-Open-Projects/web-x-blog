---
title: [OPS-109] 怎么用 awk 分析 nginx 访问日志？QPS、状态码分布、慢请求怎么统计？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-109：怎么用 awk 分析 nginx 访问日志？QPS、状态码分布、慢请求怎么统计？
**答**：
- 先确认日志格式与列位置（$1=IP、$4=时间、$7=path、$9=status、最后一列=request_time 是常见格式），awk 脚本才能对号入座。
- QPS 按分钟聚合：cut 时间前缀 + uniq -c；状态码分布一条 awk 就能出 5xx 是否突增。
- 慢请求按 request_time 排序取 TOP，配合 P95/P50 分位看长尾分布而不是只看均值。
- 分析动作沉淀成脚本进值班工具箱（OPS-191），事故时直接跑而不是现场写。
- 大日志先 tail/grep 圈定时间窗再聚合，避免全量扫描拖慢排查。

```bash
# 日志格式约定：$remote_addr - [$time_local] "$request" $status $bytes "$referer" "$ua" $request_time
LOG=/var/log/nginx/access.log

# 1. 每分钟 QPS TOP 10
awk '{print $4}' "$LOG" | cut -d: -f1-4 | sort | uniq -c | sort -rn | head

# 2. 状态码分布（一眼看出 5xx 是否异常突增）
awk '{print $9}' "$LOG" | sort | uniq -c | sort -rn

# 3. 慢请求 Top20：request_time 为最后一列
awk '{print $NF, $7}' "$LOG" | sort -rn | head -20

# 4. 近 20 万条中 5xx 的 IP 聚合（定位受害面或攻击源）
tail -n 200000 "$LOG" | awk '$9 ~ /^5/ {print $1}' | sort | uniq -c | sort -rn | head

# 5. 某接口 P95 延迟：排序后取 95 分位
awk '$7=="/api/user/info" {print $NF}' "$LOG" | sort -n \
  | awk '{a[NR]=$1} END {if (NR>0) print "p95:", a[int(NR*0.95)]"s"}'
```
