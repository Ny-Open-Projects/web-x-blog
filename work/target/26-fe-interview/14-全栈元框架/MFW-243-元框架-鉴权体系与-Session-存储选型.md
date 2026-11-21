---
title: [MFW-243] 元框架鉴权体系与 Session 存储选型
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## MFW-243：鉴权与 Session 存储选型

**答**:
- 三种 session 形态：无状态 JWT（cookie 携带——边缘友好/本地校验零查询，但吊销难）、有状态 session 表（每次校验查库/Redis——可吊销但每请求一查询）、混合（短 JWT + 服务端版本号校验——吊销粒度与成本平衡）
- 元框架落位：Middleware 放「本地可判」的校验（JWT 签名/过期——毫秒级），RSC/Action 内放「需查询」的授权（角色/资源级）——两层各司其职
- 吊销设计：JWT 加 tokenVersion（用户登出全端 +1）→ Middleware 只验签名，RSC 层比对版本（Redis 一查 O(1)）
- 安全底线：httpOnly+Secure+SameSite、CSRF 对 Action 由框架 origin 校验兜底、Handler 需自建 CSRF 防护（MFW-236）

```text
选型表：JWT（边缘快/吊销弱）/ Session 表（可吊销/每请求查）/ 混合（版本号吊销） 
落位：Middleware=本地签名校验，RSC/Action=资源级授权查询
```
