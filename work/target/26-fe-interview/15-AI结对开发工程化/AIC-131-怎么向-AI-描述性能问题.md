---
title: [AIC-131] 怎么向 AI 描述性能问题和视觉问题？「非文本证据」的供给技巧？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-131：怎么向 AI 描述性能问题和视觉问题？「非文本证据」的供给技巧？
**答**：
- 性能问题供给：火焰图/Performance 面板的**文本摘录**（长任务栈、组件渲染次数、耗时排行）+ 复现条件（数据量、交互序列）——AI 消费的是结构化数字与栈，不是感觉描述。
- 视觉问题供给：截图（多模态模型）+ 精确坐标/元素描述 + 设计稿对照（给出「期望 vs 实际」两张图）+ 相关 CSS 片段；纯文字说「按钮偏了」几乎必然答错。
- 通用技巧：证据要「量化」——「慢」不如「LCP 4.2s、长任务 800ms 在 useSyncExternalStore 通知链」；「偏了」不如「左偏 12px，相对设计稿 x=312」。
- 验证闭环：性能修复后重新测量对比（数字说话），视觉修复后截图对比——非文本问题的验证也必须回到非文本证据，不能只看代码。
- 追问钩子：这题考「多模态时代的调试素养」，核心公式：非文本问题 = 量化证据 + 对照物 + 可重复的复现路径。

```javascript
// 性能证据摘录器：从 trace JSON 提取 AI 可读摘要
function perfEvidence(trace) {
  const longTasks = trace.tasks.filter(t => t.duration > 50)
    .sort((a, b) => b.duration - a.duration).slice(0, 5);
  const renders = topRenders(trace.componentUpdates, 5); // 渲染次数 top5
  return {
    lcp: trace.lcp, cls: trace.cls,
    longTasks: longTasks.map(t => `${t.duration}ms ${t.stackTop}`),
    reRenderHot: renders.map(r => `${r.name} ×${r.count}`),
  };
}
```
