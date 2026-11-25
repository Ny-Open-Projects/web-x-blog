---
title: [MFW-239] 元框架错误处理三层一致性
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-239：错误处理三层一致性

**答**:
- 三层错误源：build（SSG 数据失败——fail-fast 还是降级）、runtime server（RSC/Action 抛错——error.js 边界 + 重试）、client（hydration 后交互错——本地边界）
- 一致性设计：错误分类统一（{ kind: 'transient'|'fatal'|'auth', retryable }）跨层传递——RSC 抛的 kind 到客户端 error.js 按同表渲染（重试按钮 vs 跳登录）
- build 期策略：关键页数据失败 → 构建失败（fail-fast 防坏产物上线）；非关键 → 占位降级 + 告警（构建成功的谎言要少说）
- 恢复动作标准化：transient → retry 按钮（调 router.refresh）；auth → 登录流；fatal → 通报 error 哨兵——动作跟 kind 走，不跟消息文案走

```javascript
// 统一错误类
class AppError extends Error { constructor(msg, kind, retryable) { ... } }
// app/error.tsx（按 kind 渲染动作）
if (error.kind === 'transient') return <Retry onClick={reset} />
if (error.kind === 'auth') return <LoginLink />
```
