---
title: [ZSM-841] 架构演进终局：从「全局 store」到「分层状态联邦」
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-841：架构演进终局：从「全局 store」到「分层状态联邦」

**答**：
- 把本库全部知识收敛成一个终局架构判断——React 生态的状态架构正从「全局 store 单体」演进为「**分层状态联邦**」：
- **联邦五层**：① 服务端渲染态（RSC 直读，零客户端状态）② 服务端缓存态（TanStack Query + hydration）③ 客户端会话态（Zustand 小 store 群 + registry 分层）④ 流程态（XState actor 按需挂载）⑤ 展示态（CSS/平台原生：:has/View Transition/scroll-driven——能进平台的不进 JS）。
- 联邦的治理接口：层与层之间只有三种合法连接——**注入**（SSR → 缓存 → store 的初始值单向流）、**失效**（mutation → invalidate → refetch 的广播）、**事件**（业务事件 → 状态机的 send）——禁止跨层直接 import 深层字段。
- 每层的技术选型判断（不是哪个库最好，而是哪层用哪个库）：缓存语义复杂度决定 ② 用 Query；交互粒度决定 ③ 用 Zustand/Jotai；可观测流程决定 ④ 用 XState——「分层先于选型」。
- 这个终局判断的验证：2026 年主流量产架构（Next.js + TanStack + Zustand 小 store + 少量 XState）已在向此收敛——不是预测是观察。
- 追问钩子：联邦化后「全局 store 时代」的哪些资产仍然有效——本库 12 个复用概念（对账器/seq/幂等键/命令栈…）全部跨层适用；变化的是「放哪层」，不变的是「怎么设计」。

```javascript
// 分层状态联邦（终局架构）
const STATE_FEDERATION = {
  L1_服务端渲染态: {
    tech: 'RSC 直读（ZSM-795）',
    rule: '渲染产物不进客户端 store',
    bridge: 'props 可序列化（796 校验）',
  },
  L2_服务端缓存态: {
    tech: 'TanStack Query + hydration（632）',
    rule: 'staleTime/gcTime/invalidate 语义归缓存层',
    bridge: 'mutation → invalidate → refetch',
  },
  L3_客户端会话态: {
    tech: 'Zustand 小 store 群 + registry 分层（776）',
    rule: '交互态/乐观队列/多选集——共享半径最小化',
    bridge: '事件 → 状态机 send',
  },
  L4_流程态: {
    tech: 'XState actor 按需挂载（674）',
    rule: '多步流程/生命周期绑定',
    bridge: 'done 事件 → 缓存失效',
  },
  L5_展示态: {
    tech: 'CSS :has / View Transition / scroll-driven（836）',
    rule: '能进平台的不进 JS',
    bridge: '无（平台原生）',
  },
  三种合法连接: ['注入（初始值单向流）', '失效（invalidate 广播）', '事件（send）'],
  禁止: '跨层直接 import 深层字段',
  不变资产: '12 个复用概念（对账器/seq/幂等键/命令栈…）跨层适用——变的是放哪层，不变的是怎么设计',
}
```
