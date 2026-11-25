---
title: [MFW-257] Next.js × React Query 双缓存一致性
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-257：Next × React Query 双缓存一致性

**答**:
- 并存的两套缓存：Next fetch/Data Cache（服务端）与 Query 缓存（客户端）——同 key 数据双写必漂移（服务端改了客户端不知）
- 统一策略：单一真相源原则——交互数据归 Query（服务端不缓存该数据：fetch no-store 直透）、静态内容归 Next 缓存（客户端只读不写）——按数据域划边界而非按框架能力混用
- 桥接点：SSR 预取用 Query（MFW-192 脱水桥）让首屏与后续同一缓存——Next 缓存只承担「跨请求的渲染加速」不承担「客户端数据源」
- 失效联动：Action 后双失效（服务端 tag + 客户端 key——MFW-201）是混用状态的代价；纯 Query 域只需单失效

```text
数据域分派：
交互频繁（列表/表单反馈）→ Query 单源（服务端 no-store 直透）
静态内容（文案/配置/SEO）→ Next 缓存单源
混用域 → 双失效（成本自知）
```
