---
title: [MFW-378→MFW-378] 双 CSP 策略（静态站与动态路由的差异头）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-378：双 CSP

**答**:
- 分歧根源：静态营销页（零内联、固定域）可上最严 CSP（script-src 'self' + 固定指纹 nonce）；动态应用页（第三方支付 SDK/JSONP 遗留）域名单长——一张头强制全站会导致「全站 unsafe-inline」自废武功
- 协议：CSP 按路由族下发（中间件/边缘函数按前缀选择策略——策略即代码进版本库可测：RBL-313 构建期 hash 提取复用）；严格页违规 = fail（report-only 结束后强制），宽松页只 report 持续收敛
- nonce 生命周期：每请求新 nonce（模板注入点统一——手写散落 nonce 是绕过口）；静态页用 hash 列表（无请求态依赖，CDN 可缓存带头页面）
- 验证闭环：csp-watch 拨测（各路由族拉响应头比对策略表——发布漂移即告警 RBL-318 对账思路）

```text
双策：静态族='self'+hash（最严可缓存） | 动态族=白名单域+nonce（report-only 收敛中）
实现：策略即代码按路由族下发；nonce 请求级统一注入点
验证：csp-watch 比对策略表，漂移即告警
```
