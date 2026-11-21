---
title: [WEB-533] CORS 与 SameSite 联合导致 Cookie 不带的排查
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-533：CORS 与 SameSite 联合导致 Cookie 不带的排查

**答**：
- 跨域请求要带 Cookie 需同时满足四条：前端 `credentials: 'include'`、服务端 `Access-Control-Allow-Credentials: true`、`Allow-Origin` 为具体 origin（不能 *）、Cookie 自身 `SameSite=None; Secure`
- 少任何一条的表现不同：前两条缺失浏览器报 CORS 错；SameSite 不满足则「请求成功但 Cookie 静默不带」——最难排查的一类
- 排查三板斧：Network 面板看请求 Cookie 列（灰色标注被 SameSite 排除的 cookie）→ Application 面板核对 Cookie 属性 → 检查站点是否跨站（site 计算规则：eTLD+1）
- 陷阱：localhost 与 127.0.0.1 互为跨站；子域之间是同站；port 不参与 site 判断
- 面试话术：先背四条铁律，再讲「静默不带」与「CORS 报错」的症状区分，排查条理立刻清晰

```javascript
fetch('https://api.example.com/x', { credentials: 'include' }); // 缺这条 = Cookie 永远不带
```
