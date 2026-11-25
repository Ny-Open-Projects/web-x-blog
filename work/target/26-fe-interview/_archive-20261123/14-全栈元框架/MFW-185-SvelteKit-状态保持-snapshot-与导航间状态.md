---
title: [MFW-185] SvelteKit 的 snapshot 与导航间状态保持怎么做？
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-185：SvelteKit 的 snapshot 与导航间状态保持怎么做？
**答**：
- 问题：用户在列表页筛选/滚动/展开到第 3 层抽屉，点进详情再返回——load 重跑数据能回来，但 **UI 状态（筛选条件、滚动位置、展开项）丢了**。
- SvelteKit 的解法是 snapshot：`+page.svelte` 导出 `snapshot` 对象，`capture()` 序列化组件状态，导航离开前存、返回时 `restore()` 还原；存进 history.state，刷新即失效（只保「导航间」，不保持久）。
- 对比 Next：App Router 没有官方等价物，常见做法是把状态放 URL searchParams（可分享但会触发重新渲染）、或 Context + layout 不卸载的分区、或用 sessionStorage 自救。
- snapshot 语义边界：只跟随浏览器历史（forward/back），新开标签、刷新、直接跳转都没有；数据本身不该塞 snapshot（load 才是数据事实源），snapshot 只保 UI。
- 注意 capture 的对象必须可结构化克隆（不能含函数/DOM 节点），与脱水序列化约束一致。

```svelte
<script>
  let filters = $state({ q: '', page: 1, open: new Set() });
  export const snapshot = {
    capture: () => ({ ...filters, open: [...filters.open] }), // Set 不可克隆，转数组
    restore: (v) => { filters = { ...v, open: new Set(v.open) }; },
  };
</script>
```