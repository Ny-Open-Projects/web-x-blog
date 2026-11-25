---
title: [R19-374] React 与 Signal 的并发模型对比：渲染模型差异
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## R19-374：React 与 Signal 的并发模型对比：渲染模型差异

**答**：
- 根本差异：React 是「拉模型」（渲染时读状态，快照一致）；Signal 是「推模型」（状态变化直接推送订阅者）——推模型无快照语义，天然无 tearing 但也没有并发渲染的时间旅行
- React 并发渲染的前提：状态读取是「快照」（render 期间不变）——Signal 库在 React 内用 useSyncExternalStore 模拟快照（React 语义兼容层）
- 性能差异：Signal 细粒度更新跳过组件树 diff；React 靠 memo/bailout 收敛——「编译时/手动优化 vs 细粒度运行时」两条技术路线
- React Compiler 的意义：自动 memo 让「快照模型 + 自动细粒度」兼得——React 阵营对 Signal 路线的回应
- 面试表达：不要说「Signal 一定更快」——不同负载（大列表 vs 深更新链）结论不同；给「更新传播路径长度」的量化框架

```text
React:  set → schedule → render(读快照) → diff → commit   [拉]
Signal: set → 通知订阅 → 直接更新 DOM 绑定                  [推]
React 内嵌 Signal: useSyncExternalStore 快照化, 失去细粒度但保并发语义
```
