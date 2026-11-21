---
title: [OPT-055] OCSP stapling 对首屏有什么影响？怎么验证它生效了？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-055：OCSP stapling 对首屏有什么影响？怎么验证它生效了？

**答**：
- 默认情况下浏览器要向 CA 的 OCSP 服务器发请求确认证书是否吊销，这是一次**关键路径外的额外 RTT**，且 OCSP 服务器慢/被墙时直接卡住建连。
- Stapling 让服务端定期向 CA 查询并缓存签名结果，握手时随证书一起"钉"给客户端，浏览器免掉这次外呼。
- 收益在无缓存的首次建连最明显（尤其海外 CA 场景可省 200ms-1s）；配合 TLS 1.3 stapling 还能进 0-RTT。
- 注意 stapling 响应有效期约 7 天，CA 查询失败会导致断续失效，必须配监控与 resolver 缓存。

```bash
# 一一对应：验证 OCSP stapling 是否生效与命中延迟的排查命令
# 1. 查看 stapled 响应是否存在
openssl s_client -connect example.com:443 -status </dev/null 2>/dev/null \
  | grep -A3 'OCSP response'
# 期望输出 "OCSP Response Status: successful"；
# 若是 "no response sent" 说明 stapling 没生效，浏览器将自行外呼 OCSP 服务器

# 2. 确认证书链是否多余（链每多一级，握手多传一段）
openssl s_client -connect example.com:443 -showcerts </dev/null 2>/dev/null \
  | grep -c 'BEGIN CERTIFICATE'
# 叶子+1~2 级中间证书为最佳；把根证书也配进去属于常见错误（根浏览器必有，纯浪费）

# 3. 实测建连耗时对比：TCP+TLS 总时长
curl -o /dev/null -s -w 'dns=%{time_namelookup} tcp=%{time_connect} tls=%{time_appconnect}\n' \
  https://example.com
# time_appconnect - time_connect 即 TLS 握手耗时，stapling 正常时稳定在 1-RTT 内；
# 若波动大且伴随 OCSP 域名解析，说明 stapling 失效退化为浏览器侧查询
```

## 十一、JS 执行优化
