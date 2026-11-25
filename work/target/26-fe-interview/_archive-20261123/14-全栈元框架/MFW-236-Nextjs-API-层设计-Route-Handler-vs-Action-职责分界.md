---
title: [MFW-236] Route Handler 与 Server Action 的职责分界
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-236：Route Handler vs Server Action 职责分界

**答**:
- 分界法则：Server Action = 「本站 UI 触发的内部变更」（类型安全/无版本负担）；Route Handler = 「对外 API」（webhook 回调/开放接口/移动端消费/定时任务入口）
- 决策细则：需要稳定契约（第三方消费/版本化 /v1/）→ Handler；纯 UI 交互（点赞/表单）→ Action（省一层 API 设计）；需 GET 语义/可缓存 → 只能 Handler（Action 是 POST）
- 混用反模式：把 Handler 当内部 RPC 给自己前端调（绕过 Action 白写类型与序列化层）；把 Action 暴露给第三方（无版本化能力，改动即破坏）
- 安全差异：Action 天然带 origin 校验（CSRF 缓解），Handler 需要自建（签名/限流/鉴权中间件）

```text
分界速查：
本站 UI 变更        → Server Action（类型安全/防 CSRF 内建）
外部消费/webhook/GET → Route Handler（版本化/可缓存/自主鉴权）
反模式：内部 UI 走 Handler；第三方调 Action
```
