---
title: [MFW-379→MFW-379] 前端 Span 补全（让 trace 里有用户视角段落）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW→379：前端 Span 补全

**答**:
- 缺口：服务端 trace 完整但「用户等待感」缺前段（点击→发起）与后段（响应→可交互）——trace 价值打折（MFW-297 只做了传 id）
- 补全四段 span：interaction（点击处理）、fetch（含排队时间——浏览器 Resource Timing 对齐）、hydration/transfer（RSC payload 解析+渲染提交）、INP 段（MFW-490 交互延迟）——统一挂到同一 traceId（W3C 出站头已打通）
- 采样与成本：前端 Span 走尾部采样（慢会话/错误会话全保——正常会话 1%）；长度上限（单会话 span ≤200——防死循环组件刷爆配额）
- 消费场景：支持工单输入 traceId → 完整时间轴（用户点了什么→哪个请求慢→哪段渲染卡）——客服到工程师零转译

```text
四段：interaction / fetch(含排队) / hydration / INP —— 同 traceId 串联
成本：尾采样（慢+错误全保）+ 单会话 span 上限
价值：工单 traceId → 用户视角完整时间轴
```
