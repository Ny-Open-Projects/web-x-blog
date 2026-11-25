---
title: [FRP-247] 测试栈选型：Jest 还是 Vitest？论证要点？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-247：Jest 还是 Vitest？
**答**：
- Vitest：原生 ESM/TS、Vite 共享转换管线（配置零重复）、速度显著快、与 Vite 项目零摩擦——新项目默认。
- Jest：生态历史最厚（snapshot/mock 库兼容）、Node 双端项目通用、稳定保守——存量 Jest 仓库迁移成本 vs 收益要算账。
- 迁移判据：构建已迁 Vite → Vitest 必选；monorepo 混合构建 → 统一到 Vitest 降低双栈维护。
- 面试亮点：说「测试栈选型跟随构建工具」——转换管线一致才是速度与配置一致性的根源。
