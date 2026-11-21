---
title: [RBL-359] 构建平台的 API 与 Webhook 生态
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-359：构建平台的 API 与 Webhook 生态

**答**:
- API 面：构建触发/状态查询/产物下载/缓存管理——REST + 幂等设计（构建触发带 idempotencyKey 防重复触发）
- Webhook 事件：构建完成/失败/发布完成——下游消费（部署系统/通知 bot/质量平台）；事件 schema 版本化（消费者兼容）
- 生态扩展模式：平台不内置所有集成，提供事件+API 让团队自建（评论 bot/报表）——平台边界意识
- 安全：API token 权限分级（只读/触发/管理）、webhook 签名验证（防伪造事件）、限流

```text
API：trigger（幂等键）/ status / artifacts / cache
Webhook：build.done / build.failed / release.done（schema 版本化 + 签名验证）
模式：平台提供事件，团队自建集成
```
