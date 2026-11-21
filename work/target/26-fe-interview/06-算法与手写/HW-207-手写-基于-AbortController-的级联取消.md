---
title: [HW-207] 手写级联取消——任务树 signal 传播（父取消子全部取消）与部分完成结果的保留
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：任务树取消：每个任务 child signal = AbortSignal.any([parent, own])——父取消级联传播子任务；已完成的任务结果保留（取消只影响未完成任务——部分结果可用）；取消原因沿树传递（诊断友好）。

```javascript
async function runTaskTree(node, parentSignal) {
  const own = new AbortController();
  const signal = AbortSignal.any?.([own.signal, ...(parentSignal ? [parentSignal] : [])])
    ?? parentSignal ?? own.signal;
  if (signal.aborted) throw new DOMException(signal.reason ?? 'aborted', 'AbortError');
  const value = await node.run({ signal });               // 任务自己监听 signal（可中断内部循环）
  const children = {};
  const childErrors = [];
  await Promise.allSettled((node.children ?? []).map(async (c) => {
    try { children[c.id] = await runTaskTree(c, signal); }          // 父 signal 传给子：级联
    catch (e) { childErrors.push({ id: c.id, msg: String(e) }); }
  }));
  return { value, children, childErrors };                // 部分结果保留（完成的不丢）
}
// 语义：
// 父 abort → signal 组合 → 子任务 fetch/sleep 全部 AbortError → 级联传播
// allSettled：某子失败/取消不影响兄弟与已完成结果 —— "取消尽量多收"
// 取消原因：signal.reason 沿树传递（'timeout' / 'user-cancel' 诊断友好）
// 应用：搜索树（主查询+联想+推荐并行）——用户改关键词取消整棵树，已完成的部分结果直接用
```

**评分点**：
- AbortSignal.any 组合父子 signal 的级联传播——本题核心。
- allSettled 部分结果保留（完成的不丢，取消只影响未完成）。
- 取消原因沿树传递（诊断）。
- 任务内部响应 signal（可中断循环，不只检查外层）。
