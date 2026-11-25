---
title: [OPS-039] Nginx 日志怎么配置？线上日志如何切割与治理？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-039：Nginx 日志怎么配置？线上日志如何切割与治理？
**答**：
- 日志先规划用途：排错日志（全量、含耗时与上游）、埋点日志（自定义 log_format 输出 JSON 供采集）、监控日志（关键字段精简）。
- 自定义 log_format 是前端运维的基本功：把 request_time、upstream_response_time、upstream_addr、版本号写进日志，排查问题效率翻倍。
- 切割用 logrotate（copytruncate 或 USR1 信号），按天切割保留 N 天，压缩归档。
- 大流量站点 access_log 开 buffer 与按级别关闭（静态资源 access_log off）降低 IO 开销。

```nginx
# log_format：结构化 JSON，直接喂给 filebeat/loki
log_format json_combined escape=json '{'
    '"time":"$time_iso8601",'
    '"remote_addr":"$remote_addr",'
    '"request":"$request",'
    '"status":$status,'
    '"body_bytes":$body_bytes_sent,'
    '"request_time":$request_time,'
    '"upstream_time":"$upstream_response_time",'
    '"upstream_addr":"$upstream_addr",'
    '"referer":"$http_referer",'
    '"ua":"$http_user_agent",'
    '"req_id":"$request_id"'
'}';

server {
    listen 80;
    server_name www.example.com;

    access_log /var/log/nginx/access.json json_combined buffer=64k flush=1s;
    error_log  /var/log/nginx/error.log warn;

    location /assets/ {
        access_log off;               # 静态资源不打访问日志，省 IO
        expires 30d;
    }
}
```

```bash
# /etc/logrotate.d/nginx：按天切割，保留 30 天，配合 USR1 无缝切换
/var/log/nginx/*.log {
    daily
    rotate 30
    missingok
    notifempty
    compress
    delaycompress        # 昨天的日志隔天再压缩，避免句柄问题
    dateext
    sharedscripts
    postrotate
        [ -f /var/run/nginx.pid ] && kill -USR1 $(cat /var/run/nginx.pid)
    endscript
}
```
