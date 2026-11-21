---
title: [AGT-241] MCP 协议总览——Model Context Protocol 解决什么问题？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-241：MCP 是什么——它解决了工具生态的什么问题？

**答**:
- 解决 N×M 集成爆炸：以前每个 AI 应用接每个工具都要写一遍集成（M 个应用×N 个工具=N×M 套胶水）；MCP 把它变成 N+M——工具方实现一次 MCP Server，应用方实现一次 MCP Client，中间用标准协议对话。
- 三方角色：Host（AI 应用，如 IDE/聊天助手）、Client（Host 内维护与单个 Server 的连接）、Server（暴露能力的轻量服务）——Server 对外提供三类原语：Tools（模型可调用的操作）、Resources（可读取的数据）、Prompts（预置模板）。
- 协议要点：基于 JSON-RPC 2.0，支持 stdio（本地进程）与 Streamable HTTP（远程）传输；连接生命周期含 initialize（能力协商）与发现阶段（tools/list 等）；能力是动态可发现的，Client 侧无需硬编码。
- 对前端工程师的意义：MCP 是"Agent 时代的 API 标准"——把内部系统能力封装成 MCP Server，就能被任意支持 MCP 的 Agent 使用，类似当年 REST 统一了服务间通信。

```text
MCP 架构：
Host(应用) → Client ↔ JSON-RPC ↔ Server(工具)
Server 三原语：
  Tools:      模型主动调用的动作（createIssue）
  Resources:  应用读取的数据（file://, db://）
  Prompts:    预置提示模板
传输：stdio（本地）/ Streamable HTTP（远程）
生命周期：initialize(能力协商) → 发现
  (tools/list) → 调用(tools/call) → 关闭
价值：N×M 集成 → N+M，生态复用。
```
