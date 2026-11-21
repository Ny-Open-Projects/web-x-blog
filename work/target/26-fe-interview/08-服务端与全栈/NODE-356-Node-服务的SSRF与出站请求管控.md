---
title: [NODE-356] Node 服务的 SSRF 防护与出站请求管控如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-356：SSRF 防护与出站请求管控
**答**:
- SSRF 场景：服务端按用户提供的 URL 发请求（网页预览/导入远程文件/webhook 回调）——攻击者用它探测内网（169.254.169.254 云元数据、localhost 管理端口）。
- 防线：URL 校验（协议白名单 http/https、禁 IP 直连与内网段 CIDR 黑名单：127/8、10/8、169.254/16、169.254.169.254）、DNS 解析后校验 IP（防 DNS rebinding：域名指向内网 IP）、重定向逐跳复检（fetch 默认跟随，需手动禁用后逐跳校验）、响应大小与超时限制。
- 网络层兜底：出站请求走代理网关（egress proxy），Pod 网络策略禁止业务容器直连元数据地址；不同信任级别出站分离。
- webhook 场景：回调地址注册时校验（白名单域 + HTTPS + 签名验证响应），运行时再校验。
- 检测：出站请求日志（目标地址分布异常告警：突然出现内网 IP 调用）。
```javascript
const net = require('net');
const BLOCKED = ['127.0.0.0/8', '10.0.0.0/8', '169.254.0.0/16', '172.16.0.0/12', '192.168.0.0/16'];
async function safeFetch(userUrl) {
  const u = new URL(userUrl);
  if (!/^https?:$/.test(u.protocol)) throw new Error('协议不允许');
  const { address } = await dns.promises.lookup(u.hostname);     // 解析后校验防 rebinding
  if (BLOCKED.some(cidr => ipInCidr(address, cidr))) throw new Error('目标地址不允许');
  return fetch(userUrl, { redirect: 'manual' });                 // 手动逐跳复检
}
```
