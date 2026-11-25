---
title: [AGT-505] 在业务系统里集成 AI 能力：侧边栏 Copilot、行内辅助、独立页三种嵌入模式怎么选？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-505：在业务系统里集成 AI 能力：侧边栏 Copilot、行内辅助、独立页三种嵌入模式怎么选

**答**：
- 行内辅助（编辑器补全/改写）：打断成本最低、上下文最准（光标处就是上下文），适合高频小动作；用 ghost text + Tab 接受。
- 侧边栏 Copilot：适合多轮任务与"针对当前页面"的问答，通过共享上下文桥（当前路由/选中项/表单值）注入业务上下文。
- 独立页：适合长任务、跨页面的工作流（报告生成、批量处理）。三种模式可以共存，选型看「任务长度 × 上下文所在位置」。

```javascript
// 上下文桥：业务页把当前上下文喂给侧边栏 Copilot
const contextBridge = {
  snapshot() {
    return {
      route: location.pathname,
      selection: window.getSelection()?.toString(),
      formState: currentForm?.getDirtyFields(),  // 正在编辑的字段
      entity: currentEntitySummary,               // 当前业务对象摘要
    };
  },
};
copilot.setSystemSuffix(() =>
  '当前用户正在查看：' + JSON.stringify(contextBridge.snapshot()));
```

