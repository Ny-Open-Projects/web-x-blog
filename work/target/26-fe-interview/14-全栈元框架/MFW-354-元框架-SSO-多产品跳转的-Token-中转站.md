---
title: [MFW-354→MFW-354] SSO 多产品跳转的 Token 中转站设计
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW→354：Token 中转站

**答**:
- 问题：跨产品域（非同父域）不能共享 cookie——每个目标域需要独立会话；用户逐个登录体验崩坏
- 中转站协议：中心 IdP 签发一次性交换码（10s TTL 单次消费）→ 跳转目标域 `?code=...` → 目标域后端用 code+client_secret 向 IdP 换正式会话 → 302 回业务页清参数——OAuth Codeswap 精简版用于内部多产品
- 安全细节：code 单次消费（重放拒绝——重放即攻击信号告警）、state 绑定发起会话、目标域白名单（开放重定向面收敛到注册表）
- 登出联动：中心登出 → 各产品 back-channel 注销（服务端间调用清各自 refresh 链——前端清不干净的由服务端版本号兜底）

```text
协议：IdP 一次性 code(10s) → 目标域后端 codeswap → 建域内会话 → 清参数
安全：code 单次+state 绑定+域白名单；登出走 back-channel 全家清
```
