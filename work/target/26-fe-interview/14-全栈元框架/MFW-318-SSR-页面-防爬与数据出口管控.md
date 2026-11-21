---
title: [MFW-318] SSR 数据出口管控（防爬与字段最小化）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-318：SSR 数据出口管控

**答**:
- 泄露面：RSC payload 是「公开的 JSON」（查看源码即见）——server 查了什么字段用户就能看到什么；权限裁剪必须在查询层（select 白名单）而非渲染层隐藏
- 防爬组合：速率（IP/无 cookie 会话——MFW-294）+ 成本抬升（分页深度限制/每页条数上限）+ 高频访问模式标记 + sitemap 引导合法爬虫、限流恶意部分
- 字段出口审计：统计「各路由 payload 暴露字段集」——新字段进 payload 走评审（数据出口 = API 设计同等严肃）
- 判定句：RSC 查询就是 API 响应构造——用 API 安全标准审计它（越权/过取/枚举）

```javascript
prisma.user.findMany({ select: { id: true, name: true } })   // salary 永不进查询
// payload 字段集审计：route→fields 清单，新增字段 → PR 评审标签
```
