---
title: [WEB-073] OCSP 装订和证书透明度 CT 分别解决什么问题？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-073：OCSP 装订和证书透明度 CT 分别解决什么问题？
**答**：
- 证书吊销查询有两条路：CRL 是全量黑名单（大而慢）；OCSP 是实时单查，但浏览器直接查 CA 会泄露用户访问记录且增加握手延迟。
- OCSP 装订（Stapling）：由服务器定期去 CA 查询签名响应并缓存，TLS 握手时随证书一起"装订"下发，浏览器免查询、隐私不外泄。
- CT 证书透明度：所有 CA 签发的证书必须公开记录到 CT 日志，证书内嵌 SCT 签名时间戳；任何人可审计 CA 是否滥发证书，Chrome 要求公共证书有 SCT 才信任。
- 面试一句话：装订解决"吊销查询的隐私与延迟"，CT 解决"CA 乱发证书无法发现"。

```nginx
# nginx 开启 OCSP 装订
ssl_stapling on;
ssl_stapling_verify on;                 # 校验 OCSP 响应签名
ssl_trusted_certificate /etc/ssl/chain.pem;  # 用于验证装订响应的信任链
resolver 8.8.8.8 valid=300s;            # 装订查询需要 DNS 解析 OCSP 地址
# CT 无需服务端配置：CA 签发时已把 SCT 嵌入证书或 OCSP 响应
```

```bash
# 检查装订是否生效：看 OCSP response 字段是否非空
echo | openssl s_client -connect example.com:443 -status 2>/dev/null \
  | grep -A2 'OCSP response'

# 查看证书中的 CT 时间戳 SCT
echo | openssl s_client -connect example.com:443 2>/dev/null \
  | openssl x509 -noout -text | grep -A3 'CT Precertificate SCTs'
```
