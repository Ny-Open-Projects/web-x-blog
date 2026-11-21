---
title: [OPS-034] Nginx 黑白名单 allow/deny 怎么用？和防火墙如何配合？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-034：Nginx 黑白名单 allow/deny 怎么用？和防火墙如何配合？
**答**：
- allow/deny 基于 IP/CIDR，按顺序匹配，适用管理后台限内网、接口只允许网关层访问等场景。
- 与认证组合（satisfy all）：既要 IP 白名单又要 Basic Auth/SSO 网关，双重校验。
- 大规模动态封禁（防刷）不建议写 Nginx 配置（reload 频繁），用 geo 模块加载外部文件或上 WAF/防火墙层。
- 注意真实 IP 问题：前面有 CDN/LB 时 remote_addr 是代理 IP，必须先用 realip 模块从 X-Forwarded-For 还原，否则黑白名单全部失效。

```nginx
# 真实 IP 还原：有 CDN/LB 时必须先做，否则 allow/deny 基于 CDN 节点 IP 全部失真
set_real_ip_from 10.0.0.0/8;          # 信任的代理层网段（CDN 回源段）
real_ip_header X-Forwarded-For;
real_ip_recursive on;

# 管理后台：仅办公网与运维 VPN 可访问
location /admin/ {
    allow 192.168.0.0/16;    # 办公网
    allow 10.8.0.0/24;       # 运维 VPN
    allow 203.0.113.7;       # 驻场外包固定出口
    deny  all;

    alias /data/web/current/admin/;
    try_files $uri $uri/ /admin/index.html;
}

# 内部元数据接口：IP 白名单 + Basic Auth 双重校验
location /internal/meta {
    satisfy all;
    allow 10.0.0.0/8;
    deny  all;
    auth_basic           "restricted";
    auth_basic_user_file /etc/nginx/.htpasswd;
    proxy_pass http://api_backend;
}
```
