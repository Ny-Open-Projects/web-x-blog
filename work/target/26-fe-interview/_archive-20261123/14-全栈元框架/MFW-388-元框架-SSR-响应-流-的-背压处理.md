---
title: [MFW-388→MFW-388] SSR 流式响应的背压处理（慢客户端不吃满服务器）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-388：流式背压

**答**:
- 问题：renderToPipeableStream 对 2G 慢客户端输出——pipe 不背压会缓冲积压在服务端内存（万级慢用户=OOM）；React 流基于 Node stream 已有背压语义，但「上游 DB 拉取」不会自动停
- 端到端背压链：socket 可写水位 → React 通知 → Suspense 段的继续求值延后 → 数据层 fetch 暂停（分段拉取 cursor 化——段间检查 shouldContinue）——把 TCP 拥塞信号传回 DB 游标
- 简化务实版：慢客户端占比低时用「响应整体超时 + 中途放弃」（放弃时 Abort 传播 MFW-361 断 DB）——背压全套只在长视频/大列表流式产品做（复杂度按收益分配）
- 度量：server 端 per-req 缓冲字节 P95（>阈值=背压失效）+ 慢客户端断开率

```text
全链：socket 水位 → React 段延后 → cursor 化 fetch 段间检查
务实：一般站=超时+Abort 传播即可；全背压留给流媒体产品
度量：per-req 缓冲 P95 / 慢客户端断开率
```
