---
title: [WEB-359] CSP 上线为什么要先跑 Report-Only？流程怎么走？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-359：CSP 上线为什么要先跑 Report-Only？流程怎么走？
**答**：
- Content-Security-Policy-Report-Only 只上报违规不拦截，先观察真实流量里哪些合法资源会被误伤。
- 流程：Report-Only 收集 1-2 周 → 按报告补白名单（域名/nonce）→ 切正式策略仍保留 report-uri → 发现新违规及时修。
- 注意：第三方脚本内部 eval、动态注入都会违规，白名单要么收编要么联系供应商，别轻易开 unsafe-eval。

```javascript
// 第一阶段
// Content-Security-Policy-Report-Only: default-src 'self'; report-uri /csp-report
// 第二阶段（同策略去掉 Report-Only 前缀）
const report = { blockedURI: 'https://stats.com/a.js', directive: 'script-src' };
function fix(report) {
  if (report.blockedURI.includes('stats.com')) return '白名单加 stats.com 或换供应商';
}
console.log(fix(report));
```
