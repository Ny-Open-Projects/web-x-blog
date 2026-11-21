---
title: [WEB-451] CSP 的 report-only 模式怎么用，怎么灰度
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-451：CSP 的 report-only 模式怎么用，怎么灰度

**答**：
- `Content-Security-Policy-Report-Only`：只上报违规不拦截，用于上线前摸底「我的页面到底会违反哪些策略」
- 灰度流程：Report-Only 观察两周 → 违规清单清理（内联脚本、第三方 SDK 的 eval）→ 切正式 CSP → 持续保留 report-uri 监听新违规
- 上报方式：`report-uri`（老）或 `report-to`（新），配 Reporting API；自己收口到监控平台按 directive 聚合
- 常见误杀：第三方 SDK 动态插 script、JSONP 内联、老代码的 eval——这些都要进 nonce/hash 或改造
- 面试话术：能讲「先观测再拦截、按违规量排序治理」的节奏感比背指令更值钱

```http
Content-Security-Policy-Report-Only: default-src 'self'; report-uri /csp-report;
```
```javascript
// 服务端聚合上报
app.post('/csp-report', express.json({ type: 'application/csp-report' }), (req, res) => {
  const r = req.body['csp-report'];
  metrics.incr(`csp:${r['violated-directive']}:${r['blocked-uri'] || 'inline'}`);
  res.status(204).end();
});
```
