---
title: [OPS-072] 前端日志采集链路怎么搭（nginx 日志/埋点/错误汇聚）？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-072：前端日志采集链路怎么搭（nginx 日志/埋点/错误汇聚）？
**答**：
- 三条日志流：nginx access/error（服务端视角）、前端埋点（用户行为+性能+自定义事件）、前端错误（Sentry 等错误汇聚平台）。
- 链路：Nginx JSON 日志 → filebeat/vector 采集 → Kafka 缓冲 → Loki/ES 存储 → Grafana/Kibana 查询；埋点走 sendBeacon 上报 → 网关 → 消息队列 → 数仓。
- 日志规范统一：req_id 贯穿（前端生成的 request id 同时进 nginx 日志与错误上报），一次问题可串联三层日志。
- 成本治理：采样、字段白名单、冷热分层存储，避免日志成本失控。

```yaml
# filebeat.yml：nginx JSON 日志采集配置
filebeat.inputs:
  - type: filestream
    id: nginx-access
    paths:
      - /var/log/nginx/access.json
    parsers:
      - ndjson: {}                    # 直接解析 JSON 行
    fields: { log_type: nginx_access, service: web-mall }
    fields_under_root: true

  - type: filestream
    id: fe-behavior                   # 前端埋点落盘的日志（网关侧）
    paths:
      - /var/log/nginx/report.log
    fields: { log_type: fe_behavior, service: web-mall }

output.kafka:
  hosts: ["kafka1.internal:9092", "kafka2.internal:9092"]
  topic: "fe-logs-%{[log_type]}"
  required_acks: 1
  compression: gzip
  max_message_bytes: 1000012

processors:
  - add_host_metadata: ~
  - drop_fields:                     # 字段白名单治理，降低存储成本
      fields: ["agent.ephemeral_id", "log.offset", "input.*"]
      ignore_missing: true
```
