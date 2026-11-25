---
title: [WEB-377] 子域名劫持（Dangling DNS）是什么？前端怎么发现和防？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-377：子域名劫持（Dangling DNS）是什么？前端怎么发现和防？
**答**：
- 域名 CNAME 指向的第三方服务已释放（下线的 Heroku/gh-pages），攻击者认领该服务就能接管域名——拿到的是整个子域，可发 Cookie、劫持 JS。
- 前端视角：第三方 SDK 挂了不再用却留着 DNS 指向、营销活动子域下线不清 DNS，都是高危残留。
- 防法：子域下线即清 DNS 记录、用自家 CNAME 收敛到可控域、监控 dangling CNAME（定期解析+探测）。

```javascript
// 探测: dig test.old-campaign.com CNAME → herokuapp.com
async function audit(sub, expectService) {
  const cname = await dnsResolve(sub);
  if (cname && !await alive(cname)) {
    return '高危：CNAME 指向已释放服务 → 立即删 DNS 记录';
  }
  return 'ok';
}
console.log('接管后可对同父域发 Cookie，比 XSS 还彻底');
```
