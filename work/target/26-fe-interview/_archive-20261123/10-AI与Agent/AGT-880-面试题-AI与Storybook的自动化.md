---
title: [AGT-880] 组件的 Story/文档（story/controls 用例）AI 自动生成与维护，要点？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-880：组件的 Story/文档（story/controls 用例）AI 自动生成与维护，要点

**答**：
- 生成策略：从 props 类型与 JSDoc 生成 stories（基础态/变体态/边界态：超长文本/空数据/极端值）——边界态是 AI 生成 Story 的最大价值（人懒得写但回归最需要）。
- 维护联动：props 类型变更时 Story 自动检测失配（controls 类型对不上），AI 生成更新 diff 供确认——Story 不再是"发布时写一次然后过期"。
- 视觉回归闭环：Story 即快照源，AI 生成的 Story 直接进视觉回归基线（组件变更影响面可视化）。

```javascript
async function genStories(component) {
  const props = parseTypes(component);
  const stories = await ai.stories(props, {
    states: ['default', 'variants', 'edge'],       // 边界态必含
    edge: ['超长文本', '空数据', '极端数值'],
  });
  linkSnapshot(stories);                           // Story即快照源
  watchProps(component, (diff) =>
    proposeStoryUpdate(diff, stories));            // 类型变更联动
  return stories;
}
```

