---
title: 低代码平台的权限模型与多端差异化鉴权
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 概念, 权限, 鉴权, JWT]
---

## 低代码平台的权限模型与多端差异化鉴权

权限公式：**角色 × 资源 × 操作 = RBAC 基础**。低代码平台的三端天然差异化：编辑端需登录（token→用户）、发布页免登录（凭 pageId 取数、接口不含敏感数据）、统计端登录 + 数据权限。

**本项目实例**：
- 编辑端与统计端：JWT 全链路——passport-jwt Strategy 校验 Bearer token，`JwtAuthGuard` 以 APP_GUARD 全局注册，默认拦截一切接口，`@Public()` 显式豁免，杜绝新接口忘加守卫；validate 里二次查库并抹除 password。
- 发布页：`/low_code/release?id=` 公开访问；问卷防重复提交不靠登录，靠 MD5(ip+User-Agent) 匿名标识（单机直连有效，反代需 trust proxy + XFF）。
- 数据归属：page/component/resources 三表带 account_id（component_data 经 page_id 挂页面归属）。自研参考实现 A 的 tenantId 是「预留 + 头级过滤（读路径）」，写路径（改/删）漏了校验——如实当案例讲；课程原版 B 无角色模型，别写成 RBAC。

工程要求：统一 Guard 层鉴权，不在 Controller 散写 if；前端路由守卫 + 接口 Guard 双重拦截（前端藏按钮，接口不能裸奔）。

注意边界：两套代码工程都没有真正的 RBAC 角色模型，博客表述别夸大。

出处「课程25 · 14-3、20-3；scan3 §6」
