---
title: [OPS-036] upstream 负载均衡与健康检查怎么配？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-036：upstream 负载均衡与健康检查怎么配？
**答**：
- 开源 Nginx 只有被动健康检查（max_fails/fail_timeout）：连续失败 N 次在窗口期内摘除节点；主动探测需 Plus 版或第三方模块（upsync+consul 等）。
- 负载策略：默认轮询、weight 权重、ip_hash 会话保持、least_conn 最少连接；前端场景多为无状态，轮询+权重即可。
- keepalive 到上游能显著降低代理开销，但要配合 `proxy_http_version 1.1` 与空 Connection 头。
- 摘除节点只是被动止血，节点恢复检测、优雅上下线（先摘流量再停服务）应固化到发布脚本里。

```nginx
upstream web_pool {
    least_conn;                             # 最少连接，适合请求耗时差异大的场景
    server 10.0.1.11:8080 weight=5 max_fails=3 fail_timeout=15s;
    server 10.0.1.12:8080 weight=5 max_fails=3 fail_timeout=15s;
    server 10.0.1.13:8080 backup;           # 备节点：主力全挂才启用
    keepalive 64;

    # 优雅下线配合：发布前把目标节点标记 down 摘流量，等连接排空再停进程
    # server 10.0.1.14:8080 down;           # 临时摘除的节点示例
}

server {
    listen 80;
    server_name www.example.com;

    location / {
        proxy_pass http://web_pool;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
        proxy_next_upstream error timeout http_502 http_503 http_504;
        proxy_connect_timeout 2s;
    }

    # 主动探测的最简替代：本机 cron 定时打健康检查接口，
    # 连续失败则告警并通知值班（开源版无主动健康检查）
    location = /healthz {
        proxy_pass http://web_pool/status;
        access_log off;
    }
}
```
