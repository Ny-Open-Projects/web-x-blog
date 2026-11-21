---
title: [WEB-302] SNI 是什么？ECH 解决什么隐私问题？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-302：SNI 是什么？ECH 解决什么隐私问题？
**答**：
- 同一 IP 承载多站点时，服务器需要知道客户端要连哪个域名才能返回对应证书——这个域名明文放在 ClientHello 的 SNI 字段里。
- SNI 明文意味着中间设备可见访问目标域名，是审查/劫持的常用抓手；DNS 查询同样明文。
- ECH（Encrypted Client Hello）把真实 SNI 加密放进握手，外层只暴露一个公共"cover"域名；依赖 HTTPS DNS 记录提前分发公钥，目前 Chrome/Cloudflare 已支持。

```javascript
// ECH 示意：ClientHello 分 outer（公开）与 inner（加密）
const clientHello = {
  outerSNI: 'cloudflare-ech.com',      // 掩护域名
  encryptedInner: { realSNI: 'example.com', keyShare: '...' }, // ECH 公钥加密
};
// 中间人只能看到 outerSNI，看不到真实目标
console.log('TLS1.3 + DNS HTTPS 记录提供 ECH 公钥');
```
