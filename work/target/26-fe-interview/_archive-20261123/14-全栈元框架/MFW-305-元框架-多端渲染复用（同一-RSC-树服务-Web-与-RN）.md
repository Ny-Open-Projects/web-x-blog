---
title: [MFW-305] 同一数据服务多端（RSC 思想外溢到 RN/桌面）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-305：多端渲染复用

**答**:
- 可复用层剥离：RSC 树的价值在「数据获取+组合逻辑」服务端化——把 loader/数据组装抽成 framework-free 模块（纯 TS 函数返回 DTO），Web/RN/桌面各自薄渲染层消费——复用的是「服务端数据编排」不是组件树
- RN 侧方案：Expo Router 文件路由同构心智 + fetch 同一 BFF；或轻量 RPC（tRPC 类）共享 server 函数——按端选择传输形态（RSC payload 仅 Web）
- 边界纪律：DTO 禁含 Web 概念（className/href 语义）——端无关字段命名（action 目标用逻辑名由端解析）
- 成本警告：三端「真同构」的测试矩阵（行为一致性×3）——先证明两端收益再上第三端

```text
复用公式：server 编排（framework-free DTO） + 各端薄渲染
传输：Web=RSC payload；RN/桌面=tRPC/REST 同 BFF
红线：DTO 无端概念字段；先两端验证再扩第三端
```
