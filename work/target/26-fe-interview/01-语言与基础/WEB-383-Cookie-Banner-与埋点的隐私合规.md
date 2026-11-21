---
title: [WEB-383] Cookie Banner 与埋点的隐私合规，前端要做哪些事？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-383：Cookie Banner 与埋点的隐私合规，前端要做哪些事？
**答**：
- GDPR/个保法：非必要 Cookie（广告/分析）须用户明示同意后才写入；同意前不加载对应 SDK。
- 技术实现：脚本加载门控（consent 状态机）、必要/功能/统计/广告四类开关存储、撤回同意后清除对应 Cookie 与 storage。
- 埋点合规：脱敏（IP 截断、字段最小化）、隐私政策同步更新、数据出境评估；前端要能导出/删除用户数据（被遗忘权）。

```javascript
const consent = readConsent();   // { necessary: true, analytics: false }
function loadAnalytics() {
  if (!consent.analytics) return;              // 未同意不加载
  injectScript('//stats.com/a.js');
}
function withdraw() {
  clearCookies(['_ga', '_gid']); localStorage.removeItem('stats');
  saveConsent({ analytics: false });
}
console.log('同意前不注入、撤回后真清除');
```
