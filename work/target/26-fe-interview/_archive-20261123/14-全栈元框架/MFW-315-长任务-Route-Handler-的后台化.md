---
title: [MFW-315] 长任务 Route Handler 的后台化（队列 + 轮询协议）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-315：长任务后台化

**答**:
- 问题：导出/报表类请求超时预算（Serverless 10-30s）——同步等待必死
- 协议：POST 提交 → 返回 taskId（202）→ 任务进队列（轻量：DB 表 + worker 拉取；重：SQS 类）→ 客户端轮询 GET /status/:id（或 SSE 推进度）→ 完成取产物（签名 URL 下载）
- 可靠性三件：任务幂等键（重复提交同 key 复用进行中任务）、进度持久化（百分比 + 阶段——轮询有内容可看）、死信与清理（超 24h 归档，产物过期删除）
- Serverless 特有：worker 用独立部署形态（常驻 Node 或队列触发函数——与 Web 层资源隔离，重活不挤页面渲染）

```text
协议：202 + taskId → 队列 → 轮询/SSE 进度 → 签名 URL 产物
三件：幂等键复用 / 进度持久化 / 死信清理
隔离：worker 独立于 Web 层（资源不互挤）
```
