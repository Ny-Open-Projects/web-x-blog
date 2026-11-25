---
title: [MP-267] 登录态与 UnionID：多端账户体系怎么打通？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-267：UnionID 多端账户体系？
**答**：
- 绑定开放平台后：小程序/公众号/App 登录都会返回 unionid（同一主体同一用户一致）。
- 账户模型：内部 user 表（userId 主键）+ oauth 表（openid/unionid/平台/绑定时间）——一个 user 可绑定多端凭证。
- 合并冲突：同手机号不同 unionid（先手机号后微信登录）——账号合并策略（保留主账号 + 关联表合并）与用户告知。
- 登录降级链：微信一键登录 → unionid 未取到（未绑定开放平台）→ 手机号验证码兜底注册。
- 安全：unionid 只在服务端流转，前端永远只见内部 token 与脱敏 user。
