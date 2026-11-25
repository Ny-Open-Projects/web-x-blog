---
title: [WEB-537] 发现 XSS 注入后的应急响应 SOP
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-537：发现 XSS 注入后的应急响应 SOP

**答**：
- 止血第一：清除已注入的存储型 payload（内容库删除/下线相关接口）；短期可临时下线受影响功能，避免持续失血
- 影响面评估：注入点存活时长 × 页面 PV，估算可能受影响的用户；若有 token 窃取脚本，立即全局失效会话（踢所有用户重新登录）
- 修复分层：输出编码（业务层修复）→ CSP 兜底（即使漏了也执行不了外链脚本）→ 输入过滤只是辅助
- 取证与上报：保留 payload 样本与访问日志，安全事件按公司流程上报（国内监管有数据安全事件上报要求）
- 复盘输出：同类注入点的全站扫描（不只修一个点）、富文本白名单统一化、CSP 上线排期

```javascript
// 应急兜底：CSP 立即收紧 + 监控外联
// Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-xxx'; report-uri /csp
// 富文本输出统一走白名单 sanitizer，禁止直接 v-html/innerHTML
```
