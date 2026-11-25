---
title: [PER-1002] 数据出境与本地化：前端 SDK 的区域路由怎么做
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1002：数据出境与本地化：前端 SDK 的区域路由怎么做

**答**：
- 问题：跨国业务下 EU 用户数据出欧违反 GDPR；SDK 统一上报到全球端点即违规。
- 方案：按用户区域路由上报域名（EU 端点/中国端点/其他），IP 判定在网关层 + Accept-Language/TZ 辅助；区域数据不互迁。
- 工程：SDK 配置携带 region，上报网关按区域隔离存储；跨区域分析用聚合后匿名统计。
- 验证：定期审计上报目标域与数据落地区域一致性，输出合规报告。

```javascript
// 区域路由 SDK
const REGIONS = { eu: 'eu.col.example.com', cn: 'cn.col.example.com',
  default: 'col.example.com' };
function pickRegion(user) {
  if (user.region) return user.region;                       // 账号区域优先
  if (Intl.DateTimeFormat().resolvedOptions().timeZone?.includes('Europe'))
    return 'eu';
  return 'default';
}
function endpoint() { return `https://${REGIONS[pickRegion(currentUser)]}/rum`; }
// SDK 初始化时锁定 endpoint，运行期不再改变，避免数据跨区
```
