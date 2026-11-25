---
title: [R19-398] 并发渲染边界：Context 与外部状态的撕裂场景
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## R19-398：并发渲染边界：Context 与外部状态的撕裂场景

**答**：
- 撕裂场景还原：低优渲染中途，外部 store 更新——树的上半部分读到旧值、下半部分（被打断后重渲染）读到新值——同一棵 commit 树两种数据
- Context 不会撕裂（React 保证渲染期快照一致）——撕裂只来自「绕过 React 的外部订阅」（直接读全局变量、非 useSyncExternalStore 的订阅）
- 症状识别：偶发的「列表与详情数据版本不一致」「计数器跳变」——并发 + 外部状态的特征组合
- 修复路径：外部状态接入 useSyncExternalStore（快照语义）；或在 store 层实现「版本戳 + 渲染期校验」
- 测试撕裂：故意在渲染中触发外部更新（mock 时间片）——撕裂的复现要控制渲染时序，一般用并发特性测试库

```javascript
// 反模式: 渲染中直读外部变量
function Bad() { return <div>{window.__store.value}</div>; }   // 可撕裂
// 正解
const v = useSyncExternalStore(store.subscribe, store.getSnapshot);  // 快照一致
```
