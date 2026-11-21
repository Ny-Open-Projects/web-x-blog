---
title: [WEB-476] Fetch Metadata 请求头怎么用来做加固
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-476：Fetch Metadata 请求头怎么用来做加固

**答**：
- 浏览器现在自动带 Sec-Fetch-Site（same-site/cross-site/none）、Sec-Fetch-Mode（navigate/cors/no-cors）、Sec-Fetch-Dest（document/script/img…）
- 价值：服务端第一次能直接知道「这个请求是谁以什么方式发起的」，不用猜 Referer
- 典型加固规则：跨站来的 `Sec-Fetch-Site: cross-site` 且 Dest 是 document → 大概率 CSRF/嵌入攻击，拒绝；资源接口只接受 mode=cors 的站点请求
- 兜底防御：老浏览器没有这些头——策略上「没有头按跨站处理」或「没有头放行」要按业务风险选择
- 前端配合：自查自家跨域调用是否会被误杀（预检与正常请求都带头），CSP report-only 式灰度同样适用于此

```javascript
// 网关层规则示例
function fetchMetaGuard(req) {
  const { 'sec-fetch-site': site, 'sec-fetch-dest': dest } = req.headers;
  if (site === 'cross-site' && dest === 'document') return 403; // 防跨站直开
  if (site === 'same-site' || site === 'none') return null;     // 放行
  return null; // 无头（老浏览器）按需策略
}
```
