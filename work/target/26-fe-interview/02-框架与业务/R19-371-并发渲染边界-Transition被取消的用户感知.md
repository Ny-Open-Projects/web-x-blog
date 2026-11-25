---
title: [R19-371] 并发渲染边界：Transition 被取消的用户感知设计
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## R19-371：并发渲染边界：Transition 被取消的用户感知设计

**答**：
- 取消语义：Transition 渲染中被新的高优更新打断 → 低优树丢弃重来——用户看到的永远是「旧内容或新内容」，无中间态；但要处理「连续打断永不完成」的饿死
- 饿死防护：连续输入场景（打字筛选）用 deferredValue/防抖在业务层收敛输入频率；React 内部对 Transition 有 retry 调度（不至于完全饿死但可能延迟久）
- isPending 的 UX 设计：pending 期间显示什么？——「旧内容 + 进度指示」优于骨架屏（避免布局跳动）；React 19 的 `useTransition` + Activity 组合可预渲染
- 打断后的数据一致性：Transition 内 fetch 在渲染函数中（use）时被打断——请求已完成但组件卸载；用「数据缓存层」承接（请求结果进缓存，重渲染直接命中）
- 设计准则：可打断更新的 UI 必须能表达「进行中」——否则用户不知道点击有没有生效

```jsx
const [isPending, startTransition] = useTransition();
function onSelect(id) {
  startTransition(() => {
    select(id);                      // 大树切换, 可打断
  });
}
// pending 期间: 旧面板保持 + 顶部进度条(isPending)
{isPending && <TopProgress />}
```
