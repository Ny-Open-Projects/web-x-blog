---
title: [WEB-419] TLS 指纹 JA3 是什么，为什么能识别爬虫
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-419：TLS 指纹 JA3 是什么，为什么能识别爬虫

**答**：
- JA3：把 ClientHello 里的 TLS 版本、CipherSuite 列表、扩展、椭圆曲线等拼起来哈希，得到一个指纹
- 原理：不同客户端（Chrome、curl、Python requests）的 ClientHello 参数组合不同，指纹就是「TLS 层的 UA」
- 反爬用途：脚本用 curl/httpx 请求时指纹与真实浏览器差异明显，服务端不比对 UA 而比对 JA3，伪装 UA 没用
- 前端关联：做合规数据采集或对接风控接口时，团队可能遇到「代码请求被拒、浏览器正常」的现象，原因常在 TLS 指纹
- 防御侧：自家 API 也可用 JA3 白名单拦截异常客户端，配合 WAF 使用

```bash
# 同一个目标：curl 与浏览器的 JA3 不同，可被服务端区分
curl -v https://target.example.com 2>&1 | grep -i "cipher\|extension" | head
# 服务端记录 ja3_hash 后可做策略：非浏览器指纹 → 验证码/拒绝
```
