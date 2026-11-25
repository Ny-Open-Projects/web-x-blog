---
title: [MFW-314] Server-Driven UI 与 RSC 的异同
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-314：SDUI 与 RSC

**答**:
- 概念分界：SDUI（服务端下发 UI 描述——JSON 模板由客户端解释器渲染，App/低代码常用）vs RSC（服务端执行组件、传输已求值的树——客户端不解释只渲染）
- 能力对比：SDUI 灵活于「不发版改 UI」（模板热更）但受限于解释器组件白名单；RSC 类型安全 + 全 React 能力但改 UI 需部署
- 混合现实：移动端 SDUI + Web 端 RSC 共享同一「服务端编排层」（MFW-305 DTO 公式）——编排归一、表达分端
- 判定：需要 OTA 免发版改 UI → SDUI；全栈 React 且可随发版 → RSC（类型与 DX 压倒性优势）

```text
分界：SDUI=传输描述（解释器白名单，免发版）| RSC=传输结果树（全能力，随部署）
混合：编排层归一（DTO），表达分端（JSON 模板 / RSC 树）
```
