---
title: [WEB-213] 证书固定（Certificate Pinning）怎么做？风险是什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-213：证书固定（Certificate Pinning）怎么做？风险是什么？

**答**：
- 含义：客户端只信任预设的公钥/证书，即使攻击者持有一张合法 CA 签发的证书（CA 被入侵、员工误签）也无法中间人。
- 浏览器端：HPKP 已废弃（误配导致站点永久锁死），现用 Expect-CT 或直接内嵌在 App 里做。
- App/客户端：把服务端公钥 SPKI 的 hash 打包内置，握手时比对证书链中任意一层的 SPKI hash。
- 风险与最佳实践：固定备用公钥（backup pin），防止主密钥泄漏或换证书后 App 集体失联；证书轮换要提前发布新版本；Web 端固定太死会阻塞 CDN 换签。

```javascript
// Node 客户端固定公钥示意
const crypto = require('crypto');
const PIN = 'sha256/XXXXXXXXbase64spkihashYYYYY=';
const tls = require('tls');
const socket = tls.connect(443, 'api.example.com', () => {
  const cert = socket.getPeerCertificate();
  const spki = cert.pubkey;
  const hash = crypto.createHash('sha256').update(spki).digest('base64');
  if (`sha256/${hash}` !== PIN) socket.destroy(); // 拒绝非预期公钥
});
```

**评分点**：
- 能说出 HPKP 已废弃及原因（误锁风险）
- 明确「固定的是公钥不是域名」
- 必须提备用 pin 与轮换策略
- 能区分 App 端 pinning 与 Web 端手段差异
