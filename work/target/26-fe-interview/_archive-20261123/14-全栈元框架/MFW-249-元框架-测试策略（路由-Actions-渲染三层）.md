---
title: [MFW-249] 元框架的测试策略（路由/Action/渲染三层）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-249：元框架测试三层

**答**:
- Action/ServerFn 单测：直接 import 调用（纯函数化——DB mock 注入），schema 边界用表驱动——RPC 黑盒在单测层拆开
- 路由/渲染集成：框架测试工具渲染路由树（Next 的 test 模式 / vitest+@testing-library）断言 RSC 输出关键结构（不逐字符对比——flight 序列化不稳定）；mock 数据层（Query/§fetch stub）
- E2E 冒烟：真实 build+start（prod 模式——dev 行为不代表 prod 缓存语义）走关键路径——缓存头/ISR 行为只能在 prod 模式验证
- 反模式清单：只测 dev 模式（缓存语义全错位）、mock fetch 到失真（丢 tag 语义——用框架提供的缓存 mock）、无 prod 冒烟

```text
三层：Action 单测（schema 表驱动）→ 路由渲染集成（结构断言）→ prod E2E 冒烟（缓存/头验证）
红线：缓存与头类断言必须在 next build && next start 下跑
```
