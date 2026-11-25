---
title: [OPS-021] CDN 缓存命中率异常怎么排查？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-021：CDN 缓存命中率异常怎么排查？
**答**：
- 先看大盘：命中率骤降通常伴随发布（新文件全量回源）或刷新操作，属预期；无发布却下降则要查配置与回源。
- 逐请求排查：抽样响应头判断命中与否（X-Cache/CF-Cache-Status 等），看 MISS 的原因（EXPIRED/PASS/BYPASS/DYNAMIC）。
- 常见根因：URL 带 query 未配置"忽略参数缓存"（如 ?t=时间戳直接打穿）、Set-Cookie 响应被 CDN 判为不可缓存、Range 请求未配置缓存。
- 用日志统计验证：拉 CDN 日志按命中状态与文件类型聚合，定位是哪类资源拖低命中率。

```bash
#!/usr/bin/env bash
# cdn_hitrate_check.sh：基于 CDN 边缘节点日志（或源站回源日志）分析命中率
LOG=${1:-/var/log/nginx/cdn_access.log}

echo "== 总体命中率 =="
awk '{hit[$4]++} END {
  total=hit["HIT"]+hit["MISS"]+hit["EXPIRED"]+hit["PASS"]+hit["DYNAMIC"];
  printf "HIT %.1f%%  MISS %.1f%%  PASS %.1f%%\n",
    hit["HIT"]/total*100, hit["MISS"]/total*100, hit["PASS"]/total*100
}' "$LOG"

echo "== MISS 原因 Top（EXPIRED 正常，PASS/DYNAMIC 偏多说明配置问题） =="
awk '$4!="HIT" {print $4, $7}' "$LOG" | sort | uniq -c | sort -rn | head -10

echo "== 带随机 query 打穿缓存的 URL（?t= 或时间戳参数） =="
awk '$4=="MISS" && $7 ~ /\?(t|ts|_)=?[0-9]{10}/ {print $7}' "$LOG" \
  | sed 's/\?.*//' | sort | uniq -c | sort -rn | head -10

echo "== 建议：对上述路径在 CDN 配置忽略该 query 参数参与缓存键 =="
```
