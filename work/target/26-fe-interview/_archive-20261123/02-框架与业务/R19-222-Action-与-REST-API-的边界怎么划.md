---
title: [R19-222] Server Actions 与 REST API 的边界怎么划分？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-222：Server Actions 与 REST API 的边界怎么划分？
**答**：
- Action 适合「本应用 UI 驱动的变更」：表单提交、按钮触发的写操作，类型安全、无需版本化。
- REST/Nitro route 适合「对外契约」：开放 API、webhook 回调、移动端复用、需要 CDN 缓存的读接口。
- 读数据优先 RSC 直接取数（不走 action）；写数据走 action；两者都不需要自建 BFF 中转层。
- 混合现实：已有微服务时，action 是「编排层」（聚合下游 REST），不是替代。
- 面试表达：用「对内 action / 对外 route」一句话收束。
