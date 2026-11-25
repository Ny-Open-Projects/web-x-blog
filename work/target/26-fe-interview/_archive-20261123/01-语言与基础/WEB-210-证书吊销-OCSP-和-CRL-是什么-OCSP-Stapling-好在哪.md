---
title: [WEB-210] 证书吊销 OCSP 和 CRL 是什么？OCSP Stapling 好在哪？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-210：证书吊销 OCSP 和 CRL 是什么？OCSP Stapling 好在哪？

**答**：
- CRL：证书吊销列表，CA 定期发布的全量吊销名单，体积大、时效差。
- OCSP：在线查询单张证书状态的协议，实时性好，但浏览器直接查 CA 会带来两个问题——隐私泄露（CA 知道你访问了谁）与额外 RTT（握手变慢），查询失败时很多浏览器选择「软失败」放行，吊销形同虚设。
- OCSP Stapling：服务器定期自己去 CA 查好签名结果，握手时随证书一起「钉」给浏览器。浏览器免了额外查询，隐私和延迟问题同时解决。
- 现代替代：Let's Encrypt 等推行短有效期证书（如 6 天），吊销需求大幅降低。

```bash
# Nginx 开启 OCSP Stapling
ssl_stapling on;
ssl_stapling_verify on;
resolver 8.8.8.8 valid=300s;

# 验证 stapling 是否生效
openssl s_client -connect example.com:443 -status </dev/null 2>/dev/null \
  | grep -A3 'OCSP response'
# 期望输出: OCSP Response Status: successful (0x0)
```
