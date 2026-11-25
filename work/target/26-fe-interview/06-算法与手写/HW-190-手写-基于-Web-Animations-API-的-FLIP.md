---
title: [HW-190] 手写 FLIP 动画通用实现——测量旧位→更新 DOM→反向变换→过渡归位（列表重排零依赖方案）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-190：手写 FLIP 动画通用实现——测量旧位→更新 DOM→反向变换→过渡归位（列表重排零依赖方案）
**答**：FLIP（First-Last-Invert-Play）通用实现——View Transitions 不支持时的零依赖方案：First 记录元素旧位置（getBoundingClientRect）→ Last 更新 DOM → Invert 计算 delta 反向 transform → Play 用 WAAPI 过渡到恒等（合成器路径）。

```javascript
function flip(container, mutate) {
  const els = [...container.children];
  const first = new Map(els.map((el) => [el.dataset.id, el.getBoundingClientRect()]));   // First
  mutate();                                               // Last：DOM 更新（重排/过滤/插入）
  const moved = [];
  for (const el of container.children) {
    const f = first.get(el.dataset.id);
    if (!f) continue;                                     // 新元素：用入场动画（fade-in）
    const l = el.getBoundingClientRect();
    const dx = f.left - l.left, dy = f.top - l.top;
    if (dx || dy) {
      moved.push(el.animate(
        [{ transform: `translate(${dx}px, ${dy}px)` }, { transform: 'none' }],
        { duration: 240, easing: 'ease-out', composite: 'add' },   // Invert+Play：WAAPI 合成器
      ));
    }
  }
  return Promise.allSettled(moved.map((a) => a.finished));   // 完成回调（供动画链编排）
}
// 用法：拖拽重排（HW-106）/筛选过滤后的列表重排
// flip(listEl, () => renderNewOrder(newList));
// 要点：
// 1. transform 反向 + 过渡到 none —— 合成器路径（PER-347），主线程零 layout 动画
// 2. composite: 'add' —— 与元素已有 transform（悬停缩放等）叠加不冲突
// 3. 新增/删除元素不参与 Invert（没有旧位置）—— 单独 fade 处理
// 4. View Transitions 可用优先用 VT（HW-151），FLIP 是降级/精细控制方案
```

**评分点**：
- FLIP 四步完整（First/Last/Invert/Play）与 WAAPI 合成器执行——本题核心。
- composite: 'add' 处理已有 transform 的叠加。
- 新增/删除元素单独处理（无旧位不 Invert）。
- 与 View Transitions 的降级关系（HW-151）。
