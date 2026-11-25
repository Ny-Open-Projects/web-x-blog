---
title: [R19-216] Action 里遇到耗时任务（生成报表）怎么办？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-216：Action 里遇到耗时任务（生成报表）怎么办？
**答**：
- 原则：Action 响应时间应秒级内；超长任务异步化——action 只「创建任务」入队（DB/消息队列），立即返回 taskId。
- 前端拿到 taskId 后轮询（useEffect + interval）或走 SSE/WebSocket 订阅进度；完成后跳转下载链接。
- Serverless 环境注意：action 执行有超时上限（Vercel 函数 10s~ 数分钟按套餐），别在 action 里 await 长任务。
- 任务失败处理：状态机 pending/running/done/failed，前端轮询到 failed 展示原因并支持重试。
- 备选：Server-Sent Events 流式返回进度（action 内 yield 进度）适合「前端等待 + 进度可见」的中等时长任务。
