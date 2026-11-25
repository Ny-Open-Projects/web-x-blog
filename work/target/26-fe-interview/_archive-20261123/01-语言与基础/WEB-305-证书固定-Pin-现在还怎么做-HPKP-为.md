---
title: [WEB-305] 证书固定（Pin）现在还怎么做？HPKP 为什么被废弃？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-305：证书固定（Pin）现在还怎么做？HPKP 为什么被废弃？
**答**：
- HPKP 允许站点声明固定公钥指纹，但攻击者可借 XSS 注入伪造 pin 永久锁死站点，浏览器已全部移除。
- 现在固定发生在 App 内：移动端网络库内置证书/公钥白名单，校验失败即断连，配 Chrome 的 Expect-CT/CT 日志辅助监督。
- Web 侧替代：依赖 CT（证书透明度）+ CA 运营监控；或上 mTLS/设备证书做应用层身份。

```javascript
// App 侧公钥固定示意
const pins = ['sha256/AAAA...=', 'sha256/BBBB...=']; // 当前 + 备用公钥
function verifyPin(cert) {
  const ok = pins.includes(cert.spkiSha256);
  if (!ok) throw new Error('TLS pinning 校验失败，中断请求');
}
// 注意：必须留备用 pin（备份域名/密钥），否则换证书=全体用户断网
console.log('固定要留逃生通道，HPKP 的教训');
```
