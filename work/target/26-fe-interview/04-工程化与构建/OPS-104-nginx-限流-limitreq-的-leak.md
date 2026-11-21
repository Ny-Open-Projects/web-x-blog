---
title: [OPS-104] nginx 限流（limit_req）的 leaky bucket 参数怎么调？burst 与 nodelay 的取舍是什么？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-104：nginx 限流（limit_req）的 leaky bucket 参数怎么调？burst 与 nodelay 的取舍是什么？
**答**：
- rate=10r/s 表示恒定速率放行，超出按漏桶排队；burst 是队列容量，默认排队会拉高延迟，加 nodelay 后 burst 名额立即放行、超了直接 429。
- 普通用户接口：burst 取 1-2 倍正常峰值并发 + nodelay，宁可 429 让前端重试，也不排队拖慢所有人。
- 无 nodelay 的排队模式只适合"允许慢但别拒绝"的场景（如导出）。
- limit_conn 与 limit_req 叠加：连接数限单 IP 长连接占用，请求速率限突发；两个 zone 的内存按 16 万 IP/10M 估算。
- 压测确定阈值而不是拍脑袋：把正常用户 P99 的请求速率乘安全系数作为 rate，429 率放灰度期观察（OPS-149 防刷与这里共用一套口径）。

```nginx
http {
    # 漏桶：10r/s，10M 内存约可跟踪 16 万个 IP
    limit_req_zone  $binary_remote_addr  zone=api_limit:10m   rate=10r/s;
    limit_conn_zone $binary_remote_addr  zone=conn_limit:10m;
    limit_req_status  429;      # 用 429 而非默认 503，语义正确且便于前端识别重试
    limit_conn_status 429;

    server {
        location /api/ {
            # burst=20 允许 20 个瞬时突发；nodelay 不排队立即放行，桶空即 429
            # 取舍：无 nodelay 会把突发请求排队造成延迟抖动，接口场景基本都用 nodelay
            limit_req  zone=api_limit   burst=20 nodelay;
            limit_conn conn_limit 10;         # 单 IP 最大并发连接

            proxy_pass http://app_backend;
        }

        # 页面级宽松档：防脚本刷页面但不伤真实用户
        location / {
            limit_req zone=api_limit burst=100 nodelay;
            try_files $uri /index.html;
        }
    }
}
```
