---
title: [FRP-395] 笔试：手写 Activity 简版（隐藏渲染 + 效果暂停）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-395：笔试：手写 Activity 简版

**答**：实现 `<Activity mode>` 语义的 mini 版：① mode='hidden'：children 的 DOM 移除但「状态保留」（vnode 树与 fiber/实例缓存）；② effect 暂停协议：hidden 时 pause 所有 effects（FRP-380 协议），visible 时 resume；③ 副作用挂起的语义校验（轮询/订阅在 hidden 期间不执行——与 display:none 的本质差异）；④ visible 切换即显（预渲染保留——无重渲染成本）；⑤ 多 Activity 嵌套（子 hidden 独立）。写出实现。

```javascript
const activityRegistry = new Map();   // key -> { vnode, container, effects }

function renderActivity(key, vnode, effects) {
  const container = document.createElement('div');   // 离屏容器(状态保留)
  mount(vnode, container);
  activityRegistry.set(key, { vnode, container, effects });
  effects.forEach((e) => e.run());
  return {
    setMode(mode) {
      const a = activityRegistry.get(key);
      if (mode === 'hidden') {
        a.container.remove();                        // DOM 移除
        a.effects.forEach((e) => e.pause());         // 效果挂起 — 与 display:none 的差异
      } else {
        document.body.appendChild(a.container);      // 即显(无重渲染)
        a.effects.forEach((e) => e.resume());        // 重跑重收集
      }
    },
    destroy() {
      const a = activityRegistry.get(key);
      a?.effects.forEach((e) => e.stop());
      activityRegistry.delete(key);
    },
  };
}
// 用法: tab 切换
const tab1 = renderActivity('tab1', <LogsPanel />, [tickerEffect, wsEffect]);
tab1.setMode('hidden');   // 状态保留 + 轮询/订阅暂停 (省资源)
tab1.setMode('visible');  // 即显 + 效果恢复
// 对照: display:none — DOM 留但 effect 照跑(浪费); unmount — 状态丢失
// Activity = 状态保留 + 效果挂起 (两全)
```

**评分点**：
- hidden = DOM 移除 + 效果 pause（与 display:none/unmount 的本质差异对照）
- resume 重跑重收集（暂停期间依赖变化能连上）
- 即显语义（预渲染保留，无重渲染）
- destroy 的完整清理
