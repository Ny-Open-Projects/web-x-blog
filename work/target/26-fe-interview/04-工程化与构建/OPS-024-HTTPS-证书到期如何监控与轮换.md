---
title: [OPS-024] HTTPS 证书到期如何监控与轮换？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-024：HTTPS 证书到期如何监控与轮换？
**答**：
- 证书过期是低级但高频的事故：监控要覆盖所有对外域名，提前 30/14/7 天分级告警。
- 检查手段：脚本用 openssl 读取证书 notAfter 与当前时间比较；或接云厂商/UPTRUST 类监控。
- 轮换：能自动化的尽量 ACME 自动续期（certbot/acme.sh + DNS 验证），CDN/负载均衡侧证书同步上传并确认生效。
- 变更流程：证书更新也是变更，更新后要验证全域名链（含二级域名与 API 域名）。

```bash
#!/usr/bin/env bash
# cert_expiry_check.sh：检查证书到期天数，低于阈值告警（配合 crontab 每日执行）
DOMAINS=(
  www.example.com
  api.example.com
  static.example.com
  *.example.com
)
ALERT_WEBHOOK="$OPS_WEBHOOK"   # 企业微信/钉钉/Slack webhook

for d in "${DOMAINS[@]}"; do
  end=$(echo | openssl s_client -servername "$d" -connect "$d:443" 2>/dev/null \
    | openssl x509 -noout -enddate | cut -d= -f2)
  [ -z "$end" ] && { echo "FAIL: $d 无法读取证书"; continue; }
  end_ts=$(date -j -f "%b %e %H:%M:%S %Y %Z" "$end" +%s 2>/dev/null \
    || date -d "$end" +%s)
  days=$(( (end_ts - $(date +%s)) / 86400 ))
  echo "$d: ${days}d remaining"

  if [ "$days" -le 30 ]; then
    level=$([ "$days" -le 7 ] && echo P2 || echo P3)
    curl -fsS -X POST "$ALERT_WEBHOOK" -H 'Content-Type: application/json' \
      -d "{\"msgtype\":\"text\",\"text\":{\"content\":\"[$level] 证书告警 $d 还剩 ${days} 天到期，请安排续期\"}}"
  fi
done

# crontab：每天 09:00 执行
# 0 9 * * * /opt/ops/cert_expiry_check.sh >> /var/log/cert_check.log 2>&1
```
