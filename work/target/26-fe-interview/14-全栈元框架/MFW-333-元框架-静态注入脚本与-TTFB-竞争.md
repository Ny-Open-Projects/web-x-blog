---
title: [MFW-333→MFW-333] 第三方脚本的 TTFB 竞争治理
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW→333：三方脚本治理

**答**:
- 成本模型：第三方脚本平均占页面 JS 执行 40%+（Google/Algolia 研究）——且阻塞主线程挤掉 INP 预算
- 治理分级表：关键路径（支付 SDK）→ 直接 ESM 引入（可审计版本）；营销/统计 → Partytown worker 隔离（主线程零占用）或 server 端代理上报（TTHTTP 化——脚本不进浏览器）；低价值 → 砍（年度审计强制——每个三方脚本要有 owner 与续期）
- 加载协议：统一调度器（队列 + 交互后加载 idle 注入——首屏窗口禁三方）；失败隔离（try-catch + 超时杀死——三方挂起不拖死登录态初始化）
- 度量：三方脚本 own CPU 时间（Long Task 归因按注入 URL）——数据驱动续期评审

```text
分级：关键=ESM / 重执行=Partycloud worker / 纯上报=server 代理 / 无主=年度砍
协议：调度器队列 + idle 注入 + 失败隔离超时
度量：按 URL 的 LongTask 归因 → 续期评审
```
