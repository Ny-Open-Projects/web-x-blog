---
title: [AIC-516] AI 代码补全接受率度量
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-516：补全接受率度量

**答**:
- 补全接受率（Acceptance Rate）的度量维度：1) **总接受率**（accepted / total suggestions——总体 AI 有效性；2) **分维度接受率**：per-language（TypeScript > Markdown？）、per-file-type（server > test？）、per-time（上午 > 下午？疲劳效应）；3) **接受后的保留率**（接受 → 5 分钟后仍保留（用户没有 revert）——"接受 ≠ 正确"（用户接受了但有 bug——保留率 = 实际质量）；4) **拒绝原因分析**（Tab Escape = 不相关；Esc = 方向错误——拒绝的类型分析）。
- 度量的实现：IDE 插件埋点（Copilot/Cursor 的 telemetry——opt-in RBL-679）；「接受的粒度」：整块接受（Tab 全部）vs 部分接受（逐词接受 Cmd+→——部分接受的接受率 = 更精细的质量度量）。
- 追问钩子：为什么「接受率 80%」不能直接解读为「AI 很好」？——接受率高可能是「AI 补全的都是简单 boilerplate」（接受容易但价值低）；也可能是「用户不审查直接 Tab」（接受率 = 盲目信任——质量问题）；「有价值的度量」：接受后的**修改率**（接受后又改了多少行——修改越多 = AI 生成越不准）+ **保留率**（接受后 5 分钟的存活率）+ **有意义的接受**（接受了非 boilerplate 的代码——逻辑生成的接受率才是 AI 质量指标）。

```typescript
// 补全事件追踪
interface CompletionEvent {
  ts: number;
  language: string;
  fileType: string;
  action: 'accepted' | 'rejected' | 'partial';
  linesAccepted: number;
  modifiedAfterAccept: number;   // 接受后修改的行数
  revertedWithin5min: boolean;
  isBoilerplate: boolean;        // import/类型声明等
}
// 接受率与质量分析
function analyzeAcceptance(events: CompletionEvent[]) {
  const total = events.length;
  const accepted = events.filter(e => e.action === 'accepted' || e.action === 'partial');
  const acceptRate = total ? +(accepted.length / total * 100).toFixed(1) : 0;
  // 修改率：接受后修改的比例
  const modified = accepted.filter(e => e.modifiedAfterAccept > 0);
  const modifyRate = accepted.length ? +(modified.length / accepted.length * 100).toFixed(1) : 0;
  // 保留率：5 分钟内未 revert
  const retained = accepted.filter(e => !e.revertedWithin5min);
  const retainRate = accepted.length ? +(retained.length / accepted.length * 100).toFixed(1) : 0;
  // 逻辑生成的接受率（排除 boilerplate）
  const logicAccepted = accepted.filter(e => !e.isBoilerplate);
  const logicAcceptRate = total ? +(logicAccepted.length / total * 100).toFixed(1) : 0;
  return { acceptRate, modifyRate, retainRate, logicAcceptRate };
}
```
