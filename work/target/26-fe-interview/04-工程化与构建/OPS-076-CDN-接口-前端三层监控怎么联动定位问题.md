---
title: [OPS-076] CDN、接口、前端三层监控怎么联动定位问题？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-076：CDN、接口、前端三层监控怎么联动定位问题？
**答**：
- 分层告警先定位层：拨测失败（CDN/入口层）→ 接口错误率（API 层）→ JS 错误/白屏（前端层），层间用 req_id/trace 串联。
- 典型联动场景：JS 错误突增 → 查错误样本里的资源 URL 与 CDN 状态 → 发现某边缘节点返回被篡改/旧资源 → 结合 CDN 命中率与回源日志锁定范围。
- 统一时间轴：三层监控数据进同一个 Grafana，故障时同一时间轴对齐看，快速分辨"先后关系还是因果"。
- 演练：每季度做一次"注入故障→观察三层告警是否按预期触发与排序"。

```bash
#!/usr/bin/env bash
# triage_layers.sh：三层联动排查脚本——输入时间窗，输出各层证据
set -euo pipefail
FROM=${1:?usage: triage_layers.sh <from_ts> [to_ts]}
TO=${2:-$(date +%s)}

echo "===== 第 1 层：CDN/入口（拨测与边缘状态） ====="
grep -h "dial" /var/log/dialtest.log | awk -v f="$FROM" -v t="$TO" \
  '$1 >= f && $1 <= t && /FAIL/' | tail -5
# 各边缘节点状态抽样
for edge in cdn-a cdn-b cdn-c; do
  code=$(curl -s -o /dev/null -w '%{http_code}' --resolve \
    www.example.com:443:"$(dig +short $edge.example.com | head -1)" \
    https://www.example.com/healthz || echo ERR)
  echo "edge=$edge healthz=$code"
done

echo "===== 第 2 层：API（错误率与上游） ====="
awk -v f="$FROM" -v t="$TO" '
  $0 ~ /"log_type":"nginx_access"/ {
    match($0, /"status":[0-9]+/); s=substr($0,RSTART+10,RLENGTH-10);
    if (s >= 500) e++
    n++
  }
  END { printf "api 请求=%d 5xx=%d 比例=%.2f%%\n", n, e, (n?e/n*100:0) }' \
  /var/log/nginx/access.json

echo "===== 第 3 层：前端（JS 错误与白屏上报） ====="
awk -v f="$FROM" -v t="$TO" '
  /fe_error_total/ { print }' /var/log/fe-errors.log | tail -5
# 用 req_id 串联：取一条 5xx 的 req_id，查前端是否上报了对应错误
RID=$(awk -v f="$FROM" -v t="$TO" 'match($0,/"status":5/) && match($0,/"req_id":"[^"]+"/) {
  print substr($0,RSTART+10,RLENGTH-11); exit}' /var/log/nginx/access.json)
echo "样例 req_id=$RID（拿去 Sentry/日志平台全局搜索，可同时看到接口 5xx 与前端报错）"
```

---

## 九、sourcemap 与错误定位（OPS-077 ~ OPS-082）

sourcemap 是"压缩后报错"到"源码行号"的翻译器。运维视角的核心策略：产物不放 map（安全+体积），map 走专用通道上传监控平台，用 release 关联版本，泄漏面收敛到零。
