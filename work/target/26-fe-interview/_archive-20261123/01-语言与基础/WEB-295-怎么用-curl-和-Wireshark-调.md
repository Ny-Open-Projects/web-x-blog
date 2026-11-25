---
title: [WEB-295] 怎么用 curl 和 Wireshark 调试 HTTP/3？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-295：怎么用 curl 和 Wireshark 调试 HTTP/3？
**答**：
- curl 快速验证：curl -v --http3-only https://host，观察 "Using HTTP/3" 与回退行为；支持 QUIC 的 curl 需较新版本。
- 抓包：QUIC 几乎全加密，Wireshark 直接看只见到包号与帧类型外壳；配置 TLS > (Pre)-Master-Secret log filename（SSLKEYLOGFILE）后可解密。
- Chrome 侧：chrome://net-export 导出日志用 netlog-viewer 分析，能看到协商的协议版本与 Alt-Svc 缓存。

```javascript
# 命令行实操
# 1) 强制走 h3（失败即报错，用来验证部署）
curl -sv --http3-only https://example.com -o /dev/null
# 2) 抓包解密
SSLKEYLOGFILE=./keys.log curl -sv --http3-only https://example.com -o /dev/null
# tshark 过滤 QUIC 并解密：
# tshark -r quic.pcap -o "tls.keylog_file:keys.log" -Y quic
console.log('验证 → 抓包解密 → netlog 三板斧');
```
