---
title: [R19-223] 发版期间旧页面调新 Action 会发生什么？怎么兼容？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-223：发版期间旧页面调新 Action 会错配吗？怎么兼容？
**答**：
- Server Action 的 id 与实现版本绑定：旧 HTML 里的 action id 在新构建后可能不存在 → 报 "Failed to find Server Action"，用户提交失败。
- 缓解一：action 参数与返回结构只加不减（向后兼容），旧 id 的 action 保留一个版本周期再删。
- 缓解二：失败兜底——客户端捕获 action 调用错误后整页刷新（拿最新 HTML），重试提交。
- 发布策略：错峰发布 + 表单页 TTL 短（减少旧页面存活时间），大改版走新路径而非改旧接口。
- 监控：上报 action not found 错误率，作为发版健康指标。
