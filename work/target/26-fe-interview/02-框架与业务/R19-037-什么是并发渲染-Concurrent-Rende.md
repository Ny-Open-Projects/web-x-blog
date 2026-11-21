---
title: [R19-037] 什么是并发渲染 Concurrent Rendering？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-037：什么是并发渲染 Concurrent Rendering？
**答**：
- 并发渲染让 React 可以"准备"多个版本的 UI，渲染过程可中断、暂停、放弃后重来。
- 本质是优先级机制：紧急更新（输入、点击）优先，非紧急更新（大列表、过滤）让路。
- 对外暴露的入口是 startTransition、useTransition、useDeferredValue、Suspense。
- 最终提交仍是同步的，保证 UI 不会出现半成品撕裂状态。

```jsx
import { startTransition, useState } from 'react';

function Tabs({ tab }) {
  const [activeTab, setActiveTab] = useState(tab);

  function selectTab(nextTab) {
    // 标记为非紧急更新：渲染可中断，切换很重的 Tab 不会卡住界面
    startTransition(() => {
      setActiveTab(nextTab);
    });
  }

  return <button onClick={() => selectTab('comments')}>评论</button>;
}
```
