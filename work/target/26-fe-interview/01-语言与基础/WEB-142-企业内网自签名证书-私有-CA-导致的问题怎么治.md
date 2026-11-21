---
title: [WEB-142] 企业内网自签名证书/私有 CA 导致的问题怎么治理？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-142：企业内网自签名证书/私有 CA 导致的问题怎么治理？
**答**：
- 内网域名用企业 CA 签发，客户端必须把企业根证书装入信任域，否则全站红色警告。
- 各运行时信任源不同：浏览器读系统钥匙串；Node 自带 CA 列表，需 NODE_EXTRA_CA_CERTS 追加企业根。
- 治理方案：IT 通过 MDM 统一分发根证书；开发者本地用 NODE_EXTRA_CA_CERTS 指向企业 CA，而不是关校验。
- 联调排查三板斧：openssl s_client 看校验返回码；确认证书链是否完整（少发中间证书是高发事故）；区分"证书过期"与"链不完整"。

```bash
# 1) 查看内网服务返回的证书链与校验结果
openssl s_client -connect git.corp.example.com:443 -servername git.corp.example.com </dev/null 2>/dev/null \
  | grep -E 'verify return|Verify return code'
# 2) 把企业根证书追加给 Node（不要关掉校验）
export NODE_EXTRA_CA_CERTS=/usr/local/share/certs/corp-root.pem
node -e "require('https').get('https://git.corp.example.com', r => console.log(r.statusCode))"
# 3) 个人开发场景用 mkcert 生成本地信任的开发证书
mkcert -install && mkcert dev.local
```

## 二十四、身份认证专题
