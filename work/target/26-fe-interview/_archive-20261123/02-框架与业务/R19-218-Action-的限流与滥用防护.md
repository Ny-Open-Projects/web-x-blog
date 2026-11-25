---
title: [R19-218] Server Action 怎么做限流与滥用防护？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-218：Server Action 怎么做限流与滥用防护？
**答**：
- Action 本质是公开的 HTTP 端点（POST + 加密 id），可被脚本直接调用——按公开 API 的标准做防护。
- 限流：按 userId/IP 令牌桶（内存 Map 仅单实例可用，生产用 Redis/Upstash ratelimit）。
- 验证码/风控：注册、评论、下单等高风险 action 接入人机校验（Turnstile/hCaptcha）。
- 输入防御：zod 严格校验（长度/枚举），数据库层参数化防注入，文件上传白名单 MIME + 魔数检测。
- 监控：action 调用频率异常告警（同 user 秒级高频 → 自动封禁冷却）。
