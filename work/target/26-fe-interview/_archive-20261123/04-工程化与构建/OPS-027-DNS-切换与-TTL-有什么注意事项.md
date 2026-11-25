---
title: [OPS-027] DNS 切换与 TTL 有什么注意事项？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-027：DNS 切换与 TTL 有什么注意事项？
**答**：
- TTL 决定 DNS 记录在递归 DNS 里的缓存时长：切换前先把 TTL 降到 60~300 秒并等待"旧 TTL"时间生效，否则故障切换要等数小时。
- 计划内切换（迁移机房/换 CDN）：提前降 TTL → 预发验证新目标 → 低峰期改记录 → 监控解析生效比例（分地区 dig）。
- 故障切换：TTL 60s 也要算上客户端/中间resolver 的不遵守缓存，预期 1~5 分钟全量生效，期间用多 CDN/多可用区兜底。
- 改 DNS 一定要留回滚记录（原记录值截图/导出），并通知依赖方（App 端硬编码域名要检查）。

```bash
#!/usr/bin/env bash
# dns_switch.sh：计划内 DNS 切换的标准流程
set -euo pipefail
DOMAIN="static.example.com"
OLD_VALUE="static.example.com.cdn-a.net."
NEW_VALUE="static.example.com.cdn-b.net."
DNSPOD_API="https://dnsapi.cn/Record.Modify"
LOGIN="login_token=${DNSPOD_TOKEN}&format=json"

# 0. 前置：提前 24h 已把 TTL 降到 60（此处校验）
ttl=$(dig +noall +answer "$DOMAIN" CNAME @119.29.29.29 | awk '{print $NF}' | tr -d 'A-Za-z.')
# 上一步取不到时用权威 DNS 查询
[ -z "$ttl" ] && ttl=$(dig +noall +answer "$DOMAIN" @f1g1ns1.dnspod.net | head -1 | awk '{print $2}')
echo "current ttl: $ttl"
[ "$ttl" -gt 300 ] && { echo "ABORT: TTL 未提前降到 300 以内"; exit 1; }

# 1. 切换记录（先拿 record_id）
record_id=$(curl -fsS -X POST "https://dnsapi.cn/Record.List" \
  -d "$LOGIN&domain=example.com&sub_domain=static" | jq -r '.records[0].id')
curl -fsS -X POST "$DNSPOD_API" \
  -d "$LOGIN&domain=example.com&record_id=$record_id&sub_domain=static" \
  -d "record_type=CNAME&record_line_id=0&value=$NEW_VALUE&ttl=60"

# 2. 验证多地解析生效比例
for region in 119.29.29.29 223.5.5.5 8.8.8.8 1.1.1.1; do
  echo -n "$region -> "
  dig +short "$DOMAIN" @"$region" CNAME | head -1
done

# 回滚：把 value 换回 $OLD_VALUE 重新执行即可
echo "rollback value: $OLD_VALUE"
```
