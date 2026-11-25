---
title: [WEB-190] 用户反馈"页面打不开"，给出一次完整的分层排查 SOP。
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-190：用户反馈"页面打不开"，给出一次完整的分层排查 SOP。
**答**：
- 按 DNS → TCP → TLS → HTTP → 渲染五层收敛，每层用一条命令拿到证据，避免上来就看业务代码。
- 先判断全量还是个别：换网络（手机热点）、换设备、换 DNS 快速二分，排除个人环境问题。
- 服务端视角补充：网关日志、监控大盘、最近发布记录——很多"打不开"其实是发布回滚造成的。
- 渲染层别漏：HTTP 200 但白屏，要看 JS 报错、关键资源 404、CSP 拦截记录。

```mermaid
flowchart TD
    A[用户反馈页面打不开] --> B{全量还是个别}
    B -->|个别| C[换网络换设备换 DNS<br/>二分定位个人环境]
    B -->|全量| D[DNS 层<br/>dig 看解析结果与 TTL]
    D --> E{解析正常}
    E -->|异常| F[DNS 故障或缓存未更新]
    E -->|正常| G[TCP 层<br/>nc 探测 443 端口]
    G --> H{端口可达}
    H -->|不通| I[服务器或防火墙故障]
    H -->|通| J[TLS 层<br/>openssl s_client 看证书与握手]
    J --> K{握手正常}
    K -->|异常| L[证书过期或链不完整]
    K -->|正常| M[HTTP 层<br/>curl 看状态码与首字节耗时]
    M --> N{状态码正确}
    N -->|异常| O[网关限流或后端 5xx]
    N -->|正常| P[渲染层<br/>看控制台报错与关键资源加载]
    P --> Q[JS 报错或资源 404 或 CSP 拦截]
```

```bash
# 每层一条命令拿证据
dig www.example.com +short                       # 1) DNS：有没有解析出 IP
nc -vz -w 3 www.example.com 443                  # 2) TCP：端口是否可达
openssl s_client -connect www.example.com:443 -servername www.example.com </dev/null 2>/dev/null | grep 'Verify return'
                                                 # 3) TLS：证书链校验结果
curl -sS -o /dev/null -w 'code=%{http_code} ttfb=%{time_starttransfer}\n' https://www.example.com
                                                 # 4) HTTP：状态码与首字节耗时
# 5) 渲染：DevTools 的 Console 与 Network，重点看 JS 异常与关键资源是否 404
```
