---
title: [WEB-211] 什么是中间人攻击？HTTPS 下还有 MITM 风险吗？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-211：什么是中间人攻击？HTTPS 下还有 MITM 风险吗？

**答**：
- MITM：攻击者位于客户端与服务器之间，截获并可能篡改通信。典型手法：公共 Wi-Fi ARP 欺骗、DNS 劫持、伪造证书。
- 纯 HTTPS 理论上能防，但现实有旁路：企业代理/杀毒软件装了自定义根证书（合法 MITM）；用户手动信任恶意证书；HTTP 降级攻击（先剥离 HTTPS 再劫持）。
- 防御组合拳：HSTS 强制 HTTPS 并禁止用户忽略证书告警；证书固定（Certificate Pinning）只信任指定公钥；DNS 用 DoH 防劫持；关键接口再做应用层签名。
- 前端可做：检测 `window.crypto.subtle` 可用性、对比双通道数据一致性（重要操作二次校验）。

```javascript
// 服务端启用 HSTS（Nginx）
// add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
// 客户端检测是否被透明代理替换了证书链（示意）
fetch('https://api.example.com/health').then(res => {
  // 无法从 JS 读证书，通常由服务端比对客户端指纹/环境特征
  console.log(res.ok);
});
```
