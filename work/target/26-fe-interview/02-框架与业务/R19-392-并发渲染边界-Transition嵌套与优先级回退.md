---
title: [R19-392] 并发渲染边界：Transition 嵌套与优先级回退
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## R19-392：并发渲染边界：Transition 嵌套与优先级回退

**答**：
- 嵌套 Transition：transition 内再 startTransition——内层更新有独立 lane（更细粒度），内层打断不影响外层已提交部分……实际语义：嵌套更新合并为同一批 lane，内层不产生新的「可打断边界」——避免依赖嵌套行为（未文档化语义）
- 优先级回退（downgrade）：Transition 更新长时间未完成时 React 会尝试「降级提交」（渲染当前能完成的骨架）——连续交互下的 UI 渐进
- isPending 嵌套的显示：外层与内层各自 pending——UI 设计上「外层 pending 优先展示」，内层 pending 用于局部指示
- 与 useOptimistic 组合：transition 中的乐观状态在「transition 被取消」时回滚——乐观值生命周期绑定 transition
- 实战建议：transition 扁平使用（一个交互一个 transition），嵌套交给 React 内部——业务层不要发明嵌套语义

```jsx
function onFilter(v) {
  startTransition(() => {                    // 外层: 列表过滤
    setFilter(v);
    startTransition(() => {                  // 内层: 建议扁平化, 勿依赖嵌套语义
      setDetail(loadPreview(v));
    });
  });
}
```
